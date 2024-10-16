from tkinter import *

janela = Tk()
janela.title('Computador de voo')
janela.geometry('400x500')

image = PhotoImage(file='logo_hitss.png')
label = Label(janela, image=image)
label.pack()

mensagem = Label(janela, text='teste')
mensagem.place(x=120, y=120)

janela.mainloop()