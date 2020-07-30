from machine import Pin, I2C
from bh1750 import BH1750
from time import sleep_ms


# # init eps8266 i2c
# i2c = machine.I2C(Pin(5),Pin(4))

# init eps32 i2c
i2c = I2C(scl=Pin(22), sda=Pin(21))

s = BH1750(i2c)

while True:
    print(s.luminance(BH1750.ONCE_HIRES_1))
    sleep_ms(200)
