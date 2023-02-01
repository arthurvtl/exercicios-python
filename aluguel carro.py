d = float(input('Há quantos dias o carro está alugado? '))
km = float(input('Quantos km foram rodados com o carro ao longo desses dias? '))

pagar = (d*60) + (km*0.15)

print('Foram rodados ao total {} quilômetros com o carro, ao longo de {} dias. \nPortando, o valor a se pagar é de R${}'.format(km, d, pagar))
