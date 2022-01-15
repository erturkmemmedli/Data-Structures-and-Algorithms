def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)
    unit_price = []
    for i in range(len(prices)):
        unit_price.append(prices[i]/weights[i])
    combined = []
    for i in range(len(prices)):
        combined.append([weights[i],unit_price[i]])
    sorted_combined = sorted(combined, key = lambda x: x[1],  reverse = True)
    amount = 0
    for i in range(len(sorted_combined)):
        if capacity - sorted_combined[i][0] >= 0:
            capacity -= sorted_combined[i][0]
            amount += sorted_combined[i][0] * sorted_combined[i][1]
            continue
        amount += capacity * sorted_combined[i][1]
        break
    return amount

if __name__ == "__main__":
    n, input_capacity = map(int, input().split())
    input_prices = []
    input_weights = []
    for i in range(n):
        inputs = tuple(map(int, input().split()))
        input_prices.append(inputs[0])
        input_weights.append(inputs[1])
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))