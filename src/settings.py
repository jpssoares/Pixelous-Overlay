import customtkinter
import os
from PIL import Image


# TODO implement window refresh fucntionality
def apply_button_callback():
    print("apply")

# TODO implement restore settings fucntionality
def restore_button_callback():
    print("restore")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Settings")
        self.geometry("450x450")
        self.resizable(False, False)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../assets/settings")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Pixelous", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Window",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.text_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Text",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.text_button_event)
        self.text_button.grid(row=2, column=0, sticky="ew")

        self.character_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Characters",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.character_button_event)
        self.character_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        label_window_size = customtkinter.CTkLabel(self.home_frame,text='Window size')
        label_window_size.pack(pady=10)

        option_window_size = customtkinter.CTkOptionMenu(self.home_frame, values=["Option 1", "Option 2", "Option 42 long long long..."])
        option_window_size.pack(pady=10)

        label_bg_color = customtkinter.CTkLabel(self.home_frame, text='Background color')
        label_bg_color.pack(pady=10)

        entry_bg_color = customtkinter.CTkEntry(self.home_frame, placeholder_text="HEX Value")
        entry_bg_color.pack(pady=10)

        self.draw_bottom_buttons(self.home_frame)

        # create second frame
        self.text_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        label_font_size = customtkinter.CTkLabel(self.text_frame,text='Font size')
        label_font_size.pack(pady=10)

        option_font_size = customtkinter.CTkEntry(self.text_frame, placeholder_text="14")
        option_font_size.pack(pady=10)

        label_font_color = customtkinter.CTkLabel(self.text_frame,text='Font color')
        label_font_color.pack(pady=10)

        option_font_color = customtkinter.CTkEntry(self.text_frame, placeholder_text="HEX Value")
        option_font_color.pack(pady=10)

        self.draw_bottom_buttons(self.text_frame)

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        label_character_pack = customtkinter.CTkLabel(self.third_frame,text='Character Pack')
        label_character_pack.pack(pady=10)

        option_character_pack = customtkinter.CTkOptionMenu(self.third_frame, values=["Dinos"])
        option_character_pack.pack(pady=10)

        self.draw_bottom_buttons(self.third_frame)

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.text_button.configure(fg_color=("gray75", "gray25") if name == "text" else "transparent")
        self.character_button.configure(fg_color=("gray75", "gray25") if name == "character" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "text":
            self.text_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.text_frame.grid_forget()
        if name == "character":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def text_button_event(self):
        self.select_frame_by_name("text")

    def character_button_event(self):
        self.select_frame_by_name("character")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def draw_bottom_buttons(self, frame):
        button_1 = customtkinter.CTkButton(frame, command=apply_button_callback, text="Apply Changes")
        button_1.pack(pady=10, side='bottom')

        button_2 = customtkinter.CTkButton(frame, command=restore_button_callback, text="Restore Default")
        button_2.pack(pady=10, side='bottom')

if __name__ == "__main__":
    app = App()
    app.mainloop()

