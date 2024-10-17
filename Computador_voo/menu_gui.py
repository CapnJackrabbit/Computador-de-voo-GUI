from tkinter import *
import subida, tas, dvt, acd, descida
from PIL import Image, ImageTk

janela = Tk()
janela.title('Computador de voo - v. 1.0')
janela.geometry('220x380')
janela.resizable(False,False)

frame = LabelFrame(janela, text='Bem vindo!')
frame.place(x=10, y=0, height=370, width=200)

image = Image.open('aviacao.png')
img = image.resize((144,80))
my_img = ImageTk.PhotoImage(img)
image_label = Label(janela, image=my_img)
image_label.place(x=38,y=30)

# titulo1 = Label(frame, text='MENU', font=('segoe', 18), fg='red', pady=20)
# titulo1.place(x=57, y=0)

botao1 = Button(frame, text='Calculo de subida', command=subida.janela_callback, height=1, width=15)
botao1.place(x=25, y=100)

botao2 = Button(frame, text='Calculo de ACD', command=acd.janela_callback, height=1, width=15)
botao2.place(x=25, y=150)

botao3 = Button(frame, text='Calculo de TAS', command=tas.janela_callback, height=1, width=15)
botao3.place(x=25, y=200)

botao4 = Button(frame, text='Calculo de DVT', command=dvt.janela_callback, height=1, width=15)
botao4.place(x=25, y=250)

botao5 = Button(frame, text='Calculo de descida', command=descida.janela_callback, height=1, width=15)
botao5.place(x=25, y=300)

janela.mainloop()