class Animals:
    """class attributes"""
    home = 'Forest'

    def __init__(self, name, age):
        """instance attributes"""
        self.name = name
        self.age = age

    @classmethod
    def animals_home(cls, home):
        """classmethod"""
        cls.home = home

    def instance_method(self):
        """instance method"""
        self.home = "Zoo"
        return f'Name: {self.name}, Age: {self.age}, Location: {self.home}'

    @staticmethod
    def check_age(age):
        """static method"""
        if age > 10:
            return 'Dangerous Animal'
        else:
            return 'Not a Dangerous Animal'


animal1 = Animals("Lion", 15)
print(animal1.instance_method())
print(animal1.check_age(15))

animal1 = Animals("Tiger", 10)
print(animal1.instance_method())
print(animal1.check_age(10))
