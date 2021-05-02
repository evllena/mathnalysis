def union(x, y):
    z = list(x | y)
    z.sort()
    return z


def cross(x, y):
    z = list(x & y)
    z.sort()
    return z


def diff(x, y):
    z = list(x - y)
    z.sort()
    return z


def sym_diff(x, y):
    z = list(x ^ y)
    z.sort()
    return z


a = set('12345')
b = set('1357')
c = set('059')

print(f'Пересечение множеств a и b:{cross(a, b)}')
print(f'Пересечение множеств a и c:{cross(a, c)}')
print(f'Пересечение множеств b и c:{cross(b, c)}')
print()
print(f'Разность множеств a и b:{diff(a, b)}')
print(f'Разность множеств a и c:{diff(a, c)}')
print(f'Разность множеств b и c:{diff(b, c)}')
print()
print(f'Объединение множеств a и b:{union(a,b)}')
print(f'Объединение множеств a и c:{union(a,c)}')
print(f'Объединение множеств b и c:{union(b,c)}')
print()
print(f'Симметрическая разность множеств a и b:{sym_diff(a, b)}')
print(f'Симметрическая разность множеств a и c:{sym_diff(a, c)}')
print(f'Симметрическая разность множеств b и c:{sym_diff(b, c)}')
