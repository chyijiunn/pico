from machine import Pin #從 硬體 引入 腳位
from utime import sleep #從 時間 引入 睡眠
led = Pin(15,Pin.OUT) #控制外加的LED
while True:
    led.value(1)      #開
    sleep(3)            #持續3秒
    led.value(0)      #關
    sleep(3)            #持續3秒