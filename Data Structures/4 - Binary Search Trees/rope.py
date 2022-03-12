def arrange_string(string, head, tail, place):
    cut = string[:head] + string[tail+1:]
    part = string[head:tail+1]
    final = cut[:place] + part + cut[place:]
    return final

if __name__ == '__main__':
    string = input()
    query = int(input())
    for q in range(query):
        i, j, k = list(map(int, input().split()))
        string = arrange_string(string, i, j, k) 
    print(string)