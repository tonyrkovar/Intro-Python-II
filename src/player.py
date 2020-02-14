# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room='outside'):
        self.inventory = []
        self.current_room = current_room
        self.name = name
    def move(self, direction):
        movement = getattr(self.current_room, f"{direction}_to")
        if movement is None:
            print(f"That's just a wall, maybe we shouldn't go there.")
        else:
            self.current_room = movement
            print(self.current_room)
    def grab_item(self, loot_item):
        self.inventory.append(loot_item)
        self.current_room.remove_loot(loot_item)
    def drop_item(self, discard):
        for item in self.inventory:
            if item.name == discard:
                self.inventory.remove(item)
                self.current_room.add_loot(item)
            
    def get_inventory(self):
        for item in self.inventory:
            print(f"{item.name}")