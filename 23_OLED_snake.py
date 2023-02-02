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
def turnR():
    button_caculation = 0
    if buttonR.value() == 0:
        button_caculation = button_caculation + 1
        if button_caculation % 4 == 0: y =  y + 1
        if button_caculation % 4 == 1: x =  x + 1
        if button_caculation % 4 == 2: y =  y - 1
        if button_caculation % 4 == 3: x =  x - 1
        return x , y  
while True:
    turnR()
    print(x,y)
    sleep(1)
    '''
    oled.pixel(x,y,1)
    x = x + 1
    oled.show()
    '''
    sleep(0.2)