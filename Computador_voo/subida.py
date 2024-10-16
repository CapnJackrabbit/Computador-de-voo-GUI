from tkinter import *
from tkinter import messagebox

def calcular_subida(entrada_elevacao,entrada_fl,entrada_temperatura,entrada_razao,entrada_velocidade,resultado):
    
    elevacao = int(entrada_elevacao.get())
    fl = int(entrada_fl.get())
    if fl < 0:
        messagebox.showerror('Erro', 'Um ou mais parametros informados sao invalidos.')
        raise ValueError
    temperatura = float(entrada_temperatura.get())
    razao_subida = int(entrada_razao.get())
    if razao_subida <= 0:
        messagebox.showerror('Erro', 'Um ou mais parametros informados sao invalidos.')
        raise ValueError
    velocidade = float(entrada_velocidade.get())
    if velocidade <= 0:
        messagebox.showerror('Erro', 'Um ou mais parametros informados sao invalidos.')
        raise ValueError

    fl = fl * 100
    delta_altura = fl - elevacao                # Variacao de altura
    fator = (fl + elevacao) * 0.00001           
    tempo = delta_altura / razao_subida         # Tempo
    delta_temp = (delta_altura * 2) / 1000      # Variação de temperatura
    temp_fl = temperatura - delta_temp          # Temperatura do FL
    ams = (fl + elevacao) / 2                   # Altitude média de subida
    tms = (temp_fl + temperatura) / 2           # Temperatura média de subida
    vams = velocidade * (1 + fator)             # Velocidade média aerodinâmica de subida
    toc = (tempo * vams) / 60

    resultado['text'] = str('Variacao de altura: {} pes\nTempo: {:.2f} minutos\nVariacao de temperatura: {:.2f} graus\nTemperatura do FL: {:.2f} graus\n Alt. media de subida: {} pes\nTemp. media de subida {:.2f} graus\nVelocidade media aerodinamica de subida: {:.2f} nos\nDistancia ate o TOC: {:.2f}'.format(delta_altura,tempo,delta_temp,temp_fl,ams,tms,vams,toc))

    print()
    print('Variação de altura: {} pés'.format(delta_altura))
    print('Tempo: {:.1f} minutos'.format(tempo))
    print('Variação de temperatura: {} °C'.format(delta_temp))
    print('Temperatura no FL: {:.1f} °C'.format(temp_fl))
    print('Altitude média de subida: {} pés'.format(ams))
    print('Temperatura média de subida: {:.1f} °C'.format(tms))
    print('Velocidade média aerodinâmica de subida: {:.1f} nós'.format(vams))
    print('Distância até o TOC: {:.2f} NM'.format(toc))


def janela_callback():
    janela_subida = Tk()
    janela_subida.title('Computador de voo  ->  Calculo de subida')
    janela_subida.geometry('790x260')
    janela_subida.resizable(False,False)

    frame = LabelFrame(janela_subida, text='Calculo de subida')
    frame.place(x=10, y=0, height=250, width=380)

    frame_res = LabelFrame(janela_subida, text='Resultado')
    frame_res.place(x=400, y=0, height=250, width=380)

    # titulo = Label(janela_subida, text='Calculo de subida', fg='red', font=('segoe', 15))
    # titulo.grid(column=1, row=0, pady=10)

    elevacao = Label(janela_subida, text='  Elevacao do aerodromo  ')
    elevacao.place(x=20, y=30)
    entrada_elevacao = Entry(janela_subida)
    entrada_elevacao.place(x=200, y=30)

    fl = Label(janela_subida, text='  Nivel de voo  ')
    fl.place(x=20, y=60)
    entrada_fl = Entry(janela_subida)
    entrada_fl.place(x=200, y=60)

    temperatura = Label(janela_subida, text='  Temperatura  ')
    temperatura.place(x=20, y=90)
    entrada_temperatura = Entry(janela_subida)
    entrada_temperatura.place(x=200, y=90)

    razao = Label(janela_subida, text='  Razao de subida  ')
    razao.place(x=20, y=120)
    entrada_razao = Entry(janela_subida)
    entrada_razao.place(x=200, y=120)

    velocidade = Label(janela_subida, text='  Velocidade  ')
    velocidade.place(x=20, y=150)
    entrada_velocidade = Entry(janela_subida)
    entrada_velocidade.place(x=200, y=150)

    botao_calculo = Button(janela_subida, text='Calcular!', command= lambda: calcular_subida(entrada_elevacao,entrada_fl,entrada_temperatura,entrada_razao,entrada_velocidade,resultado))
    botao_calculo.place(x=170, y=200)

    resultado = Label(janela_subida, text='')
    resultado.place(x=420, y=40)

    janela_subida.mainloop()