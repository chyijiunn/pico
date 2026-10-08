from machine import RTC
import time

# 初始化 RTC 時鐘
rtc = RTC()

while True:
    # 取得目前時間
    current_time = rtc.datetime()
    # 格式化顯示時間
    print('{:02d}/{:02d}-{:02d}:{:02d}:{:02d}'.format(current_time[1], current_time[2],current_time[4], current_time[5], current_time[6]))
    # 每秒鐘更新一次
    time.sleep(1)