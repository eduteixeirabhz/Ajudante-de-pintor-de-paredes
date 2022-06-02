l = float(input('Largura da parede:'))
a = float(input('Altura da parede: '))
ar = l * a
print('Sua parede tem {} de largura por {} de altura , e sua área é de {} m²'.format(l, a, ar))
tinta = ar/2
print('Para pintar essa parede você precisará de {} litros de tinta'.format(tinta))