from machine import Pin
from utime import sleep
ledRed = machine.Pin(14,Pin.OUT)
ledYellow = machine.Pin(15,Pin.OUT)
ledGreen = machine.Pin(13,Pin.OUT)
button_1 = Pin(16, Pin.IN, Pin.PULL_UP)
button_2 = Pin(17,Pin.IN,Pin.PULL_DOWN)
def traffic_mode_1 ():
    ledRed.value(1)
    sleep(2)
    ledRed.value(0)
    #Gree light
    ledGreen.value(1)
    sleep(5)
    ledGreen.value(0)
    #Yellow light
    ledYellow(1)
    sleep(1)
    #Yellow twinkle
    ledYellow(0)
    sleep(0.1)
    ledYellow(1)
    sleep(0.3)
    ledYellow(0)
    sleep(0.1)
    ledYellow(1)
    sleep(0.2)
    ledYellow(0)
    sleep(0.1)
    ledYellow(1)
    sleep(0.1)
    #Red light again
    ledYellow.value(0)
    ledRed.value(1)
    sleep(1)
    ledRed.value(0)
def traffic_mode_2 ():
    ledRed.value(1)
    ledYellow.value(1)
    ledGreen.value(1)
    sleep(2)
    ledRed.value(0)
    ledYellow.value(0)
    ledGreen.value(0)
while True:
    if button_1.value() == 0:
        traffic_mode_1()
    if button_2.value() == 1:
        traffic_mode_2()
        