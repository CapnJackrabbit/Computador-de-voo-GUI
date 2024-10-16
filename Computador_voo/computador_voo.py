import calculo_subida, calculador_acd, calculador_tas, calculador_descida, calculador_dvt

def menu():
    while True:
        try:

            print('1 - Cálculo de subida')
            print('2 - Cálculo de ângulo de correção de deriva')
            print('3 - Calcular TAS à partir de Mach')
            print('4 - Cálculo de descida')
            print('5 - Cálculo de distância/tempo/velocidade')
            print('6 - Sair')
            print()
            opcao = int(input('Escolha uma opção: '))

            if opcao == 1:
                calculo_subida.calcular_subida()

            if opcao == 2:
                calculador_acd.calcular_acd()

            if opcao == 3:
                calculador_tas.calcular_tas()

            if opcao == 4:
                calculador_descida.calcular_descida()

            if opcao == 5:
                calculador_dvt.calcular()

            if opcao == 6:
                break
        
        except ValueError:
            print('A opção informada não é válida...')

menu()
        