import time
import board
from lib.adafruit_tca9548a import TCA9548A
from lib.adafruit_veml7700 import VEML7700

i2c = board.I2C()

tca = TCA9548A(i2c)

sun1 = VEML7700(tca[0])
sun2 = VEML7700(tca[1])
sun3 = VEML7700(tca[2])
sun4 = VEML7700(tca[3])
sun5 = VEML7700(tca[4])

while True:
    print(f"{sun1.lux}, {sun2.lux}, {sun3.lux}, {sun4.lux}, {sun5.lux}")
    time.sleep(0.05)
