from tkinter import*
Login=Tk()

taskBarHeight = 40

#Configurações da tela
Login.title("Acesso ao Petshop Dogin's")
Login.resizable(False, False)

width_screen = Login.winfo_screenwidth()
height_screen = Login.winfo_screenheight() - taskBarHeight

width = int((width_screen * 57) / 100)
height = int((height_screen * 58) / 100)

posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

Login.maxsize(width, height)
Login.minsize(width, height)

Login.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
Login.configure(bg='#fff')

#Estilização do Login

#logo_dogins = PhotoImage(file = r"img/")
#logo_dog = Label(singUpOwner, image = logo_dogins)
#logo_dog.place(relx = .830, rely = .0, anchor = "n")

#botao voltar ao menu
btn_menu = Button(Login, text = "Voltar ao menu", bd = 0, bg = "#FFF", fg = "#777777", font = "Helvetica 10 underline", activebackground = "#FFF", activeforeground = "#777")
btn_menu.place(relx = .830, rely = .10, anchor = "n")

#titulo dos serviços
txt_titulo = Label(Login,text="Cadastro dos Serviços" ,bg = "#FFF", font=("Helvetica 13 bold"))
txt_titulo.place(relx = .450, rely = .20, anchor = "n")
#logo_coracao = PhotoImage(file = r"img/")
#coracao = Label(singUpOwner, image = logo_coracao)
#coracao.place(relx = .470, rely = .20, anchor = "n")

#campo codigo do serviço
txt_codigo = Label(Login,text="Código do Serviço" ,bg = "#FFF", font=("Helvetica 8"))
txt_codigo.place(relx = .320, rely = .30, anchor = "n")
lbl_codigo = Entry(Login)
lbl_codigo.place(relx = .340, rely = .35, anchor = "n" ,  width="120" , height="20")

#campo nome
txt_nome = Label(Login,text="Nome" ,bg = "#FFF", font=("Helvetica 8"))
txt_nome.place(relx = .465, rely = .30, anchor = "n")
lbl_nome = Entry(Login)
lbl_nome.place(relx = .550, rely = .35, anchor = "n" ,  width="160" , height="20")

#campo valor
txt_valor = Label(Login,text="Valor" ,bg = "#FFF", font=("Helvetica 8"))
txt_valor.place(relx = .280, rely = .43, anchor = "n")
lbl_valor = Entry(Login)
lbl_valor.place(relx = .320, rely = .48, anchor = "n",  width="90" , height="20")

#campo tempo de duração
txt_duracao = Label(Login,text="Tempo de duração" ,bg = "#FFF", font=("Helvetica 8"))
txt_duracao.place(relx = .480, rely = .43, anchor = "n")
lbl_duracao = Entry(Login)
lbl_duracao.place(relx = .500, rely = .48, anchor = "n",  width="120" , height="20")

#Descrição
txt_descricao = Label(Login,text="Descrição" ,bg = "#FFF", font=("Helvetica 8"))
txt_descricao.place(relx = .295, rely = .55, anchor = "n")
lbl_descricao = Entry(Login)
lbl_descricao.place(relx = .455, rely = .60, anchor = "n" ,  width="300" , height="60")

#botões de salvar alterar e excluir
btn_salvar=Button(Login,text="Salvar", bg="#85d3ff")
btn_salvar.place(relx = .330, rely = .85, anchor = "n",  width="90" , height="25")
btn_alterar = Button(Login,text="Alterar")
btn_alterar.place(relx= .480, rely=.85, anchor= "n",  width="90" , height="25")
btn_alterar = Button(Login,text="Excluir")
btn_alterar.place(relx= .630, rely=.85 , anchor= "n",  width="90" , height="25")


Login.mainloop()