s = float(input('Digite o valor do seu sálario: '))

aum = s * 0.15
aumAplic = s + aum

print('Parabéns! Você recebeu um bônus salarial de 15%. \nO seu sálario antigo, cujo valor era de R${}, agora passar a ser de R${} !'.format(s,aumAplic))