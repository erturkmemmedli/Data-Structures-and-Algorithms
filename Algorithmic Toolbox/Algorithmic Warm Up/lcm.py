def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9
    return int((a * b) / gcd(a,b))
  
def gcd(a, b):
    if a<b:
        return gcd(b,a)
    temp = a % b
    if temp == 0:
        return b
    else:
        return gcd(b,temp)
