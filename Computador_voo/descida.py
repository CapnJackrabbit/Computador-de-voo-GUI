from tkinter import *
from tkinter import messagebox

def calcular_descida(entrada_alt_final,entrada_alt_inicial,entrada_razao,entrada_vel_indicada,entrada_temperatura,resultado):
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

        temperatura = float(entrada_temperatura.get())
        isa = 15 - (2 * altitude_inicial/1000)
        isa_dev = temperatura - isa
        amd = (altitude_inicial + altitude_final) / 2
        delta_altura = altitude_final - altitude_inicial
        delta_temp = (delta_altura * 2) / 1000
        temp_fl = temperatura - delta_temp
        tmd = (temp_fl + temperatura) / 2
        tempo = abs(delta_altura / razao_descida)
        #fator = ((altitude_final + altitude_inicial) * 0.00001) + 1
        va = velocidade_indicada + (velocidade_indicada * (amd/60000)) + (isa_dev * 0.2)

        resultado['text'] = str('ΔH = {} pés\nTempo total {:.1f} minutos\nVelocidade aerodinâmica {:.2f} nós\nAlt. média de descida {} pés\nTemperatura média de descida {:.1f}°C'.format(delta_altura,tempo,va,amd,tmd))

    except ValueError:
        messagebox.showerror('Erro!','O valor informado é inválido')

def janela_callback():
    janela_descida = Tk()
    janela_descida.title('Computador de voo  ->  Cálculo de descida')
    janela_descida.geometry('790x260')
    janela_descida.resizable(False,False)

    frame = LabelFrame(janela_descida, text='Cálculo Descida')
    frame.place(x=10, y=0, height=250, width=380)

    frame_res = LabelFrame(janela_descida, text='Resultado')
    frame_res.place(x=400, y=0, height=250, width=380)

    alt_final = Label(janela_descida, text='  Altitude final (pés)')
    alt_final.place(x=15, y=30)
    entrada_alt_final = Entry(janela_descida)
    entrada_alt_final.place(x=210, y=30)

    alt_inicial = Label(janela_descida, text='  Altitude inicial (pés)')
    alt_inicial.place(x=15, y=60)
    entrada_alt_inicial = Entry(janela_descida)
    entrada_alt_inicial.place(x=210, y=60)

    razao = Label(janela_descida, text='  Razão de descida (pés/min)')
    razao.place(x=15, y=90)
    entrada_razao = Entry(janela_descida)
    entrada_razao.place(x=210, y=90)

    vel_indicada = Label(janela_descida, text='  Velocidade indicada (nós)')
    vel_indicada.place(x=15, y=120)
    entrada_vel_indicada = Entry(janela_descida)
    entrada_vel_indicada.place(x=210, y=120)

    temperatura = Label(janela_descida, text='  Temperatura FL atual (°C) ')
    temperatura.place(x=15, y=150)
    entrada_temperatura = Entry(janela_descida)
    entrada_temperatura.place(x=210, y=150)

    resultado = Label(janela_descida, text='')
    resultado.place(x=480, y=20)

    botao_calculo = Button(janela_descida, text='Calcular!', command= lambda: calcular_descida(entrada_alt_final,entrada_alt_inicial,entrada_razao,entrada_vel_indicada,entrada_temperatura,resultado))
    botao_calculo.place(x=170, y=200)

    janela_descida.mainloop()