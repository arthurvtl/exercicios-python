f = input('Digite uma frase qualquer: ').upper().strip()

fA = f.count('A')
fD = f.split()
print(' ')

print('A letra "A" aparece {} vezes na frase'.format(f.count("A")))
print(' ')
print('A primeira letra "A" aparece na posição {}'.format(f.find('A')+1))
print(' ')
print('A última letra "A" aparece na posição {}'.format(f.rfind('A')+1))
