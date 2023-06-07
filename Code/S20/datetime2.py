from datetime import datetime, timedelta

now = datetime.now()

# print(now.strftime("%a %d-%m-%Y"))

ev1 = datetime(1998, 4, 24)

print(f'I was born on {ev1.strftime("%A")}.')

delta = now - ev1
print(delta)
print(type(delta))  # obiect de tip timedelta!
print(f'Au trecut {delta.days} zile de la nasterea mea.')
print(f'Au trecut {delta.total_seconds() / 3600} ore de la nasterea mea.')
