from tkinter import *

loginInterface = Tk()

# Main Configuration
taskBarHeight = 40

loginInterface.resizable(False, False)

width_screen = loginInterface.winfo_screenwidth()
height_screen = loginInterface.winfo_screenheight() - taskBarHeight

width = int((width_screen * 57) / 100)
height = int((height_screen * 58) / 100)

posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

loginInterface.maxsize(width, height)
loginInterface.minsize(width, height)

loginInterface.title("Petshop Dogin's")
loginInterface.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
loginInterface.configure(bg = "#FFF")

# Styling Login Interface
formsFrame = Frame(loginInterface, bg = "#FF0000", relief = "flat", bd = 0, width = (width / 2), height = (height + 40 / 2))
formsFrame.grid(column = 0, row = 0)

welcomingLabel = Label(formsFrame, text = "Faça seu Login", font = (35))
welcomingLabel.place(relx = .238, rely = .15, anchor = "n")

userLabel = Label(formsFrame, text = "Usuário")
userLabel.place(relx = .15, rely = .25, anchor = "n")

passwordLabel = Label(formsFrame, text = "Senha")
passwordLabel.place(relx = .138, rely = .45, anchor = "n")

signInButton = Button(formsFrame, text = "Entrar", activebackground = "#e8cd00", bd = 0, bg = "#FFD600", font = (25), padx = 65, pady = 5)
signInButton.place(relx = .5, rely = .8, anchor = "center")

# Styling Logo Frame
logoFrame = Frame(loginInterface, bg = "#fff000", relief = "flat", bd = 0, width = (width / 2), height = (height + 40 / 2))
logoFrame.grid(column = 1, row = 0)

loginInterface.mainloop()