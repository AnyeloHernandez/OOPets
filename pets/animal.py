class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

    def feed(self):
        pass

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

class PetCollection:
    def __init__(self):
        self.pets = []
        self.current_pet_index = 0

    def add_pet(self, pet):
        self.pets.append(pet)

    def get_current_pet(self):
        if self.pets:
            return self.pets[self.current_pet_index]
        return None
    
    def next_pet(self):
        pass

    def previous_pet(self):
        pass