# А тут поиграемся с математическими операторами
# Округление

import math

print('Введите число с точкой: ')

a = float(input())
print(f'Ты ввёл число {a}.')

# Округление числа
print('Round: ' + str(round(a)))

# Принудительное округление в меньшую сторону
print('Floor: ' + str(math.floor(a)))

# Принудительное округление в большую сторону
print('Ceil: ' + str(math.ceil(a)))


