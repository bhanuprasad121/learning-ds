# Teacher class → properties: name, subject
# ContentCreator class → property: platform
# Create a child class Instructor that inherits from both classes.
# Task:
# Assign values to all properties
# Display instructor details using an object

class teacher:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
class contentCreator:
    def __init__(self,platform):
        self.platform=platform
class instructor(teacher,contentCreator):
    def __init__(self,name,subject,platform):
        teacher.__init__(self,name,subject)  
        contentCreator.__init__(self,platform)

inst=instructor('bhanu','python','youtube')
print('Name:',inst.name)
print('Subject:',inst.subject)
print('Platform:',inst.platform)        

# Camera class → property: cameraType
# MusicPlayer class → property: speakerBrand
# Create a child class SmartPhone that inherits from both.
# Task:
# Create one SmartPhone object
# Print camera type and speaker brand

class camera:
    def __init__(self,cameraType):
        self.cameraType=cameraType
class musicPlayer:
    def __init__(self,speakerBrand):
        self.speakerBrand=speakerBrand
class smartPhone(camera,musicPlayer):
    def __init__(self,cameraType,speakerBrand):
        camera.__init__(self,cameraType)
        musicPlayer.__init__(self,speakerBrand)
smt=smartPhone('dslr','sony')
print('Camera:',smt.cameraType)
print('Speaker:',smt.speakerBrand)
          
# Employee class → property: empId
# Department class → property: deptName
# Create a child class Manager inheriting from both.
# Task:
# Store employee ID and department name
# Display manager details


class employee:
    def __init__(self,empId):
        self.empId=empId
class department:
    def __init__(self,deptName):
        self.deptName=deptName
class manager(employee,department):
    def __init__(self,empId,deptName):
        employee.__init__(self,empId)
        department.__init__(self,deptName)
mana=manager(25252,'it')
print('EmpId:',mana.empId) 
print('Department:',mana.deptName)       
      