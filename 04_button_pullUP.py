import machine
import utime
#PULL_UP 代表 pin4 = 高電位 ，按鈕另一端需要接GND
button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
#不按下執行應為 1 ; 按下後執行應為 0
print(button.value())