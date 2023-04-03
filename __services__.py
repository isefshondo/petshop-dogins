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

servicesInterface.title("Petshop Dogin's")
servicesInterface.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
servicesInterface.configure(bg = "#FFF")

# Styling Services Interface
logoLabel = Label(servicesInterface, text = "Dogin's")
logoLabel.grid(column = 0, row = 0, sticky = "w")


cardsServicesWrapper = Frame(servicesInterface, bg = "#FFF", relief = "flat", bd = 0)
cardsServicesWrapper.place(relx = .5, rely = .5, anchor = CENTER)

welcomingLabel = Label(cardsServicesWrapper, text = "Bem-Vindo(a) Fulano", bg = "#FFF", font = (40))
welcomingLabel.grid(column = 0, row = 0, columnspan = 5)

cardWidth = int((width * 23) / 100)
cardHeight = int((height * 63) / 100)

firstService = Frame(cardsServicesWrapper, bg = "#ededed", bd = 0, width = cardWidth, height = cardHeight)
firstService.grid(column = 1, row = 1, padx = 5, pady = 20)
secondService = Frame(cardsServicesWrapper, bg = "#ededed", bd = 0, width = cardWidth, height = cardHeight)
secondService.grid(column = 2, row = 1, padx = 5, pady = 20)
thirdService = Frame(cardsServicesWrapper, bg = "#ededed", bd = 0, width = cardWidth, height = cardHeight)
thirdService.grid(column = 3, row = 1, padx = 5, pady = 20)
fourthService = Frame(cardsServicesWrapper, bg = "#ededed", bd = 0, width = cardWidth, height = cardHeight)
fourthService.grid(column = 4, row = 1, padx = 5, pady = 20)

# Later: Add the imageLabel parameter
def displayServicesElements(serviceCard, serviceDescription, buttonLabel):
    serviceLabel = Label(serviceCard, text = serviceDescription, bg = "#ededed", font = (25))
    serviceLabel.place(relx = .5, rely = .6, anchor = "center")
    buttonService = Button(serviceCard, text = buttonLabel, bg = "#FFD600", activebackground = "#e8cd00", bd = 0, cursor = "hand2", font = (25), padx = 50, pady = 5)
    buttonService.place(relx = .5, rely = .9, anchor = "s")

displayServicesElements(firstService, "Cadastre o cliente ou o pet aqui.", "Cadastrar")
displayServicesElements(secondService, "Agende um serviço para o pet.", "Agendar")
displayServicesElements(thirdService, "Cadastre aqui os serviços disponíveis.", "Cadastrar")
displayServicesElements(fourthService, "Edite ou exclua o cadastro do cliente.", "Editar")

servicesInterface.mainloop()