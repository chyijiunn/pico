import machine
import utime
button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15,machine.Pin.OUT)
while True:
    if button.value() == 1:
        led.value(1)
        utime.sleep(2)
    led.value(0)