from machine import Pin, I2C
from ssd1306 import SSD1306_I2C#with package micropython-ssd1306

i2c=I2C(0,sda=Pin(16), scl=Pin(17), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)
buttonR = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)#press = 0 , unpress = 1
buttonL = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)

oled.fill(0)
x = 64
y = 32
while True:
    if buttonR.value() == 0:
        x = x + 1
    elif  buttonL.value() == 0:
        x = x - 1
    oled.pixel(x,y,1)
    oled.show()
    