from tkinter import *
from tkinter import messagebox
import math

def calcular_tas(entrada_mach,entrada_temperatura,resultado):
    mach = float(entrada_mach.get())
    if mach <= 0:
        messagebox.showerror('Erro', 'Um ou mais parametros informados sao invalidos.')
        raise ValueError
    temperatura = float(entrada_temperatura.get())
    tas = (39 * (math.sqrt(temperatura + 273))) * mach

    resultado['text'] = str('Velocidade verdadeira: {:.2f} nos'.format(tas))


def janela_callback():
    
    janela_tas = Tk()
    janela_tas.title('Computador de voo  ->  Calculo de true airspeed')
    janela_tas.geometry('430x270')
    janela_tas.resizable(False,False)

    frame = LabelFrame(janela_tas, text='Calculo de True Airspeed')
    frame.place(x=10, y=0, height=150, width=410)

    frame_res = LabelFrame(janela_tas, text='Resultado')
    frame_res.place(x=10, y=160, height=100, width=410)

    mach = Label(janela_tas, text='  Velocidade em Mach  ')
    mach.place(x=20, y=30)
    entrada_mach = Entry(janela_tas)
    entrada_mach.place(x=200, y=30)

    temperatura = Label(janela_tas, text='  Temperatura  ')
    temperatura.place(x=20, y=60)
    entrada_temperatura = Entry(janela_tas)
    entrada_temperatura.place(x=200, y=60)

    botao = Button(frame, text='Calcular!', command= lambda: calcular_tas(entrada_mach,entrada_temperatura,resultado))
    botao.place(x=230, y=80)

    resultado = Label(janela_tas, text='')
    resultado.place(x=80, y=200)

    janela_tas.mainloop()