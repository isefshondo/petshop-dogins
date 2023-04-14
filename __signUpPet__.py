from tkinter import *
from tkinter import filedialog
from tkinter import ttk
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
elementsHolder = Frame(signUpPet, bd = 2, relief = "flat")
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

# Date Info
accountInformationHolder = Frame( bg = "#FFF")
accountInformationHolder.place(relx = .10, rely = .44)

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

# Imagem inicial
widthPhoto = 1366
heightPhoto = 768

#foto padrao antes d upload
widthPhoto = int((width_screen * 13) / 100)
heightPhoto = int((height_screen * 27) / 100)

fotoOriginal = Image.open("images/defaultPhotoPet.png")
fotoResize = fotoOriginal.resize((widthPhoto, heightPhoto))
fotoPerfil = ImageTk.PhotoImage(fotoResize)
lbl_foto_Profile = Label(bg="#FFFFFF", image=fotoPerfil)
lbl_foto_Profile.place(relx=.100, rely= .30)

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
    lbl_imagem = Label(signUpPet, image=imagem_tk)
    lbl_imagem.image = imagem_tk
    lbl_imagem.place(relx = .100, rely = .30)

uploadButton = Button(text = "Upload de Imagem", command=escolher_imagem)
uploadButton.place(relx = .120, rely = .62)

# Sign Up Frame
signUpPetFrame = Frame(elementsHolder)
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

#comboBox especies
list_especies = ["Gato", "Cachorro"]
lbl_especies = Label(signUpPet, text="Especies")
lbl_especies.place(relx=.33, rely=.27)
cb_especies = ttk.Combobox(signUpPet, values=list_especies)
cb_especies.set("Cachorro")
cb_especies.place(relx=.33, rely=.30)

#Descrição
txt_descricao = Label(signUpPet,text="Descrição" ,bg = "#FFF", font=("Helvetica 10"))
txt_descricao.place(relx = .363, rely = .59, anchor = "n")
lbl_descricao = Entry(signUpPet)
lbl_descricao.place(relx = .500, rely = .62, anchor = "n" ,  width="420" , height="70")

# displayFormElements("Descrição", 0, 9, 0, 10, "we")

signUpPet.mainloop()