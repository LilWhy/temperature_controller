import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)

resp = spi.readbytes(2)
temp = ((resp[1] + resp[0]*256)/8)*0.25
time.sleep(1)
temp += ((resp[1] + resp[0]*256)/8)*0.25
time.sleep(1)
temp += ((resp[1] + resp[0]*256)/8)*0.25
temp = temp // 3
print(temp)
