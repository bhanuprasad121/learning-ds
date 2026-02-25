from register import reg;
from login import log;


while True:
    print('1.register')
    print('2.login')

    option=input('enter your option: ')
    if option=='1':
        reg()
    if option=='2':
        log()   
        break 
        