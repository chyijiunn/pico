from machine import Pin
from utime import sleep
ledRed = machine.Pin(14,Pin.OUT)
ledYellow = machine.Pin(15,Pin.OUT)
ledGreen = machine.Pin(13,Pin.OUT)
sequence = list('121113')
while True:
        ledGreen.value(int(sequence[0]))
        sleep(int(sequence[1]))
        ledGreen.value(0)
        ledYellow.value(int(sequence[2]))
        sleep(int(sequence[3]))
        ledYellow.value(0)
        ledRed.value(int(sequence[4]))
        sleep(int(sequence[5]))
        ledRed.value(0)