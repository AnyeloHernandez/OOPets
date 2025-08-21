from pets import *
from gui import *
from controller import *


def main():
    dog = Dog("Buddy")
    print(dog.get_name())
    print(dog.speak())
    
    app = OOPetApp()

    controller = LogicController(app)
    app.controller = controller
    app.initialize_ui()

    app.mainloop()


if __name__ == "__main__":
    main()
