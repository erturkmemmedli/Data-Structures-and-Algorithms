from collections import deque

def hash_func(string):
    hash_value = 0
    for i in range(len(string)):
        hash_value = (hash_value + ord(string[i]) * (multiplier ** i)) % prime
    return hash_value % bucket_count

def addition(string):
    hash_value = hash_func(string)
    if string not in bucket[hash_value]:
        bucket[hash_value].appendleft(string)
        
def deletion(string):
    hash_value = hash_func(string)
    if string in bucket[hash_value]:
        bucket[hash_value].remove(string)
    
def search(string):
    hash_value = hash_func(string)
    print("yes" if string in bucket[hash_value] else "no")
    
def print_bucket(index):
    if index not in bucket:
        print()
    else:
        print(' '.join(bucket[index]))

if __name__ == '__main__':
    global multiplier, prime, bucket_count, bucket
    multiplier = 263
    prime = 1000000007
    
    bucket_count = int(input())
    bucket = {}
    for i in range(bucket_count):
        bucket[i] = deque()
    
    query_count = int(input())
    queries = [input() for _ in range(query_count)]
        
    for query in queries:
        operation, argument = query.split()
        if operation == 'add':
            addition(argument)
        if operation == 'del':
            deletion(argument)
        if operation == 'find':
            search(argument)
        if operation == 'check':
            print_bucket(int(argument))
