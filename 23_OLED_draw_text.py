from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c=I2C(0,sda=Pin(16), scl=Pin(17), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)

oled.fill(0)
data = open('21_OLED_draw_text','r')

for line in data:
    for i in range(len(line)):
        oled.text(line , 0 , i*10)
oled.show()
data.close()