import machine
import utime
#PULL_DOWN 代表 pin4 = 低電位 ，按鈕另一端需要接正電 
button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)
#不按下執行應為 0 ; 按下後執行應為 1
print(button.value())