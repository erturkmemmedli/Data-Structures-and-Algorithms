def change(money):
    coins = [1, 3, 4]
    MinimumCoins = [0] * (money + 1)
    for i in range(1, money + 1):
        MinimumCoins[i] = float('inf')
        for j in range(0, len(coins)):
            if i >= coins[j]:
                min_value = MinimumCoins[i-coins[j]] + 1
                if min_value < MinimumCoins[i]:
                    MinimumCoins[i] = min_value
    return MinimumCoins[money]

if __name__ == '__main__':
    amount = int(input())
    print(change(amount))