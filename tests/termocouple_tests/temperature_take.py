import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)

while True:
    resp = spi.readbytes(2)
    temp = ((resp[1] + resp[0]*256)/8)*0.25
    print (temp)
    time.sleep(1)
