# Define a basic interface for wearing clothes
class WearingClothes:
    def wear(self):
        pass

class RemovingClothes:
    def remove(self):
        pass
    
# Define a concrete implementation of the interface
class BasicClothes(WearingClothes):
    def wear(self):
        print("Wearing basic clothes")
        
    def remove(self):
        print("Removed basic clothes")
       
class remove_BasicClothes(RemovingClothes):
    def remove(self):
        print("Removed basic clothes")

# Define a decorator for wearing a sweater
class Sweater(WearingClothes, RemovingClothes):
    def __init__(self, clothes):
        self._clothes = clothes

    def wear(self):
        self._clothes.wear()
        print("Wearing a sweater")
        
    def remove(self):
        self._clothes.remove()
        print("Removing a sweater")

# Define a decorator for wearing a jacket
class Jacket(WearingClothes, RemovingClothes):
    def __init__(self, clothes):
        self._clothes = clothes

    def wear(self):
        self._clothes.wear()
        print("Wearing a jacket")
        
    def remove(self):
        self._clothes.remove()
        print("Removing a jacket")

# Define a decorator for wearing a raincoat
class Raincoat(WearingClothes, RemovingClothes):
    def __init__(self, clothes):
        self._clothes = clothes

    def wear(self):
        self._clothes.wear()
        print("Wearing a raincoat")
        
    def remove(self):
        self._clothes.remove()
        print("Removing a raincoat")

# Example usage
clothes = BasicClothes()
clothes = Sweater(clothes)
clothes = Jacket(clothes)
clothes = Raincoat(clothes)
clothes.wear()
clothes.remove()
