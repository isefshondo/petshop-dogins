from tkinter import *
from PIL import Image, ImageTk

signUpOwner = Tk()

signUpOwner.title("Petshop Dogin's")
signUpOwner.state("zoomed")
signUpOwner.resizable(False, False)
signUpOwner.configure(bg = "#FFF")

signUpOwner.grid_columnconfigure(1, weight = 2)
signUpOwner.grid_columnconfigure(2, weight = 1)
signUpOwner.grid_rowconfigure(1, weight = 1)

# Necessary Measurements
width_screen = signUpOwner.winfo_screenwidth()
height_screen = signUpOwner.winfo_screenheight()

# Header of the Sign Up Owner Interface
mainLogoImage = PhotoImage(file = r"images\mainLogo.png")
mainLogoHolder = Label(signUpOwner, image = mainLogoImage, bg = "#FFF")
mainLogoHolder.grid(column = 0, row = 0, sticky = "nw", padx = 5)

progressBarImage = PhotoImage(file = r"images\progressBar.png")
progressBarHolder = Label(signUpOwner, image = progressBarImage, bg = "#FFF")
progressBarHolder.grid(column = 1, row = 0, sticky = "nsew")

goBackButton = Button(signUpOwner, text = "Voltar ao menu", activebackground = "#FFF", activeforeground = "#777", bg = "#FFF", fg = "#777", font = ("Open Sans", 18, "underline"), bd = 0)
goBackButton.grid(column = 2, row = 0, sticky = "nse", padx = 5)
# End of the Sign Up's Page Header

mainElementsWrapper = Frame(signUpOwner, bd = 2, bg = "#D9D9D9", relief = "flat")
mainElementsWrapper.grid(column = 0, row = 1, sticky = "nsew", columnspan = 3, padx = 20, pady = 20)

mainElementsWrapper.grid_columnconfigure(0, weight = 1)
mainElementsWrapper.grid_columnconfigure(1, weight = 2)
mainElementsWrapper.grid_columnconfigure(2, weight = 1)
mainElementsWrapper.grid_rowconfigure(1, weight = 1)

titleFrame = Frame(mainElementsWrapper, bg = "#FFF")
titleFrame.grid(column = 0, row = 0, sticky = "we", columnspan = 3)

titleFrame.grid_columnconfigure(0, weight = 1)
titleFrame.grid_columnconfigure(1, weight = 1)
titleFrame.grid_rowconfigure(0, weight = 1)

heartIcon = PhotoImage(file = r"assets\imgs\heart-icon.png")
heartIconLabel = Label(titleFrame, image = heartIcon, bg = "#FFF")
heartIconLabel.grid(column = 1, row = 0, sticky = "w")

interfaceDescription = Label(titleFrame, text = "Cadastro do Cliente", bg = "#FFF", font = ("Open Sans", 35, "bold"))
interfaceDescription.grid(column = 0, row = 0, sticky = "e")

uploadImageFrame = Frame(mainElementsWrapper, bg = "#FFF")
uploadImageFrame.grid(column = 0, row = 1, sticky = "nsew")

signUpHolder = Frame(mainElementsWrapper, bg = "#FFF")
signUpHolder.grid(column = 1, row = 1, sticky = "nsew")

signUpFrame = Frame(signUpHolder, bg = "#FFF")
signUpFrame.place(relx = .5, rely = .35, anchor = "center")

signUpFrame.grid_columnconfigure(0, weight = 1)
signUpFrame.grid_columnconfigure(1, weight = 2)
signUpFrame.grid_columnconfigure(2, weight = 2)
signUpFrame.grid_columnconfigure(3, weight = 2)

accountInformation = Frame(mainElementsWrapper, bg = "#FFF")
accountInformation.grid(column = 2, row = 1, sticky = "nsew")

# Image Upload Frame
widthPhoto = int((width_screen * 13) / 100)
heightPhoto = int((height_screen * 27) / 100)

defaultPhoto = Image.open("images/defaultPhoto.png")
defaultPhotoSize = defaultPhoto.resize((widthPhoto, heightPhoto), Image.ANTIALIAS)
defaultProfilePhoto = ImageTk.PhotoImage(defaultPhotoSize)

defaultUploadLabel = Label(uploadImageFrame, image = defaultProfilePhoto)
defaultUploadLabel.place(relx = .5, rely = .3, anchor = "center")

uploadButton = Button(uploadImageFrame, text = "Upload de Imagem", bd = 0, bg = "#D5D5D5", padx = 25, pady = 5)
uploadButton.place(relx = .5, rely = .55, anchor = "center")

