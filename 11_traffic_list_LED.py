from machine import Pin
from utime import sleep
redLED = machine.Pin(13,Pin.OUT)
greenLED = machine.Pin(14,Pin.OUT)
yellowLED = machine.Pin(15,Pin.OUT)
#下為燈號[紅[亮秒數、暗],綠[亮,暗],黃[亮,暗遞減]]
sequence = [[3,0],[3,0],[0.5,0.1]]
while True:
#控制紅燈
    redLED.value(1)
    sleep(int(sequence[0][0]))
    redLED.value(0)
    sleep(float(sequence[0][1]))
    #控制綠燈
    greenLED.value(1)
    sleep(int(sequence[1][0]))
    greenLED.value(0)
    sleep(float(sequence[1][1]))
    #控制黃燈
    for i in range(3):
        yellowLED.value(1)
        sleep(float(sequence[2][0])-float(sequence[2][1])*i)
        yellowLED.value(0)
        sleep(float(sequence[2][1]))
