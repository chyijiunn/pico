from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c=I2C(0,sda=Pin(16), scl=Pin(17), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)

oled.fill(0)
data = open('22_drawData','r')
for line in data:
    a = line.split()
    for i in range(len(a)):
        xAxis = int(a[i].split(',')[0])
        yAxis = int(a[i].split(',')[1])
        oled.pixel(xAxis,yAxis,1)
data.close()

oled.show()