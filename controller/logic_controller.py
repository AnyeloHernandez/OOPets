from gui import OOPetApp
from pets import *

class LogicController():
    def __init__(self, view: OOPetApp):
        self.view = view
        self.pet_collection = PetCollection()
        self.initialize_pets()

    def initialize_pets(self):
        # Add your pets here
        chiwi = Dog("Chiwis")
        piwi = Dog("Piwi")
        penguin = Penguin("Mr.P")
        honguito = Mushroom("Honguito")
        whiskers = Cat("Whiskers")
        soot = Soot("soot")
        
        self.pet_collection.add_pet(chiwi)
        self.pet_collection.add_pet(piwi)
        self.pet_collection.add_pet(penguin)
        self.pet_collection.add_pet(honguito)
        self.pet_collection.add_pet(whiskers)
        self.pet_collection.add_pet(soot)

    def handle_previous_pet(self):
        self.pet_collection.previous_pet()
        self.update_view()

    def handle_next_pet(self):
        self.pet_collection.next_pet()
        self.update_view()

    def get_current_pet_hunger(self):
        return self.get_current_pet().get_hunger()

    def get_current_pet(self):
        return self.pet_collection.get_current_pet()

    def handle_button_press(self):
        current_pet = self.pet_collection.get_current_pet()
        if current_pet:
            print(f"Interacting with {current_pet.get_name()}: {current_pet.speak()}")
            
    def handle_feed(self):
        current_pet = self.pet_collection.get_current_pet()
        if current_pet:
            current_pet.feed()
            self.update_view()
            print(f"Feeding {current_pet.get_name()}: {current_pet.speak()}")
            
    def handle_pet(self):
        current_pet = self.pet_collection.get_current_pet()
        if current_pet:
            current_pet.pet()
            self.update_view()
            print(f"Petting {current_pet.get_name()}: {current_pet.speak()}")              

    def update_view(self):
        pet = self.pet_collection.get_current_pet()
        if pet:
            self.view.update_pet_name_label(pet.get_name())
            self.view.update_pet_hunger_label(pet.get_hunger())
            self.view.update_pet_image(pet.get_image_path())
