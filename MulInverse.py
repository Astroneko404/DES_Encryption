def gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = gcd(b % a, a)
        q = b // a
        r = y - (b // a) * x
        print(y, ' = ', q, ' * ', x, ' + ' , r)
        return (g, r, x)


# Return the tuple of (s, t) such that:
#  1 = s*m + t*a
def modinv(a, m):
    g, x, y = gcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        t = x % m
        s = (1 - t*a) // m
        return (s, t)


a = 92204805
b = 139928096
result = gcd(a, b)
print(result)