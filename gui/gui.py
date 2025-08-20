from tkinter import Tk, Button, Label, PhotoImage


GAME_TITLE = "OOPet App!"

class OOPetApp(Tk):
    def __init__(self):
        super().__init__()

        self.title(GAME_TITLE)
        self.geometry("640x512")
        self.resizable(width=False, height=False)

        self.pet_widget()
        self.navigation_button()

        self.pet_name_label()
        self.pet_hunger_label()

        self.pet_image_label()
        
    def pet_widget(self):
        petButton = Button(self, text="Pet!", command=self.handle_button_press)
        petButton.place(x=20, y=460)

    def handle_button_press(self):
        self.destroy()

    def navigation_button(self):
        navPreviousButton = Button(self, text="<", command=self.handle_nav_previous_button_press)
        navPreviousButton.place(x=540, y=460)

        navNextButton = Button(self, text=">", command=self.handle_nav_next_button_press)
        navNextButton.place(x=580, y=460)

    def handle_nav_previous_button_press(self):
        pass

    def handle_nav_next_button_press(self):
        pass

    def pet_name_label(self):
        petNameLabel = Label(self, text="Name: ")
        petNameLabel.place(x=20, y=20)

    def pet_hunger_label(self):
        petHungerLabel = Label(self, text="Hunger:\n")
        petHungerLabel.place(x=540, y=20)

    def pet_image_label(self):
        petImage = PhotoImage(file="pets/media/dog.png")
        petImageLabel = Label(self, image=petImage)
        petImageLabel.image = petImage

        width = 640
        heigh = 512
        img_width, img_heigh = petImage.width(), petImage.height()

        x = (width - img_width) // 2
        y = (heigh - img_heigh) // 2

        petImageLabel.place(x=x, y=y)