from pets.animal import Animal

class Soot(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.image_folder_path = "pets/media/soot/"
        
    def speak(self):
        return "*Soot sprite noises*"
    
    def get_image_path(self):
        return self.image_folder_path + "idle.png" 