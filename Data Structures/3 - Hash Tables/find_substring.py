def find_pattern(text, pattern):
    hash_pattern = hash(pattern)
    hashes = []
    for i in range(len(text) - len(pattern) + 1):
        hashes.append(hash(text[i: i + len(pattern)]))
    result = []
    for h in range(len(hashes)):
        if hashes[h] == hash_pattern:
            result.append(h)
    return result
        
if __name__ == '__main__':
    pattern = input()
    text = input()
    print(*find_pattern(text, pattern))
