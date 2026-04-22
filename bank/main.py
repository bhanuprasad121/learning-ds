class BankAccountKotak:
      bank='kotak'
      def __init__(self):
            pass
class savingsAccount(BankAccountKotak):
    plaAmt=30
    homeAppAmt=100
    def __init__(self):
         self.acHolderName='bhanu'
         self.__acNumber=123456789
         self.__mainBal=20000
         self.__pin=1111
         self.salary=50
         self.account_status=True
         
    def check_pin(self,pin):
        return pin == self.__pin
    def details(self):
        print(f'Account holder name is {self.acHolderName} and account number is {self.__acNumber} and your main balance is {self.__mainBal}')
    def depositeAmt(self,Damt,pin):
        if  self.check_pin(pin):
            self.__mainBal+=Damt    
            print(f'your main balance updated with {Damt} your main balance is {self.__mainBal}')
        else:
            print('invaid pin')
    def withdraw(self,wAmt,pin):
        if  self.check_pin(pin):
            if self.__mainBal < wAmt:  
                print('Insufficient balance')
            else:
                self.__mainBal-=wAmt
                print(f'you have withdrawn the sum of {wAmt} your main balance is updated to {self.__mainBal}')
        else:
             print('Invalid print')        
    def loan(self,qa,loanType):
        if loanType=='personal':
            if self.salary>=self.plaAmt:#50>=60
                # print(input('enter you personal amt: '))
                print('your personal loan is approved','50')   #need to figure it out loan system does not work good   
        else:
            housePaper=input('enter house survey number: ')
            if qa <= self.homeAppAmt:
                print('home loan approved')
            else:
                print('you have qouted more them home loan limit so loan not aproved')    
    def resume_account_status(self,ad):
        # ad=input('enter aadhar no: ''47')
        if len(ad)==12 and ad.isdigit():
            return 'debit / credit card issued'
        else:
            return 'enter vaild aadhar no'

    def card(self,ad):
        if self.account_status:
            result=self.resume_account_status(ad)
            print(result)
        else:
            self.resume_account_status(ad)
            print('your account is not active please contact bank')


sobj=savingsAccount()
sobj.details()
Damt=int(input('Enter your deposite amount:'))
pin=int(input('Enter your pin: '))
sobj.depositeAmt(Damt,pin)
wAmt=int(input('entre the amout that you want to withdraw: '))
sobj.withdraw(wAmt,pin)
loanType=input('Enter type of loan personal / home: ')
lAmt=int(input('Enter the  personal amount you need: '))
qa=int(input('enter your quote amt: '))
sobj.loan(qa,loanType)
ad=(input('enter your aadhar no:'))
sobj.resume_account_status(ad)
sobj.card(ad)









class currentAccount(BankAccountKotak):
      pass


    
