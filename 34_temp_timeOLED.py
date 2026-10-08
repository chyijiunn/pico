from machine import ADC,Pin, I2C,RTC
from ssd1306 import SSD1306_I2C
from time import sleep

i2c=I2C(0,sda=Pin(16), scl=Pin(17), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)
temp  = ADC(4)

rtc = RTC()

while True:
    current_time = rtc.datetime()
    V_temp = temp.read_u16()* 3.3 / 65535
    ˚C = round((27 - (V_temp - 0.706) / 0.001721),2)
    oled.fill(0)
    oled.text('Temp:'+str(˚C),0,0)
    oled.text('{:02d}/{:02d}-{:02d}:{:02d}:{:02d}'.format(current_time[1], current_time[2],current_time[4], current_time[5], current_time[6]),0,10)
    oled.show()
    sleep(1)
