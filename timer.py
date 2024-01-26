import time
from datetime import datetime

print("Таймер + Показ времени. Wrote by UkrKillent")
print("Для показа времени напишите [1]\nДля запуска таймера напишите в строку [2]")
name = input("Введи свое имя: ")
tm = str(input("Таймер либо время: "))
if tm == "1":

   current_datetime = datetime.now()
   print(current_datetime)
   print("Вот актуальное время, " + name)

if tm == "2":
   print("Через сколько минут закончиться таймер?")

   local_time = float(input())

   local_time = local_time * 60

   time.sleep(local_time)

   print(name + ", СТОП!")