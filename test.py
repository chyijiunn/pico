from machine import Pin, I2C
from ssd1306 import SSD1306_I2C#with package micropython-ssd1306
import utime

i2c=I2C(0,sda=Pin(20), scl=Pin(21), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.text('hello',0,0)
oled.text('hello2',0,10)#put text on (0,10)
oled.line(0,0,128,64,2)#draw a line from(x0,y0,x1,y1,1)
oled.pixel(64,30,1)#put a dot on (64,32)
oled.show()


buttonU = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_UP)#press = 0 , unpress = 1
buttonD = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)
buttonL = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP)
buttonR = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)
buttonA = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
buttonB = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    print(buttonU.value(),buttonD.value(),buttonL.value(),buttonR.value(),buttonA.value(),buttonB.value())
    utime.sleep(1)

