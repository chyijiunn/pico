from machine import Pin
from utime import sleep
SR501 = machine.Pin(1,Pin.IN , Pin.PULL_DOWN)
i = 1
def threhold(pin):
    sleep(1)
    if pin.value():
        print('Alarm!', i)
        i = i+1
SR501.irq(trigger=Pin.IRQ_RISING , handler=threhold)
#test2