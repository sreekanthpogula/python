class Soldier:
    """Abstract class"""

    def __init__(self, soldier_type, name, weapon):
        self.name = name
        self.weapon = weapon
        self.soldier_type = soldier_type

    def __new__(cls, *args, **kwargs):
        if cls.__name__ == "Soldier":
            raise TypeError("Can't instatiate abstract class Soldier")
        return super(Soldier, cls).__new__(cls)

    def shout_war_cry(self, war_cry="For honor and glory"):
        print(f"{self.soldier_type} | {self.name} shouts: {war_cry}")

    def attack(self):
        raise NotImplementedError

    def defend(self):
        raise NotImplementedError

    def patrol(self):
        raise NotImplementedError


class Archer(Soldier):
    def __init__(self, name):
        super().__init__("Archer", "Bob", "Bow and Arrow")
        self.name = name

        def attack(self):
            print(f"{self.name} releases arrows")

        def defender(self):
            print(f"{self.name} defender with {self.weapon}")

        def patrol(self):
            print(f"{self.name} patrols with {self.weapon}")


class Sniper(Soldier):
    def __init__(self, name):
        super().__init__("Sniper", "Jack", "Snipers and rifles")
        self.name = name

        def attack(self):
            print(f"{self.name} releases bullets")

        def defender(self):
            print(f"{self.name} defender with {self.weapon}")

        def patrol(self):
            print(f"{self.name} patrols with {self.weapon}")


archer = Archer("Bob")
print(archer.attack())

soldier = Soldier("Soldier", "bob", "bob")
print(soldier.shout_war_cry())
# print(soldier.attack())
