from machine import ADC
temp  = ADC(4)
'''
Pico 電壓以 3.3V 運作，
ADC 腳位 3.3V 電壓，傳回 65535 的值，
            0 V 電壓，傳回數值 0。
            腳位施加的電壓介於 0 至 3.3V 之間時，獲得兩者間的值 V_temp
據 Pico 板 datasheet:
	27 ˚C 時會提供 0.706V 的電壓，
	升高 1 ˚C ，電壓降 1.721 毫伏特，即 0.001721 伏特
'''

V_temp = temp.read_u16()* 3.3 / 65535
˚C = 27 - (V_temp - 0.706) / 0.001721
print(˚C)