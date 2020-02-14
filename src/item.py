class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Sword(Item):
    def __init__(self, name, description, damage):
        self.damage = damage
        super().__init__(name, description)


class Armor(Item):
    def __init__(self, name, description, armor):
        self.armor = armor
        super().__init__(name, description)
