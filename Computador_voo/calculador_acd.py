def calcular_acd():

    import math

    def calculate_relative_proas(proa):
        proa = proa % 360
        proa_90 = (proa + 90) % 360
        proa_180 = (proa + 180) % 360
        proa_270 = (proa + 270) % 360
        return proa_90, proa_180, proa_270, proa

    while True:
        try:
            print('_____________________________')
            proa_usuario = float(input("Entre com o rumo: "))
            if proa_usuario > 360 or proa_usuario < 0:
                print('O rumo deve estar entre 0 e 360 graus.')
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


            vento_relativo = float(input('Entre com o vento: '))
            if vento_relativo > 360 or vento_relativo < 0:
                print('O valor deve estar entre 0 e 360 graus.')
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

            tas = float(input('Informe a TAS: '))
            if tas < 0:
                print('A True Air Speed não pode ter um valor negativo.')
                raise ValueError
            velocidade_vento = float(input('Informe a velocidade do vento: '))
            if velocidade_vento < 0:
                print('A velocidade do vento não pode ter um valor negativo.')
                raise ValueError

            nm_min = tas / 60

            acd = velocidade_vento / nm_min

            proa_90, proa_180, proa_270, proa = calculate_relative_proas(proa_usuario)
            print()
            print(f"Través direito: {proa_90} graus")
            print(f"Recíproca: {proa_180} graus")
            print(f"Través esquerdo: {proa_270} graus")

            diferenca_vento = (proa - vento_relativo) % 360
            if diferenca_vento > 270 and proa > 270:
                diferenca_vento_real = 360 - (proa - vento_relativo)
            else:
                diferenca_vento_real = diferenca_vento
            
            diferenca_vento_reciproca = (vento_relativo - proa_180) % 360
            reciproca_real = proa_180
            
            #print('Vento soprando do setor {}'.format(setor_vento))
            #print('Aproado no setor {}'.format(setor_proa))
            #print(diferenca_vento)
            if diferenca_vento < 90:
                print('vento de proa pela esquerda')
                tag_vento = 'hw'
            elif diferenca_vento > 90 and diferenca_vento < 180:
                reciproca_real = diferenca_vento_reciproca
                print('vento de cauda pela esquerda')
                tag_vento = 'tw'
            elif diferenca_vento > 180 and diferenca_vento < 270:
                reciproca_real = 360 - diferenca_vento_reciproca
                print('vento de cauda pela direita')
                tag_vento = 'tw'
            else:
                print('vento de proa pela direita')
                tag_vento = 'hw'

            print()
            print('O ângulo de correção de deriva máximo é {:.2f} graus'.format(acd))
            print()

            

            if diferenca_vento <= 90 or diferenca_vento >= 270:
                acd_real = acd * math.sin(math.radians(diferenca_vento))
                componente = math.cos(math.radians(diferenca_vento))
            else:
                acd_real = acd * math.sin(math.radians(reciproca_real % 360))
                componente = math.cos(math.radians(reciproca_real))
            
            componente_real = velocidade_vento * componente

            print('O ângulo de correção de deriva real é {:.2f} graus'.format(abs(acd_real)))
            #print()
            #print('O valor da componente é: {:.2f}'.format(componente))

            #print('Componente real: {:.2f}'.format(componente_real))

            if tag_vento == 'hw':
                velocidade_final = tas - componente_real
            elif tag_vento == 'tw':
                velocidade_final = tas + componente_real

            print()

            print('A velocidade ajustada pela componente é {:.2f} nós'.format(velocidade_final))

            # print()
            # print('Diferença de vento recíproco: {:.2f}'.format(reciproca_real))
            # print('Diferença de vento: {:.2f}'.format(diferenca_vento_real))
            # print('Seno da diferença de vento recíproco: {:.2f}'.format(math.sin(math.radians(diferenca_vento_reciproca))))
            # print('Seno da diferença de vento: {:.2f}'.format(math.sin(math.radians(diferenca_vento))))

            print()

            if velocidade_final > tas:
                print('Componente de cauda')
            else:
                print('Componente de proa')


        except ValueError:
            print("O valor inserido é inválido.")

        print()
        continua = input('Deseja calcular novamente? (N) para sair ')
        if continua == 'n' or continua == 'N':
            break