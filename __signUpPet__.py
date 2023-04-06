from tkinter import *
from PIL import Image, ImageTk

signUpPet = Tk()

signUpPet.title("Petshop Dogin's")
signUpPet.state("zoomed")
signUpPet.resizable(False, False)
signUpPet.configure(bg = "#FFF")

signUpPet.grid_columnconfigure(0, weight = 0)
signUpPet.grid_columnconfigure(1, weight = 2)
signUpPet.grid_columnconfigure(2, weight = 1)
signUpPet.grid_rowconfigure(0, weight = 0)
signUpPet.grid_rowconfigure(1, weight = 1)