def appending(stack, track, i):
    stack.append(i)
    if len(track) == 0:
        track.append(i)
    else:
        if track[-1] > i:
            track.append(track[-1])
        else:
            track.append(i)

if __name__ == '__main__':
    stack = []
    track = []
    n = int(input())
    for i in range(n):
        query = input().split()
        if query[0] == 'push':
            appending(stack, track, int(query[1]))
        elif query[0] == 'pop':
            stack.pop()
            track.pop()
        elif query[0] == 'max':
            print(track[-1])
        else:
            assert(0)
