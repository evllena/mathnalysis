import sympy as sym

n = sym.Symbol('n')
a = sym.limit(n / n ** (1 / n), n, sym.oo)

print(a)

