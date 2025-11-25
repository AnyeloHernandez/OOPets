from tkinter import Tk, Button, Label, PhotoImage, Canvas

GAME_TITLE = "OOPet App!"
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 512

HEART_LINGER_TIME_MS = 1000
TICK_TIME_MS = 10000


class OOPetApp(Tk):
    def __init__(self, controller=None):
        super().__init__()

        self.controller = controller

        self.title(GAME_TITLE)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(width=False, height=False)

        # Add a Canvas
        self.canvas = Canvas(self, width=640, height=512, highlightthickness=0)
        self.canvas.place(x=0, y=0)

        self.pet_name_label = None
        self.pet_hunger_label = None
        self.pet_happiness_label = None
        self.pet_image_id = None  # Holds a reference to the pet image
        self.pet_image = None
        self.__hearts = []  # Holds each visible heart
        
        self.tick()

    def initialize_ui(self):
        self.create_feed_pet_button()
        self.create_navigation_button()
        self.create_pet_name_label()
        self.create_pet_hunger_label()
        self.create_pet_image()

    def create_feed_pet_button(self):
        petButton = Button(self, text="Feed!", command=self.controller.handle_feed)
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

    def create_pet_image(self):
        # Load the pet image
        pet_file_path = self.controller.get_current_pet().get_image_path()
        self.pet_image = PhotoImage(file=pet_file_path)

        # Window center coordinates
        x = WINDOW_WIDTH // 2
        y = WINDOW_HEIGHT // 2

        # Paint the pet image onto the canvas, and save its ID for later reference
        self.pet_image_id = self.canvas.create_image(x, y, image=self.pet_image, anchor="center")

        # Connect clicking on the image (on the canvas) to image handling
        self.canvas.tag_bind(self.pet_image_id, "<Button-1>", self.handle_image_click)

    def handle_image_click(self, event):
        self.show_heart(event.x, event.y)

        if self.controller:
            self.controller.handle_pet()
            # Handle mood change on controller
            pass

    def update_pet_name_label(self, name):
        self.pet_name_label.config(text=name)

    def update_pet_hunger_label(self, hunger):
        self.pet_hunger_label.config(text=f"{hunger}/10")

    def update_pet_image(self, image_path):
        try:
            # Load the new image
            self.pet_image = PhotoImage(file=image_path)

            # Update the canvas image
            self.canvas.itemconfig(self.pet_image_id, image=self.pet_image)

        except Exception as e:
            print(f"Error loading pet image: {e}")

    def show_heart(self, x, y):
        # Load the heart image
        heart = PhotoImage(file="pets/media/color_heart.png")

        # Paint the heart to the Canvas
        heart_id = self.canvas.create_image(x, y, image=heart, anchor="center")

        # Store the heart temporarily (prevents garbage collection)
        self.__hearts.append((heart_id, heart))

        def remove_heart():
            # Remove the heart from the canvas and from temporary storage
            self.canvas.delete(heart_id)
            self.__hearts = [(hid, h) for hid, h in self.__hearts if hid != heart_id]

        # Remove the heart after 1 second
        self.after(HEART_LINGER_TIME_MS, remove_heart)
        
    def tick(self):
        if self.controller:
            self.controller.tick()
        self.after(TICK_TIME_MS, self.tick)