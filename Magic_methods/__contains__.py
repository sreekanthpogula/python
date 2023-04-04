# __contains__: The __contains__ method is used to check if an object is a member of a container object.
class MyList:
    def __init__(self, lst):
        self.lst = lst

    def __contains__(self, item):
        return item in self.lst
    
mylist = MyList([1, 2, 3, 4, 5])
print(8 in mylist)











