from pets.animal import Animal

class Mushroom(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.backpack = []

    def speak(self):
        return "shroom!"

    def explore_cave(self):
        return f"{self.name} is exploring a dark cave."

    def add_to_backpack(self, item):
        self.backpack.append(item)
        return f"{item} was added to the backpack."
    
    def get_image_path(self):
        return "pets/media/honguito.png"