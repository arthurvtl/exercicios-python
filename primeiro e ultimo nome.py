n = str(input('Digite seu nome completo: '))

nome = n.split()

print('Primeiro nome é: {}'.format(nome[0]))
print(' ')
print('Último nome é: {}'.format(nome[len(nome)-1]))