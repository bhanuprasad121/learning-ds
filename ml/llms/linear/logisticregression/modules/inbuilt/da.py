from datetime import datetime
import math


today= datetime.now()
joining=datetime(2000,2,12)
total_days=(today-joining).days
print('Total days:',total_days)

year= total_days//365
remaining_days=total_days%365
month=remaining_days//30
days=remaining_days%30
print(f'your working years:{year}')
print(f'your working month:{month}')
print(f'your working days:{days}')

# print(d.strftime('today is %a %A %d-%m-%y %H:%M:%S'))


b=568.999
print(math.floor(b))
c=568.222
print(math.ceil(c))

d=256.22
print(math.sqrt(d))

