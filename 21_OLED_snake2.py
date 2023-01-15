from machine import Pin, I2C
from ssd1306 import SSD1306_I2C#with package micropython-ssd1306
from time import sleep

i2c=I2C(0,sda=Pin(16), scl=Pin(17), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)
buttonR = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)#press = 0 , unpress = 1
buttonL = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)

oled.fill(0)

global x ,y
x = 64
y = 32
button_caculation = 0    

while True: 
    if buttonR.value() == 0:button_caculation = button_caculation + 1
    if x > 128: x =0
    if x <0: x = 128
    if y > 64 : y =0
    if y <0 : y = 64
    if button_caculation % 4 == 0:
        oled.pixel(x,y,1)
        x = x + 1
        oled.show()
    if button_caculation % 4 == 1:
        oled.pixel(x,y,1)
        y = y + 1
        oled.show()
    if button_caculation % 4 == 2:
        oled.pixel(x,y,1)
        x = x - 1
        oled.show()
    if button_caculation % 4 == 3:
        oled.pixel(x,y,1)
        y = y - 1
        oled.show()
    #print(button_caculation,x,y)