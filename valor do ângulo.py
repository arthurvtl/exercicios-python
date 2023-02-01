import math

an = float(input('Digite um ângulo qualquer: '))

sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tg = math.tan(math.radians(an))

print('O valor do ângulo {}° em seno é de {:.2f}'.format(an,sen))
print('='*150)
print('O valor do ângulo {}° em cosseno é de {:.2f}'.format(an,cos))
print('='*150)
print('O valor do ângulo {}° em tangente é de {:.2f}'.format(an,tg))