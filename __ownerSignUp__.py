from tkinter import *

ownerInterface = Tk()

# Screen Configuration
ownerInterface.resizable(False, False)

ownerInterface.state("zoomed")

ownerInterface.title("Petshop Dogin's")
ownerInterface.configure(bg = "#FFF")


# Get Screen Measurements to Responsivity
taskBarHeight = 40

width_screen = ownerInterface.winfo_screenwidth()
height_screen = ownerInterface.winfo_screenheight() - taskBarHeight

# Styling Owner's Interface
logoImage = PhotoImage(file = r"assets\imgs\secondary-logo.png")
logoHolder = Label(ownerInterface, bg = "#FFF", image = logoImage)
logoHolder.place(relx = .25, rely = 0, anchor = "ne")
# logoHolder.grid(column = 0, row = 0)

progressImage = PhotoImage(file = r"assets\imgs\progress-bar\initial-progress.png")
progressHolder = Label(ownerInterface, bg = "#FFF", image = progressImage)
progressHolder.place(relx = .5, rely = .05, anchor = "center")
# progressHolder.grid(column = 1, row = 0)

goBackButton = Button(ownerInterface, text = "Voltar ao menu", bd = 0, bg = "#FFF", fg = "#777777", font = "Helvetica 10 underline", activebackground = "#FFF", activeforeground = "#777")
goBackButton.place(relx = .9, rely = .05, anchor = "nw")
# goBackButton.grid(column = 2, row = 0)

ownerInterface.mainloop()