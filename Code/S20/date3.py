import time

B_YEAR = 1998

now_tm = time.gmtime()

print(now_tm.tm_year - B_YEAR)

# 08.12.2020 12:12

print(time.strftime("%d.%m.%Y %H:%M", now_tm))
