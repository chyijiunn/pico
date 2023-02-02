from machine import Pin
from utime import sleep
AredLED = machine.Pin(13,Pin.OUT)
AgreenLED = machine.Pin(14,Pin.OUT)
AyellowLED = machine.Pin(15,Pin.OUT)
BredLED = machine.Pin(16,Pin.OUT)
BgreenLED = machine.Pin(17,Pin.OUT)
ByellowLED = machine.Pin(18,Pin.OUT)
#串列[A路口LED,B路口LED]
sequence =[[[5,0],[3,0],[0.5,0.1]],[[5,0],[3,0],[0.5,0.1]]]
#print(int(sequence[1][0]))
while True:
    #控制A紅燈
    AredLED.value(1)
    sleep(int(sequence[0][0][0]))
    AredLED.value(0)
    sleep(float(sequence[0][0][1]))
    #控制A綠燈
    AgreenLED.value(1)
    sleep(int(sequence[0][1][0]))
    AgreenLED.value(0)
    sleep(float(sequence[0][1][1]))
    #控制A黃燈
    for i in range(3):
        AyellowLED.value(1)
        sleep(float(sequence[0][2][0])-float(sequence[0][2][1])*i)
        AyellowLED.value(0)
        sleep(float(sequence[0][2][1]))
