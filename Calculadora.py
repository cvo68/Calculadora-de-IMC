print('Vamos calcular agora o seu IMC')

peso = float(input('Digite aqui seu peso: '))
altura = float(input('Digite aqui sua altura: '))
IMC = peso / (altura ** 2)

print(IMC)

if IMC < 19:
    print('Voce esta abaixo do peso com IMC {:.2f}.'.format(IMC))

if 19 < IMC < 25:
    print('Voce esta dentro do peso com IMC {:.2f}.'.format(IMC))

if 25 < IMC < 32:
    print('Voce esta com sobrepeso com IMC {:.2f}.'.format(IMC))

if 32 < IMC < 40:
    print('Voce esta acima do peso com IMC {:.2f}.'.format(IMC))

if IMC > 40:
    print('Voce esta obeso com IMC {:.2f}'.format(IMC))

if IMC < 0:
    print('Nao existe IMC negativo!!!')
    