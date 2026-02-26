class vehicle:
    def __init__(self,company):
        self.company=company
class car(vehicle):
    def __init__(self,company,model):
        super().__init__(company)
        self.model=model    
class car1(car):
    def __init__(self,company,model,version):
        super().__init__(company,model)
        self.version=version

aobj=car1('BMW','X5','2024 Edition')
print(aobj.company,aobj.model,aobj.version)


class Vehicle:
    def __init__(self, company):
        self.company = company

class Car(Vehicle):
    def __init__(self, company, model):
        super().__init__(company)
        self.model = model

class ElectricCar(Car):
    def __init__(self, company, model, battery):
        super().__init__(company, model)
        self.battery = battery

ec = ElectricCar("Tesla", "Model Y", "82 kWh")
print(ec.company, ec.model, ec.battery)



# Example 2: Person → Employee → Manager
class person:
    def __init__(self,name):
        self.name=name

class employee(person):
    def __init__(self,name,empid):
        super().__init__(name)
        self.empid=empid

class manager(employee):
    def __init__(self,name,empid,team_size):
        super().__init__(name,empid,) 
        self.team_size=team_size

mrg=manager('alice',121,'12')
print(mrg.name,mrg.empid,mrg.team_size)  

# print(super(person),person,employee)


# Example 3: Device → Computer → Laptop

class device:
    def __init__(self,type):
        self.type=type
class computer(device):
    def __init__(self,type,cpu):
        super().__init__(type)
        self.cpu=cpu
class laptop(computer):
    def __init__(self,type,cpu,laptop):
        super().__init__(type,cpu)
        self.laptop=laptop
com=laptop('electronic','i7','dell')
print(com.type,com.cpu,com.laptop)

# Create classes:
# ✔ Animal → property: type
# ✔ Dog → property: breed
# ✔ PetDog → property: owner_name
# Create 2 PetDog objects:
# ("Mammal", "Labrador", "Ravi")
# ("Mammal", "German Shepherd", "Priya")

class animal:
    def __init__(self,type):
        self.type=type
class dog(animal):
    def __init__(self,type,breed):
        super().__init__(type)
        self.breed=breed
class petDog(dog):
    def __init__(self,type,breed,owner_name):
        super().__init__(type,breed)
        self.owner_name=owner_name
p1=petDog("Mammal", "Labrador", "Ravi")
p2=petDog("Mammal", "German Shepherd", "Priya")

print('Type:' ,p1.type)
print('Breed:',p1.breed)
print('OwnerName:',p1.owner_name)
print('-'*10)

print('Type:' ,p2.type)
print('Breed:',p2.breed)
print('OwnerName:',p2.owner_name)
print('-'*10)


# Create classes:
# Book → title
# TextBook → subject
# CollegeTextBook → semester
# Create 3 CollegeTextBook objects:
# ("Physics Handbook", "Physics", 1st Semester)
# ("Programming in C", "C Language", 2nd Semester)
# ("Digital Logic", "ECE", 3rd Semester)

class Book:
    def __init__(self,title):
        self.title=title
class textBook(Book):
    def __init__(self,title,subject):
        super().__init__(title)
        self.subject=subject
class collegeTextBook(textBook):
    def __init__(self,title,subject,semester):
        super().__init__(title,subject)
        self.semester=semester

t1=collegeTextBook("Programming in C", "C Language", '2nd Semester')
t2=collegeTextBook("Digital Logic", "ECE", '3rd Semester')
t3=collegeTextBook("Digital Logic", "ECE", '3rd Semester')


print('Title:',t1.title)
print('Subject:',t1.subject)
print('Semester:',t1.semester)
print('^'*10)

print('Title:',t2.title)
print('Subject:',t2.subject)
print('Semester:',t2.semester)
print('^'*10)


print('Title:',t3.title)
print('Subject:',t3.subject)
print('Semester:',t3.semester)
print('^'*10)