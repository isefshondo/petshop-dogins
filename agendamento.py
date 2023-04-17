from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import subprocess
agendamento = Tk()

def ir_menu():
    subprocess.run(["python", "__menu__.py"])
    agendamento.quit()

def success():
    subprocess.run(["python", "success.py"])
    agendamento.quit()

# Configurações da tela
agendamento.title("Pesquisa Cliente Dogin's")

agendamento.resizable(False, False)

width_screen = agendamento.winfo_screenwidth()
height_screen = agendamento.winfo_screenheight()

width = 870
height = 520

posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

agendamento.maxsize(width, height)
agendamento.minsize(width, height)

agendamento.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
agendamento.configure(bg='#fff')

# foto "logo" e Label para guardar a imagem Logo
fotoOriginal = Image.open("images/logo.png")
fotoResize = fotoOriginal.resize((160, 40))
fotoLogo = ImageTk.PhotoImage(fotoResize)
logo = Label(agendamento, bg="#FFFFFF", image=fotoLogo).place(x=80, y=30)

# foto "barra de progresso" e Label para "barra de progresso"
fotoOriginal = Image.open("images/progresso.png")
fotoResize = fotoOriginal.resize((180, 60))
fotoProgresso = ImageTk.PhotoImage(fotoResize)
progresso = Label(agendamento, bg="#FFFFFF", image=fotoProgresso).place(
    relx=.50, rely=.100, anchor="center")

# botao voltar ao menu
btn_menu = Button(agendamento, text="Voltar ao menu", bd=0, bg="#FFF", fg="#777777",
                  font="Helvetica 10 underline", activebackground="#FFF", activeforeground="#777", command=ir_menu)
btn_menu.place(x=750, y=30, anchor="n")

# escrita "Agendamento"
lbl_agendamento = Label(agendamento, text="Agendamento", bg="#FFF", font=(
    "Helvetica 14 bold")).place(relx=.50, rely=.200, anchor="center")
# coracao
fotoOriginal = Image.open("images/coracao.png")
fotoResize = fotoOriginal.resize((15, 13))
fotoCoracao = ImageTk.PhotoImage(fotoResize)
coracao = Label(agendamento, bg="#FFF", image=fotoCoracao).place(
    relx=.60, rely=.200, anchor="e")

# caixas de texto e de seleção
lbl_nome = Label(agendamento, bg="#FFF", text="Nome dono",
                 font="Helvetica 10").place(x=200, y=150)
text_nome = Entry(agendamento, width=30).place(x=200, y=180)

lbl_pet = Label(agendamento, bg="#FFF", text="Escolha o pet",
                font="Helvetica 10").place(x=200, y=220)
txt_especie = ttk.Combobox(
    agendamento, values=["Alfredo", "Totó"], width=30).place(x=200, y=250)

lbl_data = Label(agendamento, bg="#FFF", text="Data",
                 font="Helvetica 10").place(x=200, y=300)
text_data = Entry(agendamento, width=15).place(x=200, y=330)

lbl_hora = Label(agendamento, bg="#FFF", text="Hora",
                 font="Helvetica 10").place(x=350, y=300)
text_hora = Entry(agendamento, width=15).place(x=350, y=330)

# Checkbutton's


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

# text "Escolha um ou mais serviços"
lbl_nome = Label(agendamento, bg="#FFF", text="Escolha um ou mais serviços",
                 font="Helvetica 10").place(x=520, y=150)

fr_quadrado1 = Frame(agendamento, borderwidth=0, relief="groove", bg="#FFFFFF")
fr_quadrado1.place(x=520, y=170, width=200, height=170)

cb_vacinacao = Checkbutton(fr_quadrado1, text="Vacinação", font="Helvetica 10", bg="#FFFFFF",
                           variable=vacinacaoClicado, onvalue=0, offvalue="n", command=vacinacaoClicado)
cb_vacinacao.place(x=10, y=10)
lbl_vacinacao = Label(agendamento, bg="#FFF", text="R$ 00,00",
                      fg="#777777", font="Helvetica 9").place(x=620, y=182)

cb_vbanho = Checkbutton(fr_quadrado1, text="Banho", font="Helvetica 10", bg="#FFFFFF",
                        variable=banhoClicado, onvalue=0, offvalue="n", command=vacinacaoClicado)
cb_vbanho.place(x=10, y=40)
lbl_banho = Label(agendamento, bg="#FFF", text="R$ 00,00",
                  fg="#777777", font="Helvetica 9").place(x=600, y=212)

cb_vtosa = Checkbutton(fr_quadrado1, text="Tosa", font="Helvetica 10", bg="#FFFFFF",
                       variable=tosaClicado, onvalue=0, offvalue="n", command=vacinacaoClicado)
cb_vtosa.place(x=10, y=70)
lbl_tosa = Label(agendamento, bg="#FFF", text="R$ 00,00",
                 fg="#777777", font="Helvetica 9").place(x=590, y=242)

cb_limpeza = Checkbutton(fr_quadrado1, font="Helvetica 10", bg="#FFFFFF", text="Limpeza Dentária",
                         variable=limpezaClicado, onvalue=0, offvalue="n", command=vacinacaoClicado)
cb_limpeza.place(x=10, y=100)
lbl_limpeza = Label(agendamento, bg="#FFF", text="R$ 00,00",
                    fg="#777777", font="Helvetica 9").place(x=660, y=272)

# text "Total"
lbl_total = Label(agendamento, bg="#FFF", text="Total",
                  font="Helvetica 10").place(x=530, y=300)
lbl_total = Label(agendamento, bg="#FFF", text="R$ 00,00",
                  fg="#777777", font="Helvetica 10 underline").place(x=570, y=302)

#img calendario
fotoOriginal = Image.open("images/calendar.png")
fotoResize = fotoOriginal.resize((15, 17))
fotoData = ImageTk.PhotoImage(fotoResize)
Data = Label(agendamento,  image=fotoData).place(x=277, y=326)

#img hora
fotoOriginal = Image.open("images/hora.png")
fotoResize = fotoOriginal.resize((15, 16))
fotoHora = ImageTk.PhotoImage(fotoResize)
Hora = Label(agendamento,image=fotoHora).place(x=424, y=326)

# botao "Salvar", "Alterar", "Excluir"
btn_salvar = Button(agendamento, width=15, text="Salvar", activebackground="#76bce3",
                    bd=1, bg="#85D3FF", compound=TOP, command=success).place(x=250, y=450)
btn_excluir = Button(agendamento, width=15, text="Excluir",
                     bg="#D9D9D9", bd=1, compound=TOP, command=success).place(x=380, y=450)
btn_alterar = Button(agendamento, width=15, text="Alterar",
                     bg="#D9D9D9", bd=0, compound=TOP, command=success).place(x=510, y=450)


agendamento.mainloop()
