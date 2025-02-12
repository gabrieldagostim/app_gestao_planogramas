import os

t = 3
m = [[0] * t for _ in range(t)]
cnt = 0

for l in range(t):
    for c in range(t):
        m[l][c] = cnt
        cnt += 1


def mostra_tabuleiro():
    for l in range(t):
        for c in range(t):
            print(f'[{m[l][c]:^1}]', end=' ')
        print()

def logica_jogo(vez):
    print()
    try:
        entrada = int(input(f'Vai jogar [{vez}] em qual posição? '))
    except ValueError as v:
        print('ops... não estava esperando isso, tente novamente')
        entrada = int(input(f'Vai jogar [{vez}] em qual posição? '))

    for l in range(t):
        for c in range(t):
            if entrada == m[l][c]:
                m[l][c] = vez
                print(f'Jogada de [{vez}] na posição {entrada}')
            else:
                # TODO ver se a posição já foi ocupada...
                # TODO fazer esquema de vitoria/derrota
                print('perdeu a vez!!')

def pausa_para_usuario():
    print()
    _ = input('Digite qualquer tecla para voltar ao inicio...')

def header():
    limpatela()
    print('----------------------------')
    print('J O G O  D A   V E L H A')
    print('----------------------------')
    print('Bem vindo ao jogo da velha, abaixo está o tabuleiro')
    print('é em formato de números, digite o número abaixo que quer jogar e divirta-se')
    print()
    mostra_tabuleiro()
    
    
def limpatela():
    os.system('cls')


cont = 0

def vez_de_jogar(cont):
    if cont % 2 == 0:
        return 'x'
    else:
        return 'o'

while True:
    header()
    # pausa_para_usuario()

    x_ou_o = vez_de_jogar(cont)
    logica_jogo(x_ou_o)

    cont += 1