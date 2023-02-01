h = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura desta mesma parede: '))

aTotal = h*l
litrosTinta = aTotal /2

print('A área total desta parede é de {}m² e a quantidade necessária de litros de tinta para pinta-lá é de, aproximadamente, {:.1f}L'.format(aTotal,litrosTinta))