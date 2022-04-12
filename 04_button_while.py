import machine
import utime
#PULL_DOWN 代表 pin4 = 0 V ，按鈕另一端需要接正電 
button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)
#不按下執行應為 0 ; 按下後執行應為 1
while True:
    print(button.value())
    utime.sleep(1)