from flask import Flask, request, url_for, redirect, render_template
import spidev
import time
import smbus
import os
import sys
from pyA20.gpio import gpio
from pyA20.gpio import port


# Define some device parameters
I2C_ADDR  = 0x27 # I2C device address
LCD_WIDTH = 16   # Maximum characters per line

# Define some device constants
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

LCD_BACKLIGHT  = 0x08  # On
#LCD_BACKLIGHT = 0x00  # Off

ENABLE = 0b00000100 # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

#Open I2C interface
bus = smbus.SMBus(0)  # Rev 1 Pi uses 0 (and Orange PI PC, for pins 3 and 5)

app = Flask(__name__)



@app.route("/index", methods=['POST', 'GET'])
@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")



@app.route("/modes", methods=['POST', 'GET'])
def modes():
    if request.method == 'POST':
        return redirect(url_for('modes'))
    return render_template("modes.html")

@app.route("/graph", methods=['POST', 'GET'])
def graph():
    if request.method == 'POST':
        return redirect(url_for('graph'))
    return render_template("graph.html")

@app.route("/temperature", methods=['POST', 'GET'])
def temperature():
    temp = temperature_check()
    if temp <= 1:
        return ("Термопара не подключена")
    else:
        return (str(temp))

@app.route("/start_record", methods=['POST', 'GET'])
def start_record():
    if request.method == 'POST':
        f = open('temperature_mode.txt', 'w')
        i = 1
        for data in request.get_json():
            if i == 2:
                i = 1
                f.write(data + '\n')
            else:
                i += 1
                f.write(data + ' ')
        f.close()
    start_working()
    return render_template("graph.html")

def temperature_check():
    spi = spidev.SpiDev()
    spi.open(0,0)
    resp = spi.readbytes(2)
    temp = ((resp[1] + resp[0]*256)/8)*0.25
    return temp

def start_working():
    lcd_byte(0x01, LCD_CMD)
    records = []
    with open("temperature_mode.txt", "r") as f:
        for line in f.readlines():
            records.append(line)
    while (records):
        cur_mode(records.pop(0))

def cur_mode(line):
    lst = line.split()
    temperature = int(lst[0])
    time_set = int(lst[1])

    lcd_init()

    signal = port.PG7
    gpio.init()
    gpio.setcfg(signal, gpio.OUTPUT)

    while (time_set):
        minute = 60
        while (minute):
            cur_temperature = temperature_check()
            lcd_string("SET" + "{}".format(temperature),LCD_LINE_1)
            lcd_string("CUR" + "{}".format(cur_temperature),LCD_LINE_2)
            if cur_temperature < temperature:
                gpio.output(signal, 1)
            else:
                gpio.output(signal, 0)
                minute = minute - 1
            time.sleep(1)
        time_set = time_set - 1
        


def lcd_init():
    # Initialise display
    lcd_byte(0x33,LCD_CMD) # 110011 Initialise
    lcd_byte(0x32,LCD_CMD) # 110010 Initialise
    lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
    lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off 
    lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
    lcd_byte(0x01,LCD_CMD) # 000001 Clear display
    time.sleep(E_DELAY)  

def lcd_byte(bits, mode):
    # Send byte to data pins
    # bits = the data
    # mode = 1 for data
    #        0 for command

    bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
    bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

    # High bits
    bus.write_byte(I2C_ADDR, bits_high)
    lcd_toggle_enable(bits_high)

    # Low bits
    bus.write_byte(I2C_ADDR, bits_low)
    lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
    # Toggle enable
    time.sleep(E_DELAY)
    bus.write_byte(I2C_ADDR, (bits | ENABLE))
    time.sleep(E_PULSE)
    bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
    time.sleep(E_DELAY)

def lcd_string(message,line):
    # Send string to display

    message = message.ljust(LCD_WIDTH," ")

    lcd_byte(line, LCD_CMD)

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]),LCD_CHR)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True) 