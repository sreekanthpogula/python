# constructor is used to initialize an object

# def __init__(self):# body of the constructor
# The default constructor is a simple constructor which doesn’t accept any arguments.
class Default_constructor:
    def __init__(self):
        self.name = "Sreekanth"

    def print_name(self):
        print(self.name)


obj = Default_constructor()
obj.print_name()


# parameterized constructor: constructor with parameters is known as parameterized constructor.
class Addition:
    x = 0
    y = 0
    sum = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sum = x + y

    def dispaly(self):
        print("The x is", self.x)
        print("The y is", self.y)
        print("The sum is = ", self.sum)

    def calculate(self):
        self.sum = self.x + self.y


obj1 = Addition(10, 20)
obj1.dispaly()
obj1.calculate()
