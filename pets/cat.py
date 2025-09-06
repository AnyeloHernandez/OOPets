from pets.animal import Animal

class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        self.sleep_counter = 0
        self.playfulness = 5

    def speak(self):
        return "Meow! 🐱"
    
    def sleep(self):
        """Cats love to sleep! This increases their mood and reduces hunger slightly."""
        self.sleep_counter += 1
        if self.get_mood() < 3:
            self.set_mood(self.get_mood() + 1)
        if self.get_hunger() > 1:
            self.set_hunger(self.get_hunger() - 1)
        return f"{self.name} takes a nice nap... 😴 (Sleep count: {self.sleep_counter})"
    
    def play_with_yarn(self):
        """Cats love playing with yarn! This greatly improves mood."""
        self.playfulness += 1
        if self.get_mood() < 3:
            self.set_mood(min(3, self.get_mood() + 2))
        return f"{self.name} plays with a ball of yarn! 🧶 So fun! (Playfulness: {self.playfulness})"
    
    def knock_things_over(self):
        """Classic cat behavior - they love knocking things over!"""
        return f"{self.name} knocks over a glass of water... *crash* 🥛💥 Typical cat behavior!"
    
    def get_sleep_count(self):
        return self.sleep_counter
    
    def get_playfulness(self):
        return self.playfulness
