def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29  
    digit_set = [str(i) for i in range(10)]
    ops_set = ['+', '-', '*']
    
    assert all(dataset[i] in digit_set for i in range(0, len(dataset), 2))
    assert all(dataset[j] in ops_set for j in range(1, len(dataset), 2))
    digits = [int(dataset[i]) for i in range(len(dataset)) if i % 2 == 0]
    operations = [dataset[i] for i in range(len(dataset)) if i % 2 == 1]
    n = len(digits)
    min_matrix = [['-'] * n for i in range(n)]
    max_matrix = [['-'] * n for i in range(n)]
    
    for i in range(0, n):
        min_matrix[i][i] = digits[i]
        max_matrix[i][i] = digits[i]
    
    for step in range(1, n):
        for i in range(0, n - step):
            j = i + step
            min_matrix[i][j], max_matrix[i][j] = MinMax(i, j, operations, min_matrix, max_matrix)
            
    return max_matrix[0][n-1]
    
def MinMax(i, j, operations, min_matrix, max_matrix):
    minimum = float('inf')
    maximum = - float('inf')

    rule = {'+': lambda x, y : x + y,
            '-': lambda x, y : x - y,
            '*': lambda x, y : x * y}
    
    for k in range(i, j):
        a = rule[operations[k]](min_matrix[i][k], min_matrix[k+1][j])
        b = rule[operations[k]](min_matrix[i][k], max_matrix[k+1][j])
        c = rule[operations[k]](max_matrix[i][k], min_matrix[k+1][j])
        d = rule[operations[k]](max_matrix[i][k], max_matrix[k+1][j])
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
        
    return minimum, maximum

if __name__ == "__main__":
    print(find_maximum_value(input()))