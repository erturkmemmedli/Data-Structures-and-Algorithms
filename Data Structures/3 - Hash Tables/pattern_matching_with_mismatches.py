import sys

def compute_mismatch(k, text, pattern, i, left, right):  
    global mismatch
    if mismatch > k:
        return 
    if right >= left:
        mid = (right + left) // 2   
        if text[i + mid] != pattern[mid]:
            mismatch += 1
        if len(pattern[:mid]) != 0:
            if text[i:i + mid] != pattern[:mid]:
                compute_mismatch(k, text, pattern, i, left, mid - 1)           
        if len(pattern[mid + 1:]) != 0:
            if text[i + mid + 1:] != pattern[mid + 1:]:
                compute_mismatch(k, text, pattern, i, mid + 1, right)          
    else:
        return
            
def matching_with_mismatches(k, text, pattern):
    global mismatch
    result = []
    for i in range(len(text) - len(pattern) + 1):
        mismatch = 0
        left = 0
        right = len(pattern) - 1
        compute_mismatch(k, text, pattern, i, left, right)
        if mismatch <= k:
            result.append(i)  
    return result

if __name__ == '__main__':
    for query in sys.stdin.readlines():
        k, text, pattern = query.split()
        result = matching_with_mismatches(int(k), text, pattern)
        print(len(result), *result)