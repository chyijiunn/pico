from machine import Pin 
from utime import sleep

redLED = Pin(13,Pin.OUT)
greenLED = Pin(14,Pin.OUT)
yellowLED = Pin(15,Pin.OUT)

while True:
#控制紅燈
    redLED.value(1)
    sleep(3)
    redLED.value(0)
    sleep(0.5)
    #控制綠燈
    greenLED.value(1)
    sleep(3)
    greenLED.value(0)
    sleep(0.5)
    #控制黃燈
    for i in range(6):
        yellowLED.value(1)
        sleep(0.6-(i*0.1))
        yellowLED.value(0)
        sleep(0.6-(i*0.1))