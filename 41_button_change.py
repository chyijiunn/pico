from machine import Pin, PWM,I2C,ADC
from ssd1306 import SSD1306_I2C
from utime import sleep
import _thread

i2c=I2C(0,sda=Pin(20), scl=Pin(21), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)

buzzer = PWM(Pin(7))
buzzer.freq(500)
buzzer.duty_u16(0)

buttonR = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)#press = 0 , unpress = 1
buttonL = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)

tempAlarm = 15

def button_thread():
    global tempAlarm
    while True:
        if buttonR.value() == 0:tempAlarm = tempAlarm + 1
        if buttonL.value() == 0:tempAlarm = tempAlarm - 1
        if buttonR.value() == 0 and buttonL.value() == 0:break
        sleep(0.2)
    
_thread.start_new_thread(button_thread, ())

oled.fill(0)
while True:
    ˚C = 27 - (ADC(4).read_u16()* 3.3 / 65535 - 0.706) / 0.001721
    oled.text('Now:'+str(˚C),0,20)
    oled.text('Alarm < '+str(tempAlarm),0,40)
    oled.show()
    sleep(1)
    oled.fill(0)
    
    if ˚C < tempAlarm:
        buzzer.duty_u16(1000)
        sleep(0.3)
        buzzer.duty_u16(0)
