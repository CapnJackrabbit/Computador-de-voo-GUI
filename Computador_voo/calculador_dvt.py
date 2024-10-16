def calcular():
    print('\nCALCULO DE DISTANCIA/VELOCIDADE/TEMPO')

    valid = True

    while True:
        try:
            tempo = float(input('Tempo, em minutos: '))
            distancia = float(input('Distancia, em NM: '))
            velocidade = float(input('Velocidade, em nós: '))

            if (tempo or distancia or velocidade) < 0:
                raise ValueError
            else:
                valid = True 

        except ValueError:
            print('\n Valor inválido inserido.')
            valid = False

        if valid == True:

            if velocidade and tempo and distancia == 0:
                distancia = (velocidade * tempo) / 60
                print('\nDistância: {:.2f} NM\n'.format(distancia))

            elif distancia and velocidade and tempo == 0:
                tempo = (distancia * 60) / velocidade
                print('\nTempo: {:.1f} minutos\n'.format(tempo))

            elif distancia and tempo and velocidade == 0:
                velocidade = (distancia * 60) / tempo
                print('\nVelocidade: {:.2f} nós\n'.format(velocidade))
        
        replay = input('Deseja calcular novamente? (N) para sair: ')
        print()
        if replay == 'n' or replay == 'N':
            break
        print()