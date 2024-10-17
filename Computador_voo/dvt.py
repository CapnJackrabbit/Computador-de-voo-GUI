from tkinter import *
from tkinter import messagebox


def calcular(entrada_tempo,entrada_distancia,entrada_velocidade,resultado):
    valid = True
    try:
        tempo = float(entrada_tempo.get())
        distancia = float(entrada_distancia.get())
        velocidade = float(entrada_velocidade.get())
    except ValueError:
        messagebox.showerror('Erro!', 'Formado de dado apresentado inválido')

    if ((tempo or distancia or velocidade) >= 0 or (tempo or distancia or velocidade) == None) :
        valid = True
    else:
        messagebox.showerror('Erro', 'Um ou mais parametros informados sao invalidos.')
        valid = False

    if valid == True:

        if (velocidade and tempo and distancia == 0):
            distancia = (velocidade * tempo) / 60
            resultado['text'] = str('Distância: {:.2f} NM'.format(distancia))

        elif (distancia and velocidade and tempo == 0):
            tempo = (distancia * 60) / velocidade
            resultado['text'] = str('Tempo: {:.1f} minutos'.format(tempo))

        elif (distancia and tempo and velocidade == 0):
            velocidade = (distancia * 60) / tempo
            resultado['text'] = str('Velocidade: {:.2f} nós'.format(velocidade))


def janela_callback():
    janela_subida = Tk()
    janela_subida.title('Computador de voo  ->  Calculo de distância/velocidade/tempo')
    janela_subida.geometry('790x260')
    janela_subida.resizable(False,False)

    frame = LabelFrame(janela_subida, text='Calculo de Distância/Velocidade/Tempo')
    frame.place(x=10, y=0, height=250, width=380)

    frame_res = LabelFrame(janela_subida, text='Resultado')
    frame_res.place(x=400, y=0, height=250, width=380)

    tempo = Label(janela_subida, text='  Tempo (minutos) ')
    tempo.place(x=20, y=30)
    entrada_tempo = Entry(janela_subida)
    entrada_tempo.place(x=200, y=30)

    distancia = Label(janela_subida, text='  Distancia (nm) ')
    distancia.place(x=20, y=60)
    entrada_distancia = Entry(janela_subida)
    entrada_distancia.place(x=200, y=60)

    velocidade = Label(janela_subida, text='  Velocidade (nós) ')
    velocidade.place(x=20, y=90)
    entrada_velocidade = Entry(janela_subida)
    entrada_velocidade.place(x=200, y=90)

    botao_calculo = Button(janela_subida, text='Calcular!', command= lambda: calcular(entrada_tempo,entrada_distancia,entrada_velocidade,resultado))
    botao_calculo.place(x=170, y=200)

    resultado = Label(janela_subida, text='')
    resultado.place(x=420, y=20)

    janela_subida.mainloop()