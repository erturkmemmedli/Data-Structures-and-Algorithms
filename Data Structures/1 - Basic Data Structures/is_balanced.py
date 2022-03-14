def isBalanced(s):
    stack = []
    for i in range(len(s)):
        if s[i] in ['[','{','(']:
            stack.append(s[i])
            stack.append(i + 1)
            #print('stack', stack)
        elif s[i] not in [')','}',']']:
            continue
        elif len(stack) == 0:
            #print(f'closing bracket {s[i]} at index {i}')
            return i + 1
        else:
            index = stack.pop()
            x = stack.pop()
            if (x == '(' and s[i] != ')') or (x == '{' and s[i] != '}') or (x == '[' and s[i] != ']'):
                #print(f'closing bracket {s[i]} at index {i} dismatches with opening bracket {x} at index {index}')
                return i + 1
            #print('match:', x, s[i])
            #print('stack', stack)
    if len(stack) == 0:
        return "Success"
    else:
        #print(f'opening bracket {stack[0]} at index {stack[1]}')
        return stack.pop()

if __name__ == "__main__":
    string = input()
    print(isBalanced(string))
