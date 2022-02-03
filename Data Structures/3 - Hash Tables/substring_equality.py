from random import randint

def precompute_hashes(text, l, m, x):
    hash_array = [None] * (len(text) + 1)
    hash_array[0] = 0
    for i in range(1, len(text) + 1):
        hash_array[i] = (x * hash_array[i - 1] + ord(text[i - 1])) % m
    Hash = [None] * (len(text) - l + 1)
    for i in range(0, len(text) - l + 1):
        Hash[i] = (hash_array[i + l] - (hash_array[i] * (x ** l) % m)) % m
    return Hash

def substring_equality(text, a, b, l):
    m_1 = 10 ** 9 + 7
    m_2 = 10 ** 9 + 9
    x = randint(1, 10 ** 9)
    Hash_1 = precompute_hashes(text, l, m_1, x)
    Hash_2 = precompute_hashes(text, l, m_2, x)
    if Hash_1[a] == Hash_1[b] and Hash_2[a] == Hash_2[b]:
        return True
    return False

if __name__ == '__main__':
    text = input()
    query = int(input())
    for i in range(query):
        a, b, l = list(map(int, input().split()))
        print("Yes" if substring_equality(text, a, b, l) else "No")