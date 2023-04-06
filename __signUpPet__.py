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

# Measurements
width_screen = signUpPet.winfo_screenwidth()
height_screen = signUpPet.winfo_screenheight()

#Header of the Sign Up Pet Interface
mainLogoImage = PhotoImage(file = r"images\mainLogo.png")
mainLogoHolder = Label(signUpPet, image = mainLogoImage, bg = "#FFF")
mainLogoHolder.grid(column = 0, row = 0, sticky = "w", padx = (5, 0))

progressBarImage = PhotoImage(file = r"images\secondProgressBar.png")
progressBarHolder = Label(signUpPet, image = progressBarImage, bg = "#FFF")
progressBarHolder.grid(column = 1, row = 0, sticky = "nsew")

goBackButton = Button(signUpPet, text = "Voltar ao menu", activebackground = "#FFF", activeforeground = "#777", bd = 0, bg = "#FFF", fg = "#777", font = ("Open Sans", 18, "underline"))
goBackButton.grid(column = 2, row = 0, sticky = "nse", padx = (0, 5))
# End of the Header

# Body of the application
elementsHolder = Frame(signUpPet, bd = 2, bg = "#D9D9D9", relief = "flat")
elementsHolder.grid(column = 0, row = 1, sticky = "nsew", columnspan = 3, padx = 20, pady = 20)

elementsHolder.grid_columnconfigure(0, weight = 1)
elementsHolder.grid_columnconfigure(1, weight = 2)
elementsHolder.grid_columnconfigure(2, weight = 1)
elementsHolder.grid_rowconfigure(1, weight = 1)

# Body elements
mainTitleHolder = Frame(elementsHolder, bg = "#FFF")
mainTitleHolder.grid(column = 0, row = 0, sticky = "nsew", columnspan = 3)

mainTitleHolder.grid_columnconfigure(0, weight = 1)
mainTitleHolder.grid_columnconfigure(1, weight = 1)
mainTitleHolder.grid_rowconfigure(0, weight = 1)

mainTitleDesc = Label(mainTitleHolder, text = "Cadastro do pet", bg = "#FFF", font = ("Open Sans", 35, "bold"))
mainTitleDesc.grid(column = 0, row = 0, sticky = "e")

mainHeartIcon = PhotoImage(file = r"assets\imgs\heart-icon.png")
mainHeartHolder = Label(mainTitleHolder, image = mainHeartIcon, bg = "#FFF")
mainHeartHolder.grid(column = 1, row = 0, sticky = "w")

# Upload Image Frame
uploadImgFrame = Frame(elementsHolder, bg = "#FFFF00")
uploadImgFrame.grid(column = 0, row = 1, sticky = "nsew")

widthPhoto = int((width_screen * 13) / 100)
heightPhoto = int((height_screen * 27) / 100)

defaultPhoto = Image.open("images/defaultPhotoPet.png")
defaultPhotoSize = defaultPhoto.resize((widthPhoto, heightPhoto))
defaultProfilePhoto = ImageTk.PhotoImage(defaultPhotoSize)
defaultUploadLabel = Label(uploadImgFrame, image = defaultProfilePhoto)
defaultUploadLabel.place(relx = .5, rely = .3, anchor = "center")

uploadButton = Button(uploadImgFrame, text = "Upload de Imagem", activebackground = "#d9d9d9", activeforeground = "#000", bg = "#eee", fg = "#000", bd = 0, padx = 25, pady = 5)
uploadButton.place(relx = .5, rely = .55, anchor = "center")

# Sign Up Frame
signUpPetFrame = Frame(elementsHolder, bg = "#993399")
signUpPetFrame.grid(column = 1, row = 1, sticky = "nsew")

signUpFrame = Frame(signUpPetFrame, bg = "#FFF")
signUpFrame.place(relx = .5, rely = .35, anchor = "center")

signUpFrame.grid_columnconfigure(0, weight = 1)
signUpFrame.grid_columnconfigure(1, weight = 1)
signUpFrame.grid_columnconfigure(2, weight = 1)

def displayFormElements(labelText, columnLabel, rowLabel, columnEntry, rowEntry, stickyEntry):
    signUpLabel = Label(signUpFrame, text = labelText, bg = "#FFF")
    if columnLabel == 1:
      signUpLabel.grid(column = columnLabel, row = rowLabel, sticky = "w", padx = 20)
    signUpLabel.grid(column = columnLabel, row = rowLabel, sticky = "w")
    signUpEntry = Entry(signUpFrame)
    if columnEntry == 1:
       signUpEntry.grid(column = columnEntry, row = rowEntry, sticky = stickyEntry, padx = 20)
    signUpEntry.grid(column = columnEntry, row = rowEntry, sticky = stickyEntry)
    if labelText == "Nome":
       signUpEntry.grid(column = columnEntry, row = rowEntry, sticky = stickyEntry, padx = 20, columnspan = 2)
    # if labelText == "Descrição":
    #    signUpText = Text(signUpFrame)
    #    signUpText.grid(column = columnEntry, row = rowEntry, sticky = stickyEntry, columnspan = 20)
    if labelText == "Código de cadastro" or labelText == "Idade":
       signUpEntry.config(state = "disabled")

displayFormElements("Código de cadastro", 0, 0, 0, 1, "wn")
displayFormElements("Data de nascimento", 0, 3, 0, 4, "wn")
displayFormElements("Nome", 1, 0, 1, 1, "we")
displayFormElements("Idade", 1, 3, 1, 4, "wn")
displayFormElements("Raça", 1, 6, 1, 7, "we")
displayFormElements("Peso", 2, 6, 2, 7, "wn")
# displayFormElements("Descrição", 0, 9, 0, 10, "we")

signUpPet.mainloop()