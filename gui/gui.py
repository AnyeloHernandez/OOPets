from tkinter import Tk, Button, Label, PhotoImage

GAME_TITLE = "OOPet App!"

class OOPetApp(Tk):
    def __init__(self, controller=None):
        super().__init__()

        self.controller = controller

        self.title(GAME_TITLE)
        self.geometry("640x512")
        self.resizable(width=False, height=False)

        self.pet_name_label = None
        self.pet_hunger_label = None
        self.pet_happiness_label = None
        self.pet_image_label = None
  
    def initialize_ui(self):
        self.create_feed_pet_button()
        self.create_navigation_button()
        self.create_pet_name_label()
        self.create_pet_hunger_label()
        self.create_pet_image_label()
        
    def create_feed_pet_button(self):
        petButton = Button(self, text="Pet!", command=self.controller.handle_button_press)
        petButton.place(x=20, y=460)

    def create_navigation_button(self):
        navPreviousButton = Button(self, text="<", command=self.controller.handle_previous_pet)
        navPreviousButton.place(x=540, y=460)

        navNextButton = Button(self, text=">", command=self.controller.handle_next_pet)
        navNextButton.place(x=580, y=460)


    def create_pet_name_label(self):
        petNameHolderLabel = Label(self, text="Name:")
        petNameHolderLabel.place(x=20, y=20)

        current_pet = self.controller.get_current_pet()
        current_pet_name = current_pet.get_name()

        self.pet_name_label = Label(self, text=current_pet_name)

        self.pet_name_label.place(x=20, y=40)
        

    def create_pet_hunger_label(self):
        petHungerLabel = Label(self, text="Hunger:\n")
        petHungerLabel.place(x=540, y=20)

        hunger_text=str(self.controller.get_current_pet_hunger()) + "/10"
        self.pet_hunger_label = Label(self, text=hunger_text)

        self.pet_hunger_label.place(x=540, y=40)


    def create_pet_image_label(self):
        petFilePath = self.controller.get_current_pet().get_image_path()
        petImage = PhotoImage(file=petFilePath)
        self.pet_image_label = Label(self, image=petImage)
        self.pet_image_label.image = petImage

        width = 640
        heigh = 512
        img_width, img_heigh = petImage.width(), petImage.height()

        x = (width - img_width) // 2
        y = (heigh - img_heigh) // 2

        self.pet_image_label.place(x=x, y=y)
        self.pet_image_label.bind("<Button-1>", self.handle_image_click)

    def handle_image_click(self, event):
        print("Pet image clicked!")

    def update_pet_name_label(self, name):
        self.pet_name_label.config(text=name)

    def update_pet_hunger_label(self, hunger):
        self.pet_hunger_label.config(text=f"{hunger}/10")

    def update_pet_image_label(self, image_path):
        try:
            petImage = PhotoImage(file=image_path)
            self.pet_image_label.config(image=petImage)
            self.pet_image_label.image = petImage
        except Exception as e:
            print(f"Error loading pet image: {e}")