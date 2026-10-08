from machine import Pin, PWM,I2C,ADC
from ssd1306 import SSD1306_I2C
from utime import sleep

i2c=I2C(0,sda=Pin(20), scl=Pin(21), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)
buzzer = PWM(Pin(7))
buzzer.freq(500)
buzzer.duty_u16(0)
oled.fill(0)
while True:
    ˚C = 27 - (ADC(4).read_u16()* 3.3 / 65535 - 0.706) / 0.001721
    oled.text(str(˚C),0,0)
    oled.show()
    sleep(1)
    oled.fill(0)
    if ˚C < 12:
        buzzer.duty_u16(1000)
        sleep(0.3)
        buzzer.duty_u16(0)
