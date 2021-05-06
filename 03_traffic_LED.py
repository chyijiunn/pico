import machine
import utime
ledRed = machine.Pin(14,machine.Pin.OUT)
ledYellow = machine.Pin(15,machine.Pin.OUT)
ledGreen = machine.Pin(13,machine.Pin.OUT)
while True:
    #Red light first
    ledRed.value(1)
    utime.sleep(2)
    ledRed.value(0)
    #Gree light
    ledGreen.value(1)
    utime.sleep(5)
    ledGreen.value(0)
    #Yellow light
    ledYellow(1)
    utime.sleep(1)
    #Yellow twinkle
    ledYellow(0)
    utime.sleep(0.1)
    ledYellow(1)
    utime.sleep(0.3)
    ledYellow(0)
    utime.sleep(0.1)
    ledYellow(1)
    utime.sleep(0.2)
    ledYellow(0)
    utime.sleep(0.1)
    ledYellow(1)
    utime.sleep(0.1)
    #Red light again
    ledYellow.value(0)
    ledRed.value(1)
    utime.sleep(1)