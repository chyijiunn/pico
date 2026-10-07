from machine import Pin ,PWM
from utime import sleep
servoPIN = PWM(Pin(16))
servoPIN.freq(50)

center=-5#ini_motor
amplitude = 30
every_degree = 1
time_of_step = 1/1
duration = time_of_step/(2*amplitude)
def servo(degrees):
    if degrees > 90: degrees=90
    if degrees < -90: degrees=-90
    maxDuty=9000
    minDuty=1000
    newDuty=((maxDuty+minDuty)/2)+(((maxDuty-minDuty)/2)*(degrees/90))
    #print(degrees,'--->',int(newDuty))
    servoPIN.duty_u16(int(newDuty))

servo(center-(amplitude/2))
try:
    while 1:
        for i in range(center-amplitude,center+amplitude,every_degree):
            servo(i)
            sleep(duration)
        for i in range(center+amplitude,center-amplitude,-every_degree):
            servo(i)
            sleep(duration)
except KeyboardInterrupt:
    servo(center)
    print("\n偵測到鍵盤中斷，正在關閉系統...")

