from machine import Pin
from utime import sleep
AredLED = machine.Pin(13,Pin.OUT)
AgreenLED = machine.Pin(14,Pin.OUT)
AyellowLED = machine.Pin(15,Pin.OUT)
BredLED = machine.Pin(16,Pin.OUT)
BgreenLED = machine.Pin(17,Pin.OUT)
ByellowLED = machine.Pin(18,Pin.OUT)
AredLED.value(0)
AgreenLED.value(0)
AyellowLED.value(0)
BredLED.value(0)
BgreenLED.value(0)
ByellowLED.value(0)
while True:
    #控制A紅B綠
    AredLED.value(1)
    BgreenLED.value(1)
    sleep(3)
    BgreenLED.value(0)
    #控制A紅Ｂ黃
    ByellowLED.value(1)
    sleep(1.5)
    ByellowLED.value(0)
    #控制A紅Ｂ紅
    BredLED.value(1)
    sleep(1.5)
    AredLED.value(0)
    #控制B紅A綠
    AgreenLED.value(1)
    sleep(3)
    AgreenLED.value(0)
    #控制B紅A黃
    AyellowLED.value(1)
    sleep(1.5)
    AyellowLED.value(0)
    #控制A紅B紅
    AredLED.value(1)
    sleep(1.5)
    BredLED.value(0)