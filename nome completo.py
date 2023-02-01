nome = str(input('Digite seu nome completo: ')).strip()

print('Nome em caixa alta é {}'.format(nome.upper()))
print(' ')
print('Nome em caixa baixa: {}'.format(nome.lower()))
print(' ')
print('Seu nome possui {} letras'.format(len(nome) - nome.count(' ')))
print(' ')

div = nome.split()[0]
divTamanho = len(div)
print('Seu primeiro nome é {} e possui {} letras '.format(div,divTamanho))