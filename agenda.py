from tkinter import *
import subprocess
# Importação da biblioteca para edeição de imagens
from PIL import Image, ImageTk
PC = Tk()

def ir_menu():
    subprocess.run(["python", "__menu__.py"])
    PC.quit()

def agendamento():
    subprocess.run(["python", "agendamento.py"])

def owner():
    subprocess.run(["python", "__signUpOwner__.py"])

# Configurações da tela
PC.title("Pesquisa Cliente Dogin's")

PC.resizable(False, False)

width_screen = PC.winfo_screenwidth()
height_screen = PC.winfo_screenheight()

width = 870
height = 570


posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

PC.maxsize(width, height)
PC.minsize(width, height)

PC.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
PC.configure(bg='#fff')

#foto "logo"
fotoOriginal = Image.open("images/logo.png")
fotoResize = fotoOriginal.resize((160, 40))
fotoLogo = ImageTk.PhotoImage(fotoResize)
test = Label(PC, bg="#FFFFFF", image=fotoLogo).place(x=80, y=30)

# escrita "Agendamento"
lbl_agendamento = Label(PC, text="Agendamento", bg="#FFF", font=(
    "Helvetica 14 bold")).place(relx=.50, rely=.200, anchor="center")
# coracao
fotoOriginal = Image.open("images/coracao.png")
fotoResize = fotoOriginal.resize((15, 13))
fotoCoracao = ImageTk.PhotoImage(fotoResize)
coracao = Label(PC, bg="#FFF", image=fotoCoracao).place(
    relx=.59, rely=.200, anchor="center")

#caixa de texto
btn_menu = Button(PC, text="Voltar ao menu", bd=0, bg="#FFF", fg="#777777", font="Helvetica 10 underline", activebackground="#FFF", activeforeground="#777", command=ir_menu)
btn_menu.place(x=750, y=30, anchor="n")

lbl_nome = Label(PC, bg="#FFF", text="Nome do Cliente",font="Helvetica 10").place(x=200, y=180)
text_nome = Entry(PC, width=40).place(x=310, y=180)

# foto "table"
fotoOriginal = Image.open("images/table.png")
fotoResize = fotoOriginal.resize((700, 225))
fotoTable = ImageTk.PhotoImage(fotoResize)
table = Label(PC, bg="#FFF", image=fotoTable).place(x=90, y=230)

# botao "Agendar" e "Editar Cliente"
btn_agendar = Button(PC, width=15, text="Agendar", activebackground="#76bce3", bd=1, bg="#85D3FF",compound=TOP, command=agendamento).place(x=330, y=470)
btn_editar = Button(PC, width=15, text="Editar Cliente", bg="#D9D9D9", bd=1,compound=TOP, command=owner).place(x=450, y=470)

#text "Não encontrou"
lbl_voltar = Label(PC, bg="#FFF", text="Não encontrou o que procurava? Cadastre um novo cliente:",
    font="Helvetica 10").place(x=400, y=520, anchor="center")

#botao cadastrar clienete
btn_cadastrar = Button(PC, text="Cadastrar Cliente", bd=0, bg="#FFF", fg="#777777",
                  font="Helvetica 10 underline", activebackground="#FFF", activeforeground="#777", command=owner)
btn_cadastrar.place(x=625, y=508, anchor="n")

PC.mainloop()
