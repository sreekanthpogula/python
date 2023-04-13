from abc import ABC, abstractmethod

class ArmyComponent(ABC):
    """
    The base component class for the Army hierarchy.
    """
    @abstractmethod
    def execute_order(self, order):
        pass

class Division(ArmyComponent):
    """
    A division is a set of brigades.
    """
    def __init__(self):
        self.brigades = []
    
    def add_brigade(self, brigade):
        self.brigades.append(brigade)
    
    def execute_order(self, order):
        print(f"Executing order at Division level: {order}")
        for brigade in self.brigades:
            brigade.execute_order(order)

class Brigade(ArmyComponent):
    """
    A brigade consists of platoons.
    """
    def __init__(self):
        self.platoons = []
    
    def add_platoon(self, platoon):
        self.platoons.append(platoon)
    
    def execute_order(self, order):
        print(f"Executing order at Brigade level: {order}")
        for platoon in self.platoons:
            platoon.execute_order(order)

class Platoon(ArmyComponent):
    """
    A platoon consists of squads.
    """
    def __init__(self):
        self.squads = []
    
    def add_squad(self, squad):
        self.squads.append(squad)
    
    def execute_order(self, order):
        print(f"Executing order at Platoon level: {order}")
        for squad in self.squads:
            squad.execute_order(order)

class Squad(ArmyComponent):
    """
    A squad is a small group of real soldiers.
    """
    def __init__(self, soldiers):
        self.soldiers = soldiers
    
    def execute_order(self, order):
        print(f"Executing order at Squad level: {order}")
        for soldier in self.soldiers:
            print(f"{soldier} executing order: {order}")

# Example usage:
# Create the Army hierarchy:
division = Division()
brigade1 = Brigade()
brigade2 = Brigade()
platoon1 = Platoon()
platoon2 = Platoon()
platoon3 = Platoon()
squad1 = Squad(["Soldier1", "Soldier2"])
squad2 = Squad(["Soldier3", "Soldier4"])
squad3 = Squad(["Soldier5", "Soldier6"])
squad4 = Squad(["Soldier7", "Soldier8"])
squad5 = Squad(["Soldier9", "Soldier10"])
squad6 = Squad(["Soldier11", "Soldier12"])

# Add the components to form the hierarchy:
division.add_brigade(brigade1)
division.add_brigade(brigade2)
brigade1.add_platoon(platoon1)
brigade1.add_platoon(platoon2)
brigade2.add_platoon(platoon3)
platoon1.add_squad(squad1)
platoon1.add_squad(squad2)
platoon2.add_squad(squad3)
platoon2.add_squad(squad4)
platoon3.add_squad(squad5)
platoon3.add_squad(squad6)

# Execute an order:
division.execute_order("Attack the enemy!")
