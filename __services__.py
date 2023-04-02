from tkinter import *

servicesInterface = Tk()

# Main Configuration
taskBarHeight = 40

servicesInterface.resizable(False, False)

width_screen = servicesInterface.winfo_screenwidth()
height_screen = servicesInterface.winfo_screenheight() - taskBarHeight
width = int((width_screen * 87) / 100)
height = int((height_screen * 70) / 100)
posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

servicesInterface.maxsize(width, height)
servicesInterface.minsize(width, height)

servicesInterface.geometry("%dx%d+%d+%d" % (width, height, posx, posy))

# TODO: Configure font
# TODO: Grid of the page
logoLabel = Label(servicesInterface, text = "Dogin's")
logoLabel.grid(column = 0, row = 0, sticky = "w")


cardsServicesWrapper = Frame(servicesInterface, bg = "#FF0000", relief = "flat", bd = 0)
cardsServicesWrapper.place(relx = .5, rely = .5, anchor = CENTER)

welcomingLabel = Label(cardsServicesWrapper, text = "Bem-Vindo(a) Fulano")
welcomingLabel.grid(column = 0, row = 0, columnspan = 5)

cardWidth = int((width * 23) / 100)
cardHeight = int((height * 63) / 100)

firstService = Frame(cardsServicesWrapper, bg = "#000", bd = 0, cursor = "hand2", width = cardWidth, height = cardHeight)
firstService.grid(column = 1, row = 1, padx = 5, pady = 20)
secondService = Frame(cardsServicesWrapper, bg = "#FFF", bd = 0, cursor = "hand2", width = cardWidth, height = cardHeight)
secondService.grid(column = 2, row = 1, padx = 5, pady = 20)
thirdService = Frame(cardsServicesWrapper, bg = "#555", bd = 0, cursor = "hand2", width = cardWidth, height = cardHeight)
thirdService.grid(column = 3, row = 1, padx = 5, pady = 20)
fourthService = Frame(cardsServicesWrapper, bg = "#9A9A9A", bd = 0, cursor = "hand2", width = cardWidth, height = cardHeight)
fourthService.grid(column = 4, row = 1, padx = 5, pady = 20)
# TODO: Display elements
# TODO: Calculate the elements measurements

servicesInterface.mainloop()