# Creating the Form Elements
def displayInputElements(labelText, columnLabel, rowLabel, columnEntry, rowEntry, stickyEntry):
    if columnLabel == 1 and columnEntry == 1:
        signUpLabel = Label(signUpFrame, text = labelText, bg = "#FFF")
        signUpLabel.grid(column = columnLabel, row = rowLabel, sticky = "w", padx = 20)
        if labelText == "Nome" or labelText == "Endereço":
            signUpEntry = Entry(signUpFrame)  
            signUpEntry.grid(column = columnEntry, row = rowEntry, sticky = stickyEntry, columnspan = 2, padx = 20)
        else:
            signUpEntry = Entry(signUpFrame)  
            signUpEntry.grid(column = columnEntry, row = rowEntry, sticky = stickyEntry, padx = 20)
    else:
        signUpLabel = Label(signUpFrame, text = labelText, bg = "#FFF")
        signUpLabel.grid(column = columnLabel, row = rowLabel, sticky = "w")
        signUpEntry = Entry(signUpFrame)
        signUpEntry.grid(column = columnEntry, row = rowEntry, sticky = stickyEntry)
        if labelText == "Código do cliente":
            signUpEntry.config(state = "disabled")

# Displaying the elements in the Interface
displayInputElements("Código do cliente", 0, 0, 0, 1, "we")
displayInputElements("CPF", 0, 3, 0, 4, "nwn")
displayInputElements("Telefone residencial", 0, 6, 0, 7, "nwn")
displayInputElements("CEP", 0, 9, 0, 10, "nwn")
displayInputElements("Bairro", 0, 12, 0, 13, "we")
displayInputElements("Nome", 1, 0, 1, 1, "we")
displayInputElements("Data de nascimento", 1, 3, 1, 4, "we")
displayInputElements("Idade", 2, 3, 2, 4, "wn")
displayInputElements("Celular", 1, 6, 1, 7 , "wn")
displayInputElements("Endereço", 1, 9, 1, 10, "we")
displayInputElements("Nº", 3, 9, 3, 10, "w")
displayInputElements("Cidade", 1, 12, 1, 13, "we")
displayInputElements("UF", 2, 12, 2, 13, "w")

# Creating Blank Spaces Between Rows
firstBlankSpace = Label(signUpFrame, text = "", bg = "#FFF")
firstBlankSpace.grid(column = 0, row = 2, sticky = "nsew", columnspan = 4)

secondBlankSpace = Label(signUpFrame, text = "", bg = "#FFF")
secondBlankSpace.grid(column = 0, row = 5, sticky = "nsew", columnspan = 4)

thirdBlankSpace = Label(signUpFrame, text = "", bg = "#FFF")
thirdBlankSpace.grid(column = 0, row = 8, sticky = "nsew", columnspan = 4)

fourthBlankSpace = Label(signUpFrame, text = "", bg = "#FFF")
fourthBlankSpace.grid(column = 0, row = 11, sticky = "nsew", columnspan = 4)
# End of Creating Blank Spaces Between Rows

buttonWrapper = Frame(signUpHolder, bg = "#FFF")
buttonWrapper.place(relx = .5, rely = .85, anchor = "s")

buttonWrapper.grid_columnconfigure(0, weight = 1)
buttonWrapper.grid_columnconfigure(1, weight = 1)
buttonWrapper.grid_columnconfigure(2, weight = 1)
buttonWrapper.grid_rowconfigure(0, weight = 1)

saveButton = Button(buttonWrapper, text = "Salvar", padx = 35, activebackground = "#76BCE3", bg = "#85D3FF", bd = 0)
saveButton.grid(column = 0, row = 0, padx = 50)

borderButton = Frame(buttonWrapper, bg = "#85D3FF", padx = 1.5, pady = 1.5)
borderButton.grid(column = 1, row = 0, padx = 50)

updateButton = Button(borderButton, text = "Alterar", padx = 30, activebackground = "#FFF", bd = 0, bg = "#FFF")
updateButton.pack()

deleteButton = Button(buttonWrapper, text = "Excluir", padx = 25, activebackground = "#C5C5C5", activeforeground = "#777", bd = 0, bg = "#D9D9D9", fg = "#777")
deleteButton.grid(column = 2, row = 0, padx = 50)

# Account Info
accountInformationHolder = Frame(accountInformation, bg = "#FFF")
accountInformationHolder.place(relx = .5, rely = .18, anchor = "center")

accountInformationHolder.grid_columnconfigure(0, weight = 1)
accountInformationHolder.grid_rowconfigure(2, weight = 1)

updateDate = Label(accountInformationHolder, text = "Data de atualização", bg = "#FFF")
updateDate.grid(column = 0, row = 0, sticky = "w")
updatDateEntry = Entry(accountInformationHolder)
updatDateEntry.config(state = "disabled")
updatDateEntry.grid(column = 0, row = 1, sticky = "we")

updateBlankSpace = Frame(accountInformationHolder, bg = "#FFF")
updateBlankSpace.grid(column = 0, row = 2, sticky = "nsew")

signUpDate = Label(accountInformationHolder, text = "Data de cadastro", bg = "#FFF")
signUpDate.grid(column = 0, row = 3, sticky = "w")
signUpDateEntry = Entry(accountInformationHolder)
signUpDateEntry.config(state = "disabled")
signUpDateEntry.grid(column = 0, row = 4, sticky = "we")

signUpOwner.mainloop()