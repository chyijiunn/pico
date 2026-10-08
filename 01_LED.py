import machine
LED = machine.Pin(25,machine.Pin.OUT)#控制內建的LED
LED.value(1)