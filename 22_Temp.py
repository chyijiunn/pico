from machine import ADC
temp  = ADC(4)
V_temp = temp.read_u16()* 3.3 / 65535
˚C = 27 - (V_temp - 0.706) / 0.001721
print(˚C)