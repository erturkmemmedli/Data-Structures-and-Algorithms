def precompute_hashes(text, l):
    Hash = []
    for i in range(len(text) - l + 1):
        Hash.append(hash(text[i: i + l]))
    HD[l] = Hash

def substring_equality(text, a, b, l):
    if l not in HD:
        precompute_hashes(text, l)
    if HD[l][a] == HD[l][b]:
        return True
    else:
        return False

if __name__ == '__main__':
    text = input()
    query = int(input())
    global HD
    HD = {}
    for i in range(query):
        a, b, l = list(map(int, input().split()))
        print("Yes" if substring_equality(text, a, b, l) else "No")
