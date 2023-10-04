from abc import ABC


class Company(ABC):
    
    def employees(self):
        raise NotImplementedError
    
    
class Organization(Company):
    """class attributes"""
    home = 'Office'
    
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        
    def employees(self):
        print("I'm an employee")
        
    @classmethod
    def associates_home(cls, home):
        cls.home = home
        
    def org_details(self):
        self.home = "galaxy"
        return f'Name: {self.name}, Designation: {self.designation}, '\
            f'Location: {self.home}'
    
    @staticmethod
    def check_elgibility(designation):
        if designation == "software engineer":
            return 'Elgible'
        else:
            return 'Not Elgible'
 
       
R = Organization("sreekanth", "software engineer")
R.employees()
    
        

# associate1 = Organization("sreekanth", "software engineer")
# print(associate1.org_details())
# print(associate1.check_elgibility("senior software engineer"))

# associate2 = Organization("Venkatesh", "Data engineer")
# print(associate2.org_details())
# print(associate2.check_elgibility("senior software engineer"))


