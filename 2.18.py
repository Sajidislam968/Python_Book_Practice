import time
GMT = int(input("Enter the time zone offset to GMT: "))
t = time.time()
second = int(t)
current_second = second%60
minutes = second//60
current_minutes = minutes%60
hours = minutes//60
current_hours = hours%24
adjust_hour = (current_hours+GMT)%24
print(f"{adjust_hour}:{current_minutes}:{current_second}")

