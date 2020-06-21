import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime

 


class Horaire :
    def __init__(self , fenetre):
        self.window = fenetre
        self.window.geometry("250x90")
        self.window.title(' Projet GLPOO')
        self.ID_list = ["baradane" , "jennifer"]
        self.time_now =  datetime.now().strftime("%Y-%m-%d %H:%M")

        tk.Label(self.window, text="    Nom     ").grid(row=0 , column=0)
        tk.Label(self.window, text="    Horaire       ").grid(row=1 , column=0)
        
        self.horaire = tk.Entry(self.window)
        self.ID_get = ttk.Combobox(self.window, values = self.ID_list)
        
        self.ID_get.grid(row=0, column=1)
        self.horaire.grid(row=1, column=1)
        
        self.horaire.insert(0,self.time_now)
        
        
        tk.Button(self.window,text=" Insertion ",
          command=self.Insertion , fg='red').grid(row=3,column=1,sticky=tk.W,pady=4 )
   
    def Insertion(self):
        print( self.horaire.get()  , self.ID_get.get() )
        
