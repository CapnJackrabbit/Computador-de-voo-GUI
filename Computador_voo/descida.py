from tkinter import *
from tkinter import messagebox

def calcular_descida(entrada_alt_final,entrada_alt_inicial,entrada_razao,entrada_vel_indicada,resultado):
    try:
        altitude_final = int(entrada_alt_final.get())
        altitude_inicial = int(entrada_alt_inicial.get())
        if altitude_inicial < altitude_final:
            messagebox.showerror('Erro!', 'A altitude inicial não pode ser menor que a altitude final')
            raise ValueError
        razao_descida = int(entrada_razao.get())
        velocidade_indicada = float(entrada_vel_indicada.get())
        if velocidade_indicada <= 0:
            messagebox.showerror('Erro!','A velocidade indicada não pode ser nula ou negativa.')
            raise ValueError

        delta_altura = altitude_final - altitude_inicial
        tempo = abs(delta_altura / razao_descida)
        fator = ((altitude_final + altitude_inicial) * 0.00001) + 1
        va = velocidade_indicada * fator

        resultado['text'] = str('ΔH = {} pés\nTempo total {:.1f} minutos\nVelocidade aerodinâmica {:.2f}'.format(delta_altura,tempo,va))

    except ValueError:
        messagebox.showerror('Erro!','O valor informado é inválido')

def janela_callback():
    janela_descida = Tk()
    janela_descida.title('Computador de voo  ->  Calculo de descida')
    janela_descida.geometry('790x260')
    janela_descida.resizable(False,False)

    frame = LabelFrame(janela_descida, text='Calculo Descida')
    frame.place(x=10, y=0, height=250, width=380)

    frame_res = LabelFrame(janela_descida, text='Resultado')
    frame_res.place(x=400, y=0, height=250, width=380)

    alt_final = Label(janela_descida, text='  Altitude final ')
    alt_final.place(x=20, y=30)
    entrada_alt_final = Entry(janela_descida)
    entrada_alt_final.place(x=200, y=30)

    alt_inicial = Label(janela_descida, text='  Altitude inicial ')
    alt_inicial.place(x=20, y=60)
    entrada_alt_inicial = Entry(janela_descida)
    entrada_alt_inicial.place(x=200, y=60)

    razao = Label(janela_descida, text='  Razao de descida ')
    razao.place(x=20, y=90)
    entrada_razao = Entry(janela_descida)
    entrada_razao.place(x=200, y=90)

    vel_indicada = Label(janela_descida, text='  Velocidade indicada ')
    vel_indicada.place(x=20, y=120)
    entrada_vel_indicada = Entry(janela_descida)
    entrada_vel_indicada.place(x=200, y=120)

    resultado = Label(janela_descida, text='')
    resultado.place(x=500, y=20)

    botao_calculo = Button(janela_descida, text='Calcular!', command= lambda: calcular_descida(entrada_alt_final,entrada_alt_inicial,entrada_razao,entrada_vel_indicada,resultado))
    botao_calculo.place(x=170, y=200)

    janela_descida.mainloop()