from tkinter import*
from PIL import Image, ImageTk
import subprocess

def ir_menu():
    subprocess.run(["python", "__menu__.py"])
    Login.quit()

def success():
    subprocess.run(["python", "success.py"])

Login=Tk()

taskBarHeight = 40

#Configurações da tela
Login.title("Acesso ao Petshop Dogin's")
Login.resizable(False, False)

width_screen = Login.winfo_screenwidth()
height_screen = Login.winfo_screenheight() - taskBarHeight

width = 870
height = 570

posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

Login.maxsize(width, height)
Login.minsize(width, height)

Login.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
Login.configure(bg='#fff')

#Estilização do Login
logo_dogins_origin = Image.open("images/mainLogo.png")
logo_resize = logo_dogins_origin.resize((160, 40), Image.ANTIALIAS)
logoDogins = ImageTk.PhotoImage(logo_resize)
logo_dog = Label(Login, image = logoDogins , bg="#fff")
logo_dog.place(relx = .150, rely = .10, anchor = "n")

#botao voltar ao menu
btn_menu = Button(Login, text = "Voltar ao menu", bd = 0, bg = "#FFF", fg = "#777777", font = "Helvetica 16 underline", activebackground = "#FFF", activeforeground = "#777", command=ir_menu)
btn_menu.place(relx = .830, rely = .10, anchor = "n")

#titulo dos serviços
txt_titulo = Label(Login,text="Cadastro dos Serviços" ,bg = "#FFF", font=("Helvetica 20 bold"))
txt_titulo.place(relx = .450, rely = .20, anchor = "n")
logo_cora= Image.open("images/heart-icon.png")
cora = logo_cora.resize((20, 15), Image.ANTIALIAS)
logo_coracao = ImageTk.PhotoImage(cora)
coracao = Label(Login, image = logo_coracao , bg="#fff")
coracao.place(relx = .65, rely = .22, anchor = "n")

#campo codigo do serviço
txt_codigo = Label(Login,text="Código do Serviço" ,bg = "#FFF")
txt_codigo.place(relx = .270, rely = .30, anchor = "n")
lbl_codigo = Entry(Login)
lbl_codigo.place(relx = .285, rely = .34, anchor = "n" ,  width="130" , height="20")

#campo nome
txt_nome = Label(Login,text="Nome do serviço prestado" ,bg = "#FFF")
txt_nome.place(relx = .550, rely = .30, anchor = "n")
lbl_nome = Entry(Login,   width="50")
lbl_nome.place(relx = .635, rely = .34, anchor = "n")

#campo valor
txt_valor = Label(Login,text="Valor" ,bg = "#FFF")
txt_valor.place(relx = .235, rely = .40, anchor = "n")
lbl_valor = Entry(Login)
lbl_valor.place(relx = .265, rely = .44, anchor = "n",  width="90" , height="20")

#campo tempo de duração
txt_duracao = Label(Login,text="Tempo de duração" ,bg = "#FFF")
txt_duracao.place(relx = .525, rely = .40, anchor = "n")
lbl_duracao = Entry(Login)
lbl_duracao.place(relx = .530, rely = .44, anchor = "n",  width="120" , height="20")

#Descrição
txt_descricao = Label(Login,text="Descrição" ,bg = "#FFF")
txt_descricao.place(relx = .245, rely = .50, anchor = "n")
lbl_descricao = Text(Login)
lbl_descricao.place(relx = .470, rely = .54, anchor = "n" ,  width="450" , height="80")

#botões de salvar alterar e excluir
btn_salvar=Button(Login,text="Salvar", bg="#85d3ff", command=success)
btn_salvar.place(relx = .330, rely = .85, anchor = "n",  width="100" , height="25")
btn_alterar = Button(Login, text="Alterar", command=success)
btn_alterar.place(relx= .480, rely=.85, anchor= "n",  width="100" , height="25")
btn_excluir = Button(Login,text="Excluir", command=success)
btn_excluir.place(relx= .630, rely=.85 , anchor= "n",  width="100" , height="25")


Login.mainloop()