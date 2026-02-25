class BankAccountHDFC:
    bankName="HDFC"
    def __init__(self):
        pass
    
class SavingsAccount(BankAccountHDFC):
    accountType="savings"
    personalLoanApprovingAmount=500000
    homeLoanApprovingAmount=300000
    
    def __init__(self):
        self.acountHolderName="vamsiEnduri"
        self.__accountNumber='12344321'
        self.__mainBal=50000
        self.__pin="1234"
        self.__sal=500000
        self.account_status_=True
    
    def account_status(self):
        return self.account_status_==True


    def pin_check(self,pin):
        return pin == self.__pin # return True

    def details(self): #getter function 
        print(f"{self.acountHolderName} is account holder with account number {self.__accountNumber} and having main bal {self.__mainBal}")
    def deposit(self,d_amount,pin):
        if self.pin_check(pin): # checking pin validation
            self.__mainBal+=d_amount # updating main bal
            print(f"main bal updated... with {d_amount} and now main bal {self.__mainBal}")
        else:
            print("invalid pin enter proper pin to proceed with....")    
    def withdraw(self,w,p):
        if self.pin_check(p):
            if self.__mainBal < w : # 2000 < 5000
                print("insufficient funds")
            else:
                self.__mainBal-=w 
                print(f"{w} is debited succesfully.. now main bal {self.__mainBal}") 
        else:
            print("invalid pin")           

    def check_bal(self,p):
        if self.pin_check(p):
            print(f"yr main bal is :-- {self.__mainBal}")
        else:
            print("invalid pin")    
    def apply_loan(self,qa,tL):
        if tL == "personal":
            if self.__sal >= self.personalLoanApprovingAmount:
                print("loan approved for personal purpose",qa)
        else :
            hPapers=input("enter home papers survey number") 
            if qa <= self.homeLoanApprovingAmount: # 2l < 3l
                print("home loan approved")
            else:
                print("you are quoting more than limit home loan amount so loan canceled")    
            
    def resume_account_status():
        ac=input("enter adhar card number :-- ")
        if ac.length == 12:
            return "atm/debit  card issued"            
    def apply_card(self):
        if self.account_status():
            self.resume_account_status()
        else:
            self.resume_account_status()

sObj=SavingsAccount()
sObj.details()
# d_amount=int(input("enter deposit amount ..."))
# pin=input("enter pin to proceed ....")
# sObj.deposit(d_amount,pin)
# w_amount=int(input("enter withdraw amount ..."))
# sObj.withdraw(w_amount,pin)
# # sObj.check_bal(pin)
# qA=int(input("enter auoting amount :-- "))
# tyLoan=input("type of loan personal r home")
# sObj.apply_loan(qA,tyLoan) # 200000 home
sObj.resume_account_status()
sObj.apply_card()









# class CurrentAccount(BankAccountHDFC):
#     accountType="current"