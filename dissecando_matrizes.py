import os

# Matriz inteira
# Triangulo superior
# Diagonal principal
# Triangulo inferior
# matriz de grandeza 4
def mostra_cabecalho():
    os.system('cls')
    print('----------------------------------')
    print('D I S S E C A N D O')
    print('M A T R I Z E S')
    print('----------------------------------')

def escolhas_usuario():
    print('Escolha uma ação')
    print()
    print('[1] - Matriz inteira')
    print('[2] - Triangulo Superior')
    print('[3] - Triangulo Inferior')
    print('[4] - Diagonal Principal')
    print('[5] - Sair')

    num = int(input('Digite a escolha: '))        
    
    return (num, mostra_cabecalho())

def pega_dados_matriz():
    a = '[ ][ ][ ][ ]\n' * 4
    print(a)

    print('VAMOS PREENCHER NOSSA MATRIZ')
    for l in range(t):
        for c in range(t):
            try:
                m[l][c] = int(input(f"Valor para [{l},{c}] -> "))
            except ValueError as e:
                print('Ops.. não entendi, tente novamente um número inteiro! ') 
                print()
                m[l][c] = int(input(f"Valor para [{l},{c}] -> "))
    mostra_cabecalho()
    print('Agora vamos escolher uma ação para essa matriz')
    print('...')

def voltar_ao_inicio():
    print()
    _ = input('Digite qualquer tecla para voltar ao inicio...')

def agradecimento():
    print()
    print('Até breve amigo(a)')

t = 4
m = [[0] * t for _ in range(t)]

mostra_cabecalho()
pega_dados_matriz()

while True:
    num, _ = escolhas_usuario()

    match num:
        case 1:
            for linha in range(t):
                print(m[linha])

            voltar_ao_inicio()
        case 2:
            for l in range(t):
                for c in range(t):
                    if c > l:
                        print(f'[{m[l][c]}]', end='')
                    else:
                        print('[-]', end='')
                print()

            voltar_ao_inicio()
        case 3:
            for l in range(t):
                for c in range(t):
                    if c < l:
                        print(f'[{m[l][c]}]', end='')
                    else:
                        print('[-]', end='')
                print()
            voltar_ao_inicio()
        case 4:
            for l in range(t):
                for c in range(t):
                    if c == l:
                        print(f'[{m[l][c]}]', end='')
                    else:
                        print('[-]', end='')
                print()
            voltar_ao_inicio()

        case 5:
            agradecimento()
            break  

        case _:
            print('Opa meu amigo, opção errada, Tente novamente!')
            voltar_ao_inicio()