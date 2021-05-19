import sympy as sym

n = sym.Symbol('n')
a = sym.limit(n / pow(sym.factorial(n), 1 / n), n, sym.oo)

print(a)

