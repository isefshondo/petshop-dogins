from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

def ir_menu():
    subprocess.run(["python", "__menu__.py"])
    signUpPet.quit()

def agendar():
    subprocess.run(["python", "agendamento.py"])

def success():
    subprocess.run(["python", "success.py"])

signUpPet = Tk()

signUpPet.title("Petshop Dogin's")
signUpPet.resizable(False, False)
signUpPet.configure(bg = "#FFF")

heightTaskBar = 40

widthScreen = (signUpPet.winfo_screenwidth())
heightScreen = (signUpPet.winfo_screenheight() - heightTaskBar)

width = 1130
height = 650

posx = (widthScreen/2) - (width/2)
posy = (heightScreen/2) - (height/2)

signUpPet.maxsize(width, height)
signUpPet.minsize(width, height)

signUpPet.geometry("%dx%d+%d+%d" % (width, height, posx, posy))

signUpPet.grid_columnconfigure(1, weight = 2)
signUpPet.grid_columnconfigure(2, weight = 1)
signUpPet.grid_rowconfigure(1, weight = 1)

# Necessary Measurements
width_screen = signUpPet.winfo_screenwidth()
height_screen = signUpPet.winfo_screenheight()

def goToMenu():
    subprocess.run(["python", "__init__.py"])

# Header of the Sign Up Owner Interface
mainLogoImage = PhotoImage(file = r"images\mainLogo.png")
mainLogoHolder = Label(signUpPet, image = mainLogoImage, bg = "#FFF")
mainLogoHolder.grid(column = 0, row = 0, sticky = "nw", padx = 5)

progressBarImage = PhotoImage(file = r"images\progressBar.png")
progressBarHolder = Label(signUpPet, image = progressBarImage, bg = "#FFF")
progressBarHolder.grid(column = 1, row = 0, sticky = "nsew")

goBackButton = Button(signUpPet, text = "Voltar ao menu", activebackground = "#FFF", activeforeground = "#777", bg = "#FFF", fg = "#777", font = ("Open Sans", 18, "underline"), bd = 0, command=goToMenu)
goBackButton.grid(column = 2, row = 0, sticky = "nse", padx = 5)
# End of the Sign Up's Page Header

mainElementsWrapper = Frame(signUpPet, bd = 2, bg = "#D9D9D9", relief = "flat")
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

heartIcon = PhotoImage(file = r"images\heart-icon.png")
heartIconLabel = Label(titleFrame, image = heartIcon, bg = "#FFF")
heartIconLabel.grid(column = 1, row = 0, sticky = "w")

interfaceDescription = Label(titleFrame, text = "Cadastro do Pet", bg = "#FFF", font = ("Open Sans", 35, "bold"))
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
# foto padrao antes d upload
widthPhoto = int((width_screen * 13) / 100)
heightPhoto = int((height_screen * 27) / 100)

# Image Upload Frame
pasta_inicial=""
def escolher_imagem():
    caminho_imagem = filedialog.askopenfilename(initialdir=pasta_inicial, title="Escolha uma imagem",
                                                filetypes=(("Arquivos de imagem", ".jpg;.jpeg;*.png"),
                                                           ("Todos os arquivos", ".")))
    imagem_pil = Image.open(caminho_imagem)
    largura, altura = imagem_pil.size
    if altura > 200:
        proporcao = altura / 200
        nova_altura = int(altura / proporcao)
        imagem_pil = imagem_pil.resize((170, nova_altura))
    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    lbl_imagem = Label(uploadImageFrame, image=imagem_tk)
    lbl_imagem.image = imagem_tk
    lbl_imagem.place(relx = .100, rely = .30)

defaultPhoto = Image.open("images/defaultPhotoPet.png")
defaultPhotoSize = defaultPhoto.resize((widthPhoto, heightPhoto))
defaultProfilePhoto = ImageTk.PhotoImage(defaultPhotoSize)

defaultUploadLabel = Label(uploadImageFrame, image = defaultProfilePhoto)
defaultUploadLabel.place(relx = .5, rely = .3, anchor = "center")

uploadButton = Button(uploadImageFrame, text = "Upload de Imagem", bd = 0, bg = "#D5D5D5", padx = 25, pady = 5, command=escolher_imagem)
uploadButton.place(relx = .5, rely = .55, anchor = "center")

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
    if labelText == "Código de cadastro" or labelText == "Idade":
       signUpEntry.config(state = "disabled")

displayFormElements("Código de cadastro", 0, 0, 0, 1, "we")
displayFormElements("Data de nascimento", 0, 3, 0, 4, "wn")
displayFormElements("Nome", 1, 0, 1, 1, "we")
displayFormElements("Idade", 1, 3, 1, 4, "wn")
displayFormElements("Raça", 1, 6, 1, 7, "we")
displayFormElements("Peso", 2, 6, 2, 7, "wn")

speciesLabel = Label(signUpFrame, text="Espécie:", bg="#fff").grid(column=0, row=6, sticky="w")
speciesList = ["Cachorro", "Gato"]
speciesOptions = ttk.Combobox(signUpFrame, values=speciesList)
speciesOptions.set("Selecionar")
speciesOptions.grid(column=0, row=7, sticky="we")

descriptionLabel = Label(signUpFrame, text="Descrição", bg="#fff").grid(column=0, row=9, sticky="w")
descriptionText = Entry(signUpFrame).grid(column=0, row=10, sticky="we", columnspan=2)

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

saveButton = Button(buttonWrapper, text = "Salvar", padx = 35, activebackground = "#76BCE3", bg = "#85D3FF", bd = 0, command=agendar)
saveButton.grid(column = 0, row = 0, padx = 50)

borderButton = Frame(buttonWrapper, bg = "#85D3FF", padx = 1.5, pady = 1.5)
borderButton.grid(column = 1, row = 0, padx = 50)

updateButton = Button(borderButton, text = "Alterar", padx = 30, activebackground = "#FFF", bd = 0, bg = "#FFF", command=success)
updateButton.pack()

deleteButton = Button(buttonWrapper, text = "Excluir", padx = 25, activebackground = "#C5C5C5", activeforeground = "#777", bd = 0, bg = "#D9D9D9", fg = "#777", command=success)
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

signUpPet.mainloop()