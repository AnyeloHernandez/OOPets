from gui import OOPetApp
from pets import *

class LogicController():
    def __init__(self, view):
        self.view = view
        self.pet_collection = PetCollection()
        self.initialize_pets()

    def initialize_pets():
        chiwi = Dog("Chiwi")