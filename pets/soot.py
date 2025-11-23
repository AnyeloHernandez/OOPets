from pets.animal import Animal

class Soot(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.image_folder_path = "pets/media/soot/"
        self.action = "neutral"
        self.mood_list = ["angry", "sad", "neutral", "happy"]
        
    def speak(self):
        return "*Soot sprite noises*"
    
    def feed(self):
        self.action = "eat"
        super().feed()
        
    def pet(self):
        self.action = self.mood_list[self.get_mood()]
    
    def get_image_path(self):
        return self.image_folder_path + self.action + ".png" 