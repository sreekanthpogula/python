class InstanceCounter(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        cls.instances[cls.__name__] = cls.instances.get(cls.__name__, 0) + 1
        return instance

class MyClass(metaclass=InstanceCounter):
    pass

class MyOtherClass(metaclass=InstanceCounter):
    pass

obj1 = MyClass()
obj2 = MyClass()
obj3 = MyOtherClass()
print(MyClass.instances)

