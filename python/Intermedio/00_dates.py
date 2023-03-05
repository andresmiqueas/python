## Dias

from datetime import datetime # Importo datetime del modulo datetime

now = datetime.now() #Inicializo un objeto de tipo date  

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

year_2023 = datetime(2023, 3, 15) # Para definir una fecha minimo necesito año, mes y dia

print_date(year_2023)

from datetime import time

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

diff = year_2023 - now
print(diff)


print(year_2023.time())

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)

print(end_timedelta-start_timedelta)
