def gcd(a, b):
    assert 0 <= a <= 2 * 10 ** 10 and 0 <= b <= 2 * 10 ** 10
    if a<b:
        return gcd(b,a)
    temp = a % b
    if temp == 0:
        return b
    else:
        return gcd(b,temp)
