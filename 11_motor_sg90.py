from machine import Pin ,PWM
from utime import sleep
servoPIN = PWM(Pin(16))
servoPIN.freq(50)
servoPIN.duty_u16(x)    # x = 1000 ~ 9000
sleep(1)