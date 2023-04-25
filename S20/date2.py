import time

B_YEAR = 1998

now = time.time()

print(now)

now_tm = time.gmtime(now)

print(
    f"Evenimentul a avut loc in anul {now_tm.tm_year}, luna {now_tm.tm_mon}, ziua {now_tm.tm_mday}, ora {now_tm.tm_hour}.")
