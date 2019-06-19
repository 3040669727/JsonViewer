import tkinter as tk
from jsonviewer.gui.main_window import Application

if __name__ == '__main__':

    root = tk.Tk()



    app = Application(master=root)
    app.mainloop()