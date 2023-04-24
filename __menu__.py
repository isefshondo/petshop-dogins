from tkinter import *
import subprocess

servicesInterface = Tk()

def table():
    subprocess.run(["python", "agenda.py"])

def pet():
    subprocess.run(["python", "__signUpPet__.py"])

def owner():
    subprocess.run(["python", "__signUpOwner__.py"])

def services():
    subprocess.run(["python", "_services_.py"])

def sair_tela():
    servicesInterface.destroy()
    return

# Main Configuration
taskBarHeight = 40

servicesInterface.resizable(False, False)

width_screen = servicesInterface.winfo_screenwidth()
height_screen = servicesInterface.winfo_screenheight() - taskBarHeight

width = 1130
height = 600

posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

servicesInterface.maxsize(width, height)
servicesInterface.minsize(width, height)

servicesInterface.title("Petshop Dogin's")
servicesInterface.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
servicesInterface.configure(bg = "#FFF")

# Styling Services Interface
logoImageFile = PhotoImage(file = r"assets\imgs\secondary-logo.png")
logoLabel = Label(servicesInterface, bg = "#FFF", image = logoImageFile, compound = "top")
logoLabel.grid(column = 0, row = 0, padx = 80)

cardsServicesWrapper = Frame(servicesInterface, bg = "#FFF", relief = "flat", bd = 0)
cardsServicesWrapper.place(relx = .5, rely = .55, anchor = CENTER)

welcomingLabel = Label(cardsServicesWrapper, text = "Bem-Vindo(a)", bg = "#FFF", font = ("Helvetica 20 bold"))
welcomingLabel.grid(column = 0, row = 0, columnspan = 5)

heartIconImage = PhotoImage(file = r"assets\imgs\heart-icon.png")
iconLabel = Label(cardsServicesWrapper, bg = "#FFF", image = heartIconImage, compound = "center")
iconLabel.place(relx= .65, rely = .0)

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

def displayServicesElements(serviceCard, serviceDescription, buttonLabel, pathButton):
    serviceLabel = Label(serviceCard, text = serviceDescription, bg = "#ededed")
    serviceLabel.place(relx = .5, rely = .75, anchor = "center")
    buttonService = Button(serviceCard, text = buttonLabel, bg = "#85D3FF", activebackground = "#76bce3", bd = 0, cursor = "hand2", padx = 50, pady = 5, command=pathButton)
    buttonService.place(relx = .5, rely = .95, anchor = "s")

firstServiceImage = PhotoImage(file = r"assets\imgs\sign-up-pets.png")
firstImageLabel = Label(firstService, image = firstServiceImage, compound = "top")
firstImageLabel.place(relx = .5, rely = .35, anchor = "center")

secondServiceImage = PhotoImage(file = r"assets\imgs\schedule-services.png")
secondImageLabel = Label(secondService, image = secondServiceImage, compound = "top")
secondImageLabel.place(relx = .5, rely = .35, anchor = "center")

thirdServiceImage = PhotoImage(file = r"assets\imgs\sign-up-services.png")
thirdImageLabel = Label(thirdService, image = thirdServiceImage, compound = "top")
thirdImageLabel.place(relx = .5, rely = .35, anchor = "center")

fourthServiceImage = PhotoImage(file = r"assets\imgs\edit-delete.png")
fourthImageLabel = Label(fourthService, image = fourthServiceImage, compound = "top")
fourthImageLabel.place(relx = .5, rely = .35, anchor = "center")

displayServicesElements(firstService, "Cadastre o cliente ou o pet aqui.", "Cadastrar", owner)
displayServicesElements(secondService, "Agende um serviço para o pet.", "Agendar", pet)
displayServicesElements(thirdService, "Cadastre aqui os serviços disponíveis.", "Cadastrar", services)
displayServicesElements(fourthService, "Edite ou exclua o cadastro do cliente.", "Editar", table)

servicesInterface.mainloop()