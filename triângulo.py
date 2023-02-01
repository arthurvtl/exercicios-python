import math

co = int(input('Digite o valor do cateto oposto: '))
ca = int(input('Digite o valor do cateto adjacente '))

h = math.sqrt((ca*ca) + (co*co))

print('O valor da hipotenusa tal que, o cateto oposto é igual a {} e o cateto adjacente é igual a {}, o valor da hipotenusa é de {}. '.format(co,ca,h))