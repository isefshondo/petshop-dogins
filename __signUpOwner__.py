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
mainLogoHolder.grid(column = 0, row = 0, sticky = "nw")

progressBarImage = PhotoImage(file = r"images\progressBar.png")
progressBarHolder = Label(signUpOwner, image = progressBarImage, bg = "#FFF")
progressBarHolder.grid(column = 1, row = 0, sticky = "nsew")

goBackButton = Button(signUpOwner, text = "Voltar ao menu", activebackground = "#FFF", activeforeground = "#777", bg = "#FFF", fg = "#777", bd = 0)
goBackButton.grid(column = 2, row = 0, sticky = "nsew")
# End of the Sign Up's Page Header

mainElementsWrapper = Frame(signUpOwner, bd = 2, bg = "#FF0000", relief = "flat")
mainElementsWrapper.grid(column = 0, row = 1, sticky = "nsew", columnspan = 3, padx = 20, pady = 20)
mainElementsWrapper.grid_columnconfigure(0, weight = 1)
mainElementsWrapper.grid_columnconfigure(1, weight = 2)
mainElementsWrapper.grid_columnconfigure(2, weight = 1)
mainElementsWrapper.grid_rowconfigure(1, weight = 1)

interfaceDescription = Label(mainElementsWrapper, text = "Cadastro do Cliente", font = ("Open Sans", 35, "bold"))
interfaceDescription.grid(column = 0, row = 0, sticky = "we", columnspan = 3)

uploadImageFrame = Frame(mainElementsWrapper, bg = "#f0f0f0")
uploadImageFrame.grid(column = 0, row = 1, sticky = "nsew")

aTestingFrame = Frame(mainElementsWrapper, bg = "#1D5DEC")
aTestingFrame.grid(column = 1, row = 1, sticky = "nsew")

signUpFrame = Frame(aTestingFrame, bg = "#ff0000")
signUpFrame.place(relx = .5, rely = .35, anchor = "center")

signUpFrame.grid_columnconfigure(0, weight = 1)
signUpFrame.grid_columnconfigure(1, weight = 2)
signUpFrame.grid_columnconfigure(2, weight = 2)
signUpFrame.grid_columnconfigure(3, weight = 2)

accountInformation = Frame(mainElementsWrapper, bg = "#FFFF00")
accountInformation.grid(column = 2, row = 1, sticky = "nsew")

# Image Upload
widthPhoto = int((width_screen * 13) / 100)
heightPhoto = int((height_screen * 27) / 100)

defaultPhoto = Image.open("images/defaultPhoto.png")
defaultPhotoSize = defaultPhoto.resize((widthPhoto, heightPhoto), Image.ANTIALIAS)
defaultProfilePhoto = ImageTk.PhotoImage(defaultPhotoSize)

defaultUploadLabel = Label(uploadImageFrame, image = defaultProfilePhoto)
defaultUploadLabel.place(relx = .5, rely = .3, anchor = "center")

uploadButton = Button(uploadImageFrame, text = "Upload de Imagem", bd = 0, bg = "#FFF", padx = 25, pady = 5)
uploadButton.place(relx = .5, rely = .55, anchor = "center")

# Sign Up
idClient = Label(signUpFrame, text = "Código do cliente")
idClient.grid(column = 0, row = 0, sticky = "w")
idClientEntry = Entry(signUpFrame)
idClientEntry.grid(column = 0, row = 1, sticky = "we")

nCpfClient = Label(signUpFrame, text = "CPF")
nCpfClient.grid(column = 0, row = 3, sticky = "w")
nCpfClientEntry = Entry(signUpFrame)
nCpfClientEntry.grid(column = 0, row = 4, sticky = "nwn")

nTelClient = Label(signUpFrame, text = "Telefone residencial")
nTelClient.grid(column = 0, row = 6, sticky = "w")
nTelClientEntry = Entry(signUpFrame)
nTelClientEntry.grid(column = 0, row = 7, sticky = "nwn")

nCepClient = Label(signUpFrame, text = "CEP")
nCepClient.grid(column = 0, row = 9, sticky = "w")
nCepClientEntry = Entry(signUpFrame)
nCepClientEntry.grid(column= 0, row = 10, sticky = "nwn")

