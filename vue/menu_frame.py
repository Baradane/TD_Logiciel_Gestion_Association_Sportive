from tkinter import Label, Button
from vue.base_frame import BaseFrame
from vue.historique import Horaire
import tkinter as tk


class MenuFrame(BaseFrame):
    def __init__(self, root_frame):
        super().__init__(root_frame)
        self.create_widgets()

    def create_widgets(self):
        self.title = Label(self, text="Association des sports")
        self.badgeage = Button(self, text="Badgeage", width=30, command=self.call_horaire)
        self.members = Button(self, text="Members", width=30, command=self._root_frame.show_members)
        self.coaches = Button(self, text="Coaches", width=30, command=self._root_frame.show_coaches)
        self.sports = Button(self, text="Sports", width=30, command=self._root_frame.show_sports)
        self.quit = Button(self, text="QUIT", fg="red", width=30,
                           command=self.quit)
        self.title.pack(side="top")
        self.badgeage.pack()
        self.members.pack()
        self.coaches.pack()
        self.sports.pack()
        self.quit.pack(side="bottom")

    def call_horaire(self):
        window = tk.Tk()
        Horaire(window )
        window.mainloop()
