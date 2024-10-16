def calcular_descida():

    while True:
        try:

            altitude_final = int(input('Entre com a altitude final: '))
            altitude_inicial = int(input('Entre com a altitude inicial: '))
            #altitude_inicial = (altitude_inicial * 100)        para usar FL ao invés de altitude
            if altitude_inicial < altitude_final:
                print('A altitude inicial não pode ser menor que a altitude final.')
                raise ValueError
            razao_descida = int(input('Entre com a razão de descida: '))
            # if razao_descida >= 0:
            #     print('A razão de descida não pode ser nulo ou maior que zero.')
                # raise ValueError
            velocidade_indicada = float(input('Entre com a velocidade indicada: '))
            if velocidade_indicada <= 0:
                print('A velocidade indicada não pode ser nula ou negativa.')
                raise ValueError

            delta_altura = altitude_final - altitude_inicial
            tempo = abs(delta_altura / razao_descida)
            fator = ((altitude_final + altitude_inicial) * 0.00001) + 1
            va = velocidade_indicada * fator

            print()
            print('ΔH = {} pés'.format(delta_altura))
            print('Tempo total = {:.1f} minutos'.format(tempo))
            print('Velocidade aerodinâmica = {:.2f}'.format(va))
            print()
        
        except ValueError:
            print('O valor informado é inválido')

        replay = input('Pressione qualquer tecla para efetuar novo cálculo, (N) para sair: ')
        if replay == 'n' or replay == 'N':
            break
        print()