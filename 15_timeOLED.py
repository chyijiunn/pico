from machine import ADC,Pin, I2C,RTC
from ssd1306 import SSD1306_I2C
from time import sleep

i2c=I2C(0,sda=Pin(16), scl=Pin(17), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)

rtc = RTC()

while True:
    oled.fill(0)
    current_time = rtc.datetime()
    print('Time: {:02d}:{:02d}:{:02d}'.format(current_time[4], current_time[5], current_time[6]))
    oled.text('Time: {:02d}:{:02d}:{:02d}',0,0)
    oled.show()
    sleep(1)