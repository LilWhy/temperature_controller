import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)

while True:
    resp = spi.readbytes(2)
    #Умножаем на 0.25 для точности вычислений градусов
    temp = ((resp[1] + resp[0]*256)/8)*0.25
    print (temp)
    time.sleep(1)