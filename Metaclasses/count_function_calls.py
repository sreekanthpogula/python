def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    helper.__name__= func.__name__

    return helper

@call_counter
def f():
    pass

f = call_counter(f)
print(f.calls)
for _ in range(10):
    f()
    
print(f.calls)



class FuncCallCounter(type):
    """ A Metaclass which decorates all the methods of the 
        subclass using call_counter as the decorator
    """
    
    @staticmethod
    def call_counter(func):
        """ Decorator for counting the number of function 
            or method calls to the function or method func
        """
        def helper(*args, **kwargs):
            helper.calls += 1
            return func(*args, **kwargs)
        helper.calls = 0
        helper.__name__= func.__name__
    
        return helper
    
    
    def __new__(cls, clsname, superclasses, attributedict):
        """ Every method gets decorated with the decorator call_counter,
            which will do the actual call counting
        """
        for attr in attributedict:
            if callable(attributedict[attr]) and not attr.startswith("__"):
                attributedict[attr] = cls.call_counter(attributedict[attr])
        
        return type.__new__(cls, clsname, superclasses, attributedict)
    

class A(metaclass=FuncCallCounter):
    
    def foo(self):
        pass
    
    def bar(self):
        pass

if __name__ == "__main__":
    x = A()
    print(x.foo.calls, x.bar.calls)
    x.foo()
    print(x.foo.calls, x.bar.calls)
    x.foo()
    x.bar()
    print(x.foo.calls, x.bar.calls)