from pets import *
from gui import *
from controller import *


def main():
    dog = Dog("Buddy")
    print(dog.get_name())
    print(dog.speak())
    
    app = OOPetApp()  # Sin controlador inicialmente

    controller = LogicController(app)
    app.controller = controller
    app.initialize_ui()  # Inicializar UI después de asignar controlador

    app.mainloop()


if __name__ == "__main__":
    main()
