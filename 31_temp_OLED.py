from machine import ADC,Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep

i2c=I2C(0,sda=Pin(16), scl=Pin(17), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)
temp  = ADC(4)

while True:
    V_temp = temp.read_u16()* 3.3 / 65535
    ˚C = round((27 - (V_temp - 0.706) / 0.001721),2)
    oled.fill(0)
    oled.text('Temp:'+str(˚C),0,0)
    oled.show()
    sleep(1)
    
