print('Equação de segundo Grau')

a = float(input('Digite um número para a:'))
b = float(input('Digite um número para b:'))
c = float(input('Digite um número para c:'))


# a = 1
# b = -3
# c = -10

delta = ((b)**2) - (4*(a)*(c))

if delta > 0:
    print('A equação possui duas soluções reais.')
    raiz_delta = (delta **(1/2))

    x_l = (-(b) + raiz_delta)/2
    x_ll = (-(b) - raiz_delta)/2

    print(f'{raiz_delta=}')
    print(f'Solução S=[{x_l}, {x_ll}]')

elif delta == 0:
    print('A equação possui uma solução real')

else:
    print('A equação não possui solução real.')
