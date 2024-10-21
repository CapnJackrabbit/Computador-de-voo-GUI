from tkinter import *
from tkinter import messagebox

def calcular_subida(entrada_elevacao,entrada_fl,entrada_temperatura,entrada_razao,entrada_velocidade,resultado):
    
    elevacao = int(entrada_elevacao.get())
    fl = int(entrada_fl.get())
    if fl < 0:
        messagebox.showerror('Erro', 'O nível de voo não pode ser negativo.')
        raise ValueError
    temperatura = float(entrada_temperatura.get())
    razao_subida = int(entrada_razao.get())
    if razao_subida <= 0:
        messagebox.showerror('Erro', 'A razão de SUBIDA não pode ser negativa.')
        raise ValueError
    velocidade = float(entrada_velocidade.get())
    if velocidade <= 0:
        messagebox.showerror('Erro', 'A velocidade aerodinâmica não pode ser negativa.')
        raise ValueError

    fl = fl * 100
    isa = 15 - (2 * fl/1000)
    isa_dev = temperatura - isa
    delta_altura = fl - elevacao                # Variação de altura
    fator = (fl + elevacao) * 0.00001           
    tempo = delta_altura / razao_subida         # Tempo
    delta_temp = (delta_altura * 2) / 1000      # Variação de temperatura
    temp_fl = temperatura - delta_temp          # Temperatura do FL
    ams = (fl + elevacao) / 2                   # Altitude média de subida
    tms = (temp_fl + temperatura) / 2           # Temperatura média de subida
    vams = velocidade + (velocidade * (ams/60000)) + (isa_dev * 0.2)             # Velocidade média aerodinâmica de subida
    toc = (tempo * vams) / 60
    
    
    resultado['text'] = str('Variação de altura: {} pés\nTempo: {:.2f} minutos\nVariação de temperatura: {:.2f} °C\nTemperatura do FL: {:.2f} °C\n Alt. media de subida: {} pés\nTemp. media de subida {:.2f} °C\nVelocidade media aerodinâmica de subida: {:.2f} nos\nDistância ate o TOC: {:.2f}'.format(delta_altura,tempo,delta_temp,temp_fl,ams,tms,vams,toc))


def janela_callback():
    janela_subida = Tk()
    janela_subida.title('Computador de voo  ->  Cálculo de subida')
    janela_subida.geometry('790x260')
    janela_subida.resizable(False,False)

    frame = LabelFrame(janela_subida, text='Cálculo de subida')
    frame.place(x=10, y=0, height=250, width=380)

    frame_res = LabelFrame(janela_subida, text='Resultado')
    frame_res.place(x=400, y=0, height=250, width=380)

    elevacao = Label(janela_subida, text='  Elevação do aeródromo (pés) ')
    elevacao.place(x=15, y=30)
    entrada_elevacao = Entry(janela_subida)
    entrada_elevacao.place(x=210, y=30)

    fl = Label(janela_subida, text='  Nível de voo (FL) ')
    fl.place(x=15, y=60)
    entrada_fl = Entry(janela_subida)
    entrada_fl.place(x=210, y=60)

    temperatura = Label(janela_subida, text='  Temperatura (°C) ')
    temperatura.place(x=15, y=90)
    entrada_temperatura = Entry(janela_subida)
    entrada_temperatura.place(x=210, y=90)

    razao = Label(janela_subida, text='  Razão de subida (pés/min) ')
    razao.place(x=15, y=120)
    entrada_razao = Entry(janela_subida)
    entrada_razao.place(x=210, y=120)

    velocidade = Label(janela_subida, text='  Velocidade (nós) ')
    velocidade.place(x=15, y=150)
    entrada_velocidade = Entry(janela_subida)
    entrada_velocidade.place(x=210, y=150)

    botao_calculo = Button(janela_subida, text='Calcular!', command= lambda: calcular_subida(entrada_elevacao,entrada_fl,entrada_temperatura,entrada_razao,entrada_velocidade,resultado))
    botao_calculo.place(x=170, y=200)

    resultado = Label(janela_subida, text='')
    resultado.place(x=420, y=40)

    janela_subida.mainloop()