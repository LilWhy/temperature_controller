import os
import sys

if not os.getegid() == 0:
    sys.exit('Script must be run as root')
    
from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port

signal = port.PG7

gpio.init()
gpio.setcfg(signal, gpio.OUTPUT)

try:
    print ("Press CTRL+C to exit")
    while True:
        gpio.output(signal, 1)
        sleep(2)
        gpio.output(signal, 0)
     exept KeyboardInterrupt:
        gpio.output(signal, 0)
   