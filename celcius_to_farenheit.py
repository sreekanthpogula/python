class CelsiusToFahrenheit:
    def __get__(self, instance, owner):
        return instance._celsius * 9 / 5 + 32

    def __set__(self, instance, value):
        instance._celsius = (value - 32) * 5 / 9

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        CelsiusToFahrenheit().__set__(self, value)
    
t = Temperature(0)
print(t.celsius) # Output: 0
t.celsius = 100
print(t.celsius) # Output: 37.77777777777778



