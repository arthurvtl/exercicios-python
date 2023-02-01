nome = input('Olá, qual seu nome? ')
n1 = int(input(nome + ', digite quanto vc tirou na primeira prova: '))
n2 = int(input(nome + ', digite quanto vc tirou na segunda prova: '))

m = (n1 + n2) / 2

print('A média da nota das provas 1 e 2 de {} é igual a {} '.format(nome,m))

print('='*150)

if(m>=6):
    print("você foi aprovado :D")
else:
    print('você foi reprovado :c')