from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin(7))
buzzer.freq(500)
    
for i in range(100,1000,100):
    buzzer.duty_u16(i)
    sleep(0.5)
    buzzer.duty_u16(0)
