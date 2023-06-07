import time

event_time = "12 April 2023 16:48:53"

ev_tm = time.strptime(event_time, "%d %B %Y %H:%M:%S")

print(ev_tm)

ev1 = "20-02-2023 10:11"
ev2 = "22-02-2023 12:45"

ev1_time = time.strptime(ev1, "%d-%m-%Y %H:%M")
ev2_time = time.strptime(ev2, "%d-%m-%Y %H:%M")

delta_min = ev2_time.tm_min - ev1_time.tm_min
delta_h = (ev2_time.tm_hour - ev1_time.tm_hour) * 60
delta_d = (ev2_time.tm_mday - ev1_time.tm_mday) * 60 * 24
print(delta_min + delta_d + delta_h)
