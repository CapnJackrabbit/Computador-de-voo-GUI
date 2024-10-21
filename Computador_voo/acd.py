from tkinter import *
from tkinter import messagebox

import math

def calcular_acd(entrada_rumo,entrada_dir_vento,entrada_tas,entrada_vel_vento,resultado,resultado2,resultado3,resultado4,resultado5,resultado6):

    def calculate_relative_proas(proa):
        proa = proa % 360
        proa_90 = (proa + 90) % 360
        proa_180 = (proa + 180) % 360
        proa_270 = (proa + 270) % 360
        return proa_90, proa_180, proa_270, proa

    try:
        proa_usuario = float(entrada_rumo.get())
        if proa_usuario > 360 or proa_usuario < 0:
            messagebox.showerror('Erro!', 'O rumo deve estar entre 0 e 360 graus')
            raise ValueError
        if proa_usuario >= 0 and proa_usuario < 90:
            setor_proa = 'NE'
        elif proa_usuario > 90 and proa_usuario < 180:
            setor_proa = 'SE'
        elif proa_usuario > 180 and proa_usuario < 270:
            setor_proa = 'SO'
        elif proa_usuario == 0 or proa_usuario == 360:
            setor_proa = 'N'
        elif proa_usuario == 90:
            setor_proa = 'L'
        elif proa_usuario == 180:
            setor_proa = 'S'
        elif proa_usuario == 270:
            setor_proa = 'O'
        else:
            setor_proa = 'NO'


        vento_relativo = float(entrada_dir_vento.get())
        if vento_relativo > 360 or vento_relativo < 0:
            messagebox.showerror('Erro!', 'O vento deve estar entre 0 e 360 graus')
            raise ValueError
        if vento_relativo > 0 and vento_relativo < 90:
            setor_vento = 'NE'
        elif vento_relativo > 90 and vento_relativo < 180:
            setor_vento = 'SE'
        elif vento_relativo > 180 and vento_relativo < 270:
            setor_vento = 'SO'
        elif vento_relativo == 360 or vento_relativo == 0:
            setor_vento = 'N'
        elif vento_relativo == 90:
            setor_vento = 'L'
        elif vento_relativo == 180:
            setor_vento = 'S'
        elif vento_relativo == 270:
            setor_vento = 'O'
        else:
            setor_vento = 'NO'

        tas = float(entrada_tas.get())
        if tas < 0:
            messagebox.showerror('Erro!', 'A TAS não pode ser negativa')
            raise ValueError
        velocidade_vento = float(entrada_vel_vento.get())
        if velocidade_vento < 0:
            messagebox.showerror('Erro!', 'A velocidade do vento não pode ser negativa')
            raise ValueError

        nm_min = tas / 60

        acd = velocidade_vento / nm_min

        proa_90, proa_180, proa_270, proa = calculate_relative_proas(proa_usuario)

        resultado['text'] = str('Través direito {} graus\nTravés esquerdo {} graus\nReciproca {} graus'.format(proa_90,proa_270,proa_180))

        diferenca_vento = (proa - vento_relativo) % 360
        if diferenca_vento > 270 and proa > 270:
            diferenca_vento_real = 360 - (proa - vento_relativo)
        else:
            diferenca_vento_real = diferenca_vento
        
        diferenca_vento_reciproca = (vento_relativo - proa_180) % 360
        reciproca_real = proa_180
        if diferenca_vento < 90:
            resultado2['text'] = str('Vento de proa pela esquerda')
            tag_vento = 'hw'
        elif diferenca_vento > 90 and diferenca_vento < 180:
            reciproca_real = diferenca_vento_reciproca
            resultado2['text'] = str('Vento de cauda pela esquerda')
            tag_vento = 'tw'
        elif diferenca_vento > 180 and diferenca_vento < 270:
            reciproca_real = 360 - diferenca_vento_reciproca
            resultado2['text'] = str('Vento de cauda pela direita')
            tag_vento = 'tw'
        else:
            resultado2['text'] = str('Vento de proa pela direita')
            tag_vento = 'hw'

        resultado3['text'] = str('O ângulo de correção de deriva máximo é {:.2f} graus'.format(acd))

        if diferenca_vento <= 90 or diferenca_vento >= 270:
            acd_real = acd * math.sin(math.radians(diferenca_vento))
            componente = math.cos(math.radians(diferenca_vento))
        else:
            acd_real = acd * math.sin(math.radians(reciproca_real % 360))
            componente = math.cos(math.radians(reciproca_real))
        
        componente_real = velocidade_vento * componente

        resultado4['text'] = str('O ângulo de correção de deriva real é {:.2f} graus'.format(abs(acd_real)))

        if tag_vento == 'hw':
            velocidade_final = tas - componente_real
        elif tag_vento == 'tw':
            velocidade_final = tas + componente_real

        resultado5['text'] = str('A velocidade ajustada pela componente é {:.2f} nós'.format(velocidade_final))

        if velocidade_final > tas:
            resultado6['text'] = str('Componente de cauda')
        else:
            resultado6['text'] = str('Componente de proa')


    except ValueError:
        messagebox.showerror('Erro!', 'Um ou mais valores inseridos são inválidos.')


def janela_callback():
    janela_acd = Tk()
    janela_acd.title('Computador de voo  ->  Cálculo de angulo de correção de deriva')
    janela_acd.geometry('790x260')
    janela_acd.resizable(False,False)

    frame = LabelFrame(janela_acd, text='Cálculo de ACD')
    frame.place(x=10, y=0, height=250, width=380)

    frame_res = LabelFrame(janela_acd, text='Resultado')
    frame_res.place(x=400, y=0, height=250, width=380)

    rumo = Label(janela_acd, text='  Rumo (graus)  ')
    rumo.place(x=20, y=30)
    entrada_rumo = Entry(janela_acd)
    entrada_rumo.place(x=200, y=30)

    dir_vento = Label(janela_acd, text='  Direção do vento (graus) ')
    dir_vento.place(x=20, y=60)
    entrada_dir_vento = Entry(janela_acd)
    entrada_dir_vento.place(x=200, y=60)

    tas = Label(janela_acd, text='  TAS (nós)  ')
    tas.place(x=20, y=90)
    entrada_tas = Entry(janela_acd)
    entrada_tas.place(x=200, y=90)

    vel_vento = Label(janela_acd, text='  Velocidade do vento (nós) ')
    vel_vento.place(x=20, y=120)
    entrada_vel_vento = Entry(janela_acd)
    entrada_vel_vento.place(x=200, y=120)

    botao_calculo = Button(janela_acd, text='Calcular!', command= lambda: calcular_acd(entrada_rumo,entrada_dir_vento,entrada_tas,entrada_vel_vento,resultado,resultado2,resultado3,resultado4,resultado5,resultado6))
    botao_calculo.place(x=170, y=200)

    resultado = Label(janela_acd, text='')
    resultado.place(x=500, y=20)

    resultado2 = Label(janela_acd, text='')
    resultado2.place(x=500, y=100)

    resultado3 = Label(janela_acd, text='')
    resultado3.place(x=420, y=140)

    resultado4 = Label(janela_acd, text='')
    resultado4.place(x=420, y=160)

    resultado5 = Label(janela_acd, text='')
    resultado5.place(x=420, y=180)

    resultado6 = Label(janela_acd, text='')
    resultado6.place(x=515, y=220)

    janela_acd.mainloop()