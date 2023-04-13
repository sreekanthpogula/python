class AmericanSocketInterface:
    def voltage(self):
        return 110
    
    def live(self):
        return 1
    
    def neutral(self):
        return -1
    
    def  earth(self):
        return 0
    
class EuropeanSocketInterface:
    def voltage(self):
        return 500
    
    def live(self):
        return 1
    
    def neutral(self):
        return -1
    
    def  earth(self):
        return 0
    
class EuropeanPlugInterface:
    def voltage(self):
        return 220
    
    def live(self):
        return 1
    
    def neutral(self):
        return -1
    
class AmericanPlugInterface:
    def voltage(self):
        return 260
    
    def live(self):
        return 1
    
    def neutral(self):
        return -1
    
class AmericanToEuropeanAdapter(EuropeanPlugInterface):
    def __init__(self, socket):
        self.socket = socket
        
    def live(self):
        return self.socket.live()
    
    def neutral(self):
        return self.socket.neutral()
    
    def voltage(self):
        return self.socket.voltage()
    
class EuropeanToAmericanAdapter(AmericanPlugInterface):
    def __init__(self, socket):
        self.socket = socket
        
    def live(self):
        return self.socket.live()
    
    def neutral(self):
        return self.socket.neutral()
    
    def voltage(self):
        return self.socket.voltage()
    
    
class Laptop:
    def __init__(self, plug):
        self.plug = plug
        
    def charge(self):
        voltage = self.plug.voltage()
        live = self.plug.live()
        neutral = self.plug.neutral()
        
        print(f"Chargin laptop  with {voltage}V, live:{live}, neutral: {neutral}")
        
american_socket = AmericanSocketInterface()
adapter = AmericanToEuropeanAdapter(american_socket)
laptop = Laptop(adapter)
laptop.charge()

european_socket = EuropeanSocketInterface()
adapter = EuropeanToAmericanAdapter(european_socket)
laptop = Laptop(adapter)
laptop.charge()