import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

delta = b * (b) - 4*a*c


if (delta < 0):
    print('Não possui raízes reais')
elif (delta == 0):
    x = -b / (2*a)
    print('Temos como solução, duas raízes reais e iguais no valor de: ')
    print(x)
else:
    x1 = (-(b) + math.sqrt(delta)) / (2*a)
    x2 = (-(b) - math.sqrt(delta)) / (2*a)
    print('Temos como solução, duas raízes reais e diferentes no valor de: ')
    print(x1)
    print(x2)
