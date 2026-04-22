
class details:
    def __init__(self,name,salary,password):
        self.name=name
        self._salary=salary
        self.__password=password  

    def show_name(self):
        print('Name:',self.name)

    def _show_salary(self):
        print('Salary:',self._salary)

    def __show_password(self):
        print('Password:',self.__password)   

    def __show_password(self):
        masked = '*' * len(str(self.__password))
        print('Password:', masked)  

    def show_details(self):
        self.show_name()
        self._show_salary()
        self.__show_password()            
    
emp=details('thanishka',55000,12568)
emp2=details('tanvi',56822,718885)
emp.show_details()
print('^'*10)
emp2.show_details()


