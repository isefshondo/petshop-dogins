from tkinter import *

# Importação da biblioteca para edeição de imagens
from PIL import Image, ImageTk
agendamento = Tk()

# Configurações da tela
agendamento.title("Pesquisa Cliente Dogin's")

agendamento.resizable(False, False)

width_screen = agendamento.winfo_screenwidth()
height_screen = agendamento.winfo_screenheight()

width = 870
height = 570

posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

agendamento.maxsize(width, height)
agendamento.minsize(width, height)

agendamento.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
agendamento.configure(bg='#fff')

# foto "logo" e Label para guardar a imagem Logo
fotoOriginal = Image.open("images/logo.png")
fotoResize = fotoOriginal.resize((150, 30))
fotoLogo = ImageTk.PhotoImage(fotoResize)
test = Label(agendamento, bg="#FFFFFF", image=fotoLogo).place(x=80, y=30)

# foto "barra de progresso" e Label para "barra de progresso"
fotoOriginal = Image.open("images/progresso.png")
fotoResize = fotoOriginal.resize((180, 60))
fotoProgresso = ImageTk.PhotoImage(fotoResize)
test = Label(agendamento, bg="#FFFFFF", image=fotoProgresso).place(relx=.50, rely=.100, anchor="center")

# escrita "Agendamento"
lbl_agendamento = Label(agendamento, text="Agendamento", bg="#FFF", font=(
    "Helvetica 14 bold")).place(relx=.50, rely=.200, anchor="center")
# coracao
fotoOriginal = Image.open("images/coracao.png")
fotoResize = fotoOriginal.resize((15, 13))
fotoCoracao = ImageTk.PhotoImage(fotoResize)
coracao = Label(agendamento, bg="#FFF", image=fotoCoracao).place(relx=.60, rely=.200, anchor="e")

#text "Nome do Dono " e caixa de texto "Nome do dono"
lbl_nome = Label(agendamento, bg="#FFF", text="Nome do dono",font="Helvetica 10").place(x=200, y=150)
text_nome = Entry(agendamento, width=30).place(x=200, y=180)

#text "Escolha o pet" e text "Escolha o pet" e 
lbl_pet = Label(agendamento, bg="#FFF", text="Escolha o pet",font="Helvetica 10").place(x=200, y=220)
text_pet = Entry(agendamento, width=30).place(x=200, y=250)

# text "Data" e vcaixa de texto "Data"
lbl_data = Label(agendamento, bg="#FFF", text="Data",font="Helvetica 10").place(x=200, y=300)
text_data = Entry(agendamento, width=15).place(x=200, y=330)

# text "Hora" e caixa de texto "UF"
lbl_hora = Label(agendamento, bg="#FFF", text="Hora",font="Helvetica 10").place(x=370, y=300)
text_hora = Entry(agendamento, width=10).place(x=370, y=330)

#Checkbutton's
def vacinacaoClicado():
    esp = str(vvacinacao.get())
    print("Vacimação:"+esp)

def banhoClicado():
    esp = str(vbanho.get())
    print("Banho:"+esp)

def tosaClicado():
    esp = str(vtosa.get())
    print("Tosa:"+esp)

def limpezaClicado():
    esp = str(vlimpeza.get())
    print("Tosa:"+esp)


vvacinacao = IntVar()
vbanho = IntVar()
vtosa = IntVar()
vlimpeza = IntVar()

fr_quadrado1 = Frame(agendamento, borderwidth=1, relief="groove",bg="#FFFFFF")
fr_quadrado1.place(x=470, y=230, width=200, height=100)

cb_vacinacao = Checkbutton(fr_quadrado1, text="Vacicao",variable=vacinacaoClicado,onvalue=0, offvalue="n",command=vacinacaoClicado)
cb_vacinacao.pack(side=TOP)

cb_vbanho = Checkbutton(fr_quadrado1, text="Banho",bg="#FFFFFF",variable=banhoClicado,onvalue=0, offvalue="n",command=vacinacaoClicado)
cb_vbanho.pack(side=TOP)

cb_vtosa = Checkbutton(fr_quadrado1, text="Tosa",bg="#FFFFFF",variable=tosaClicado,onvalue=0, offvalue="n",command=vacinacaoClicado)
cb_vtosa.pack(side=TOP)

cb_limpeza = Checkbutton(fr_quadrado1, bg="#FFFFFF",text="Limpeza Dentária",variable=limpezaClicado,onvalue=0, offvalue="n",command=vacinacaoClicado)
cb_limpeza.pack(side=TOP)

#botao "Salvar", "Alterar", "Excluir"
btn_salvar = Button(agendamento, width=15, text="Salvar", activebackground="#76bce3", bd=0, bg="#85D3FF",compound=TOP).place(x=250, y=450)
btn_alterar = Button(agendamento, width=15, text="Alterar Cliente", bg="#fff", bd=1,compound=TOP).place(x=380, y=450)
btn_excluir = Button(agendamento, width=15, text="Excluir Cliente", bg="#fff", bd=1,compound=TOP).place(x=510, y=450)



agendamento.mainloop()
