from random import randint

def are_equal(first, second):
    if len(first) != len(second):
        return False
    for i in range(len(first)):
        if first[i] != second[i]:
            return False
    return True

def poly_hash(string, p, x):
    hash_value = 0
    for i in range(len(string)):
        hash_value = (hash_value + ord(string[i]) * (x ** i)) % p
    return hash_value    

def precompute_hashes(text, pattern_length, p, x):
    Hash = [None] * (len(text) - pattern_length + 1)
    last_substring = text[len(text) - pattern_length:]
    Hash[len(text) - pattern_length] = poly_hash(last_substring, p, x)
    for i in range(len(text) - pattern_length - 1, -1 , -1):
        last = i + pattern_length
        Hash[i] = (x * Hash[i + 1] + ord(text[i]) - (ord(text[last]) * (x ** pattern_length) % p)) % p
    return Hash

def Rabin_Karp(text, pattern):
    p = 31
    x = randint(0, p - 1)
    result = []
    hash_pattern = poly_hash(pattern, p, x)
    pattern_length = len(pattern)
    Hash = precompute_hashes(text, pattern_length, p, x)
    for i in range(len(text) - len(pattern) + 1):
        if hash_pattern != Hash[i]:
            continue
        if are_equal(text[i: i + len(pattern)], pattern):
            result.append(i)
    return result

if __name__ == '__main__':
    pattern = input()
    text = input()
    print(*Rabin_Karp(text, pattern))