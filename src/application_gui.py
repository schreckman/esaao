import customtkinter as tk
import gettext
import os

tk.set_appearance_mode("System")
tk.set_default_color_theme("blue")

LOCALE = os.getenv('LANG', 'de')
_ = gettext.translation('messages', localedir='locales', languages=[LOCALE]).gettext


class App(tk.CTk):
    def __init__(self):
        super().__init__()
        # variables:
        self.streamerName = ""

        # configure window
        self.title("ESAAO - Sound Analyser Audio Outputer")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create tabview
        self.tabview = tk.CTkTabview(master=self)
        self.tabview.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.tabview.add(_("ESAAO"))
        self.tabview.add(_("Settings"))
        self.tabview.add(_("About"))

        # ESAAO window
        self.appearance_mode_label_esaao1 = tk.CTkLabel(self.tabview.tab(_("ESAAO")),
                                                        text=_("Current streamer name: ") + self.streamerName,
                                                        anchor="w")
        self.appearance_mode_label_esaao1.grid(row=5, column=0, padx=20, pady=(10, 0))

        self.string_input_button = tk.CTkButton(master=self.tabview.tab(_("ESAAO")),
                                                text=_("Choose a streamer"),
                                                command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))

        # Settings Window
        self.appearance_mode_label_settings1 = tk.CTkLabel(self.tabview.tab(_("Settings")),
                                                           text=_("Appearance Mode:"),
                                                           anchor="w")
        self.appearance_mode_label_settings1.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionmenu = tk.CTkOptionMenu(self.tabview.tab(_("Settings")),
                                                           values=["Light", "Dark", "System"],
                                                           command=self.change_appearance_mode_event)
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.appearance_mode_optionmenu.set("System")

    def open_input_dialog_event(self):
        dialog = tk.CTkInputDialog(text=_("write a streamers name:"), title=_("Streamer name"))
        self.streamerName = dialog.get_input()
        print("Streamer name:", self.streamerName)
        self.appearance_mode_label_esaao1.destroy()
        self.appearance_mode_label_esaao1 = tk.CTkLabel(self.tabview.tab(_("ESAAO")),
                                                        text=_("Current streamer name: ")
                                                             + self.streamerName, anchor="w")
        self.appearance_mode_label_esaao1.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.update_idletasks()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        tk.set_appearance_mode(new_appearance_mode)
