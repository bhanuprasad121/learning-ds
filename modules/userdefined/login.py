from register import Nuser;
from dashboard import dashboard_;
def log():
    u=input('enter you name:')
    p=input('enter your password:')
    for nuser in Nuser:
        if u==nuser['username'] and p==nuser['password']:
            print('successfully loggedin')
            dashboard_(u)
            break
