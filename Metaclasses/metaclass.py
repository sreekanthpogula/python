DemoClass = type('DemoClass', (), {})
obj = DemoClass()
print(obj)

class Demo:
    pass

Demo2 = type('Demo2', (Demo,), dict(attribute=10))
obj = Demo2()

print(obj.attribute)
print(obj.__class__)
print(obj.__class__.__bases__)
