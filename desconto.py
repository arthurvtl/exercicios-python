p = float(input('Qual o valor do produto que o Sr(a) deseja adquirir? '))

desconto = p * 0.05
aplicDesconto = p - desconto

print('O valor do desconto é de {} e aplicando-o ao preço do produto, o produto sai por apenas {}'.format(desconto,aplicDesconto))