def money_change(money):
    assert 0 <= money <= 10 ** 3
    return int(money / 10) + int((money % 10) / 5) + int(money % 5)

if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))