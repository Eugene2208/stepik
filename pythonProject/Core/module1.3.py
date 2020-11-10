def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n

def comb(n: int, k: int):
    return print(fac(n)//(fac(n - k)*fac(k)))


comb(3, 2)
