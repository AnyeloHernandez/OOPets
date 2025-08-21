MAX_HUNGER = 10
MAX_MOOD = 3 # 0 sad, 1 neutral, 2 happy, 3 very happy

class Animal:
    def __init__(self, name: str):
        self.name = name
        self.__hunger = MAX_HUNGER
        self.__mood = MAX_MOOD

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

    def feed(self):
        self.__hunger += 1 if self.__mood <= MAX_HUNGER else self.__hunger
        return self.__hunger

    def pet(self):
        self.__mood += 1 if self.__mood <= MAX_MOOD else self.__mood
        return self.__mood

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_hunger(self):
        return self.__hunger
    
    def set_hunger(self, hunger):
        self.__hunger = hunger

    def get_mood(self):
        return self.__mood
    
    def set_mood(self, new_mood):
        self.__mood = new_mood

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