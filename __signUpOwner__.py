from tkinter import *
from PIL import Image, ImageTk

signUpOwner = Tk()

signUpOwner.title("Petshop Dogin's")
signUpOwner.state("zoomed")
signUpOwner.resizable(False, False)
signUpOwner.configure(bg = "#FFF")

# Necessary Measurements
width_screen = signUpOwner.winfo_screenwidth()
height_screen = signUpOwner.winfo_screenheight()

# Header of the Sign Up Owner Interface
mainLogoImage = PhotoImage(file = r"images\mainLogo.png")
mainLogoHolder = Label(signUpOwner, image = mainLogoImage, bg = "#FFF")
mainLogoHolder.grid(column = 0, row = 0, sticky = "nw")

progressBarImage = PhotoImage(file = r"images\progressBar.png")
progressBarHolder = Label(signUpOwner, image = progressBarImage, bg = "#FFF")
progressBarHolder.grid(column = 1, row = 0, sticky = "nsew")

goBackButton = Button(signUpOwner, text = "Voltar ao menu", activebackground = "#FFF", activeforeground = "#777", bg = "#FFF", fg = "#777", bd = 0)
goBackButton.grid(column = 2, row = 0, sticky = "nsew")

mainElementsWrapper = Frame(signUpOwner, bd = 2, bg = "#FF0000", relief = "flat")
mainElementsWrapper.grid(column = 0, row = 1, sticky = "nsew", columnspan = 3, padx = 20, pady = 20)

interfaceDescription = Label(mainElementsWrapper, text = "Cadastro do Cliente", font = (35))
interfaceDescription.grid(column = 0, row = 0, sticky = "we", columnspan = 3)

uploadImageFrame = Frame(mainElementsWrapper, bg = "#f0f0f0")
uploadImageFrame.grid(column = 0, row = 1, sticky = "nsew")

signUpFrame = Frame(mainElementsWrapper, bg = "#ff0000")
signUpFrame.grid(column = 1, row = 1, sticky = "nsew")

accountInformation = Frame(mainElementsWrapper, bg = "#FFFF00")
accountInformation.grid(column = 2, row = 1, sticky = "nsew")

mainElementsWrapper.grid_columnconfigure(0, weight = 1)
mainElementsWrapper.grid_columnconfigure(1, weight = 2)
mainElementsWrapper.grid_columnconfigure(2, weight = 1)
mainElementsWrapper.grid_rowconfigure(1, weight = 1)

signUpOwner.grid_columnconfigure(1, weight = 2)
signUpOwner.grid_columnconfigure(2, weight = 1)
signUpOwner.grid_rowconfigure(1, weight = 1)

# Image Upload


signUpOwner.mainloop()