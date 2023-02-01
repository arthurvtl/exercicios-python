import random

a1 = input('Digite o nome do Aluno 1: ')
print(' ')
a2 = input('Digite o nome do Aluno 2: ')
print(' ')
a3 = input('Digite o nome do Aluno 3: ')
print(' ')
a4 = input('Digite o nome do aluno 4: ')

lista = [a1, a2, a3, a4]

sorteio = random.choices(lista)
print(' ')
print('Entre os alunos {}, {}, {} e {}, o aluno sorteado foi o {}'.format(a1,a2,a3,a4,sorteio))

print(' ')
print('-'*150)
print(' ')

lista2 = [a1, a2, a3, a4]
print('A ordem original é : ')
print(lista2)
print(' ')
random.shuffle(lista2)
print('A ordem sorteada da lista foi: ')
print(lista2)

