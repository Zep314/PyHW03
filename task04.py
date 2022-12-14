# Задание: Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def dec2bin(n): # просто делим на 2 и уменьшаем число.
    ret = ''
    while n > 0:
        ret = str(n % 2) + ret
        n = n // 2
    return ret

m = 45
print(f'Десятичное число {m} в двоичной записи будет {dec2bin(m)}')
m = 3
print(f'Десятичное число {m} в двоичной записи будет {dec2bin(m)}')
m = 2
print(f'Десятичное число {m} в двоичной записи будет {dec2bin(m)}')
m = 150
print(f'Десятичное число {m} в двоичной записи будет {dec2bin(m)}')
