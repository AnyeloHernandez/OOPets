from pets import *
from gui import *

def main():
    dog = Dog("Buddy")
    print(dog.get_name())
    print(dog.speak())
    app = OOPetApp()
    app.mainloop()


if __name__ == "__main__":
    main()
