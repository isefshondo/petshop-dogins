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
loginFormFrame = Frame(loginInterface, bg = "#FFF", relief = "flat", bd = 0, width = (width / 2), height = (height + 40 / 2))
loginFormFrame.grid(column = 0, row = 0)

heartIconImage = PhotoImage(file = r"assets\imgs\heart-icon.png")
iconLabel = Label(loginFormFrame, bg = "#FFF", image = heartIconImage, compound = "center")
iconLabel.place(relx = .45, rely = .15, anchor = "n")

welcomingLabel = Label(loginFormFrame, text = "Faça seu Login", bg = "#FFF", font = (35))
welcomingLabel.place(relx = .238, rely = .15, anchor = "n")

userLabel = Label(loginFormFrame, text = "Usuário", bg = "#FFF")
userLabel.place(relx = .15, rely = .25, anchor = "n")
userTextBox = Entry(loginFormFrame, width = 50)
userTextBox.place(relx = .09, rely = .32)

passwordLabel = Label(loginFormFrame, text = "Senha", bg = "#FFF")
passwordLabel.place(relx = .138, rely = .45, anchor = "n")
passwordTextBox = Entry(loginFormFrame, width = 50)
passwordTextBox.place(relx = .09, rely = .52)

signInButton = Button(loginFormFrame, text = "Entrar", activebackground = "#76bce3", bd = 0, bg = "#85D3FF", font = (25), padx = 65, pady = 5)
signInButton.place(relx = .5, rely = .75, anchor = "center")

closeLoginInterface = Button(loginFormFrame, text = "Sair da plataforma", activebackground = "#FFF", bg = "#FFF", bd = 0, font = ("Helvetica 12 underline"), activeforeground = "#777777", fg = "#777777")
closeLoginInterface.place(relx = .5, rely = .85, anchor = "center")

# Styling Logo Frame
loginLogoFrame = Frame(loginInterface, bg = "#FFF", relief = "flat", bd = 0, width = (width / 2), height = (height + 40 / 2))
loginLogoFrame.grid(column = 1, row = 0)

logoImage = PhotoImage(file = r"assets\imgs\logo-dogins.png")
logoLabel = Label(loginLogoFrame, bg = "#FFF", image = logoImage)
logoLabel.place(relx = .5, rely = .5, anchor = "center")

loginInterface.mainloop()