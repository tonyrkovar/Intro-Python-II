# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, ):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return f"{self.name}\n\n{self.description}"
    def add_loot(self, loot_item):
        self.items.append(loot_item)
    def remove_loot(self, discard):
        for item in self.items:
            if item.name == discard:
                self.items.remove(item)
        
