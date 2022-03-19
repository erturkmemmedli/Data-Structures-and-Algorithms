import sys
import random

def precompute_hashes(text, l, p, x):
    hash_array = [None] * (len(text) + 1)
    hash_array[0] = 0
    for i in range(1, len(text) + 1):
        hash_array[i] = (x * hash_array[i - 1] + ord(text[i - 1])) % p
        
    Hash = [None] * (len(text) - l + 1)
    for i in range(0, len(text) - l + 1):
        Hash[i] = (hash_array[i + l] - (hash_array[i] * (x ** l) % p)) % p
    return Hash    

def longest_common_substring(string_1, string_2):
    p_1 = 10 ** 9 + 39
    p_2 = 10 ** 9 + 61
    x = random.randint(1, 10 ** 9)
    
    if len(string_1) <= len(string_2):
        pattern = string_1
        text = string_2
    else:
        pattern = string_2
        text = string_1
    
    left = 0
    right = len(pattern)
    
    first_index = 0
    second_index = 0

    while left <= right and left <= len(pattern) and right >= 0:
        breakFlag = False
        tempFlag = False
        
        mid = (left + right) // 2

        Hash_small_1 = precompute_hashes(pattern, mid, p_1, x)
        Hash_small_2 = precompute_hashes(pattern, mid, p_2, x)
    
        Hash_big_1 = precompute_hashes(text, mid, p_1, x)
        Hash_big_2 = precompute_hashes(text, mid, p_2, x)
 
        for i in range(0, len(Hash_small_1)):
            for j in range(0, len(Hash_big_1)):
                if Hash_small_1[i] == Hash_big_1[j] and Hash_small_2[i] == Hash_big_2[j]:
                    if left != mid:
                        first_index = i
                        second_index = j
                        left = mid
                        breakFlag = True
                        break
                    else:
                        first_index = i
                        second_index = j
                        tempFlag = True
                        left += 1
                        break
            if breakFlag == True or tempFlag == True:
                break
                
        if breakFlag == True or tempFlag == True:
            continue
        elif left == right:
            mid -= 1
            break
        else:
            right = mid
    
    if len(string_1) <= len(string_2):
        return first_index, second_index, mid
    else:
        return second_index, first_index, mid

if __name__ == '__main__':
    for query in sys.stdin.readlines():
        string_1, string_2 = query.split()
        print(*longest_common_substring(string_1, string_2))
