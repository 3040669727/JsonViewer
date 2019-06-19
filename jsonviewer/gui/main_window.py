import tkinter as tk
from tkinter import Tk
from tkinter.messagebox import *


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        # find out which version of Tk we are using

        tk_version = master.tk.call('info', 'patchlevel')
        tk_version = tk_version.replace('.', '')
        tk_version = tk_version[0:2]
        tk_version = int(tk_version)

        menubar = tk.Menu(master)
        app_menu = tk.Menu(menubar, name='apple')
        menubar.add_cascade(menu=app_menu)

        app_menu.add_command(label='About ' + 'JsonViewer', command=self.do_about_dialog)
        app_menu.add_separator()

        if tk_version < 85:
            app_menu.add_command(label="Preferences...", command=self.do_preferences)
        else:
            # Tk 8.5 and up provides the Preferences menu item
            master.createcommand('tk::mac::ShowPreferences', self.do_preferences)

        master.config(menu=menubar)  # sets the window to use this menubar

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def do_about_dialog(self):
        tk_version = self.master.tk.call('info', 'patchlevel')
        showinfo(message='JsonViewer' + "\nThe answer to all your problems.\n\nTK version: " + tk_version)

    def do_preferences(self):
        showinfo(message="Preferences window")