nHoodClient = Label(signUpFrame, text = "Bairro")
nHoodClient.grid(column = 0, row = 12, sticky = "w")
nHoodClientEntry = Entry(signUpFrame)
nHoodClientEntry.grid(column = 0, row = 13, sticky = "we")

nameClient = Label(signUpFrame, text = "Nome")
nameClient.grid(column = 1, row = 0, sticky = "w", padx = 20)
nameClientEntry = Entry(signUpFrame)
nameClientEntry.grid(column = 1, row = 1, columnspan = 2, sticky = "we", padx = 20)

birthDate = Label(signUpFrame, text = "Data de nascimento")
birthDate.grid(column = 1, row = 3, sticky = "w", padx = 20)
birthDateEntry = Entry(signUpFrame)
birthDateEntry.grid(column = 1, row = 4, sticky = "we", padx = 20)

ageClient = Label(signUpFrame, text = "Idade")
ageClient.grid(column = 2, row = 3, sticky = "w")
ageClientEntry = Entry(signUpFrame)
ageClientEntry.grid(column = 2, row = 4, sticky = "wn")

nPhoneClient = Label(signUpFrame, text = "Celular")
nPhoneClient.grid(column = 1, row = 6, sticky = "w", padx = 20)
nPhoneClientEntry = Entry(signUpFrame)
nPhoneClientEntry.grid(column = 1, row = 7, sticky = "w", padx = 20)

nAddressClient = Label(signUpFrame, text = "Endereço")
nAddressClient.grid(column = 1, row = 9, sticky = "w", padx = 20)
nAddressClientEntry = Entry(signUpFrame)
nAddressClientEntry.grid(column = 1, row = 10, sticky = "we", columnspan = 2, padx = 20)

nHouseClient = Label(signUpFrame, text = "Nº")
nHouseClient.grid(column = 3, row = 9, sticky = "w")
nHouseClientEntry = Entry(signUpFrame)
nHouseClientEntry.grid(column = 3, row = 10, sticky = "w")

cityClient = Label(signUpFrame, text = "Cidade")
cityClient.grid(column = 1, row = 12, sticky = "w", padx = 20)
cityClientEntry = Entry(signUpFrame)
cityClientEntry.grid(column = 1, row = 13, sticky = "we", padx = 20)

ufClient = Label(signUpFrame, text = "UF")
ufClient.grid(column = 2, row = 12, sticky = "w")
ufClientEntry = Entry(signUpFrame)
ufClientEntry.grid(column = 2, row = 13, sticky = "w")

# Creating Blank Spaces Between Rows
firstBlankSpace = Label(signUpFrame, text = "", bg = "#ff0000")
firstBlankSpace.grid(column = 0, row = 2, sticky = "nsew", columnspan = 4)

secondBlankSpace = Label(signUpFrame, text = "", bg = "#ff0000")
secondBlankSpace.grid(column = 0, row = 5, sticky = "nsew", columnspan = 4)

thirdBlankSpace = Label(signUpFrame, text = "", bg = "#ff0000")
thirdBlankSpace.grid(column = 0, row = 8, sticky = "nsew", columnspan = 4)

fourthBlankSpace = Label(signUpFrame, text = "", bg = "#ff0000")
fourthBlankSpace.grid(column = 0, row = 11, sticky = "nsew", columnspan = 4)

buttonWrapper = Frame(aTestingFrame, bg = "#000")
buttonWrapper.place(relx = .5, rely = .85, anchor = "s")

buttonWrapper.grid_columnconfigure(0, weight = 1)
buttonWrapper.grid_columnconfigure(1, weight = 1)
buttonWrapper.grid_columnconfigure(2, weight = 1)
buttonWrapper.grid_rowconfigure(0, weight = 1)

saveButton = Button(buttonWrapper, text = "Salvar", padx = 35)
saveButton.grid(column = 0, row = 0, padx = 50)

updateButton = Button(buttonWrapper, text = "Alterar", padx = 30)
updateButton.grid(column = 1, row = 0, padx = 50)

deleteButton = Button(buttonWrapper, text = "Excluir", padx = 25)
deleteButton.grid(column = 2, row = 0, padx = 50)

signUpOwner.mainloop()