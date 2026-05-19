#data e horário da aula: 19/05/2026 - datetime
#tempo de duração da aula: 1:30 - timedelta - intervalo de tempo

from datetime import datetime, timedelta

x = timedelta(hours=1, minutes=30)
print(x)

aula = datetime(2026, 5, 19, 14, 30)
print(aula)

print(aula + x)