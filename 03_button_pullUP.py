import machine
import utime
#PULL_DOWN 代表 pin4 = 0 V ，按鈕另一端需要接地 
button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
#不按下執行應為 1 ; 按下後執行應為 0
print(button.value())