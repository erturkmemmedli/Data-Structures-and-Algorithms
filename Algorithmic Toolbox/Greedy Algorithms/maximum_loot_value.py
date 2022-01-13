def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)
    unit_price = []
    for i in range(len(prices)):
        unit_price.append(prices[i]/weights[i])
    dictionary = dict(zip(weights, unit_price))
    sorted_dictionary = sorted(dictionary.items(), key = lambda x: x[1],  reverse = True)
    amount = 0
    for i in range(len(sorted_dictionary)):
        if capacity - sorted_dictionary[i][0] >= 0:
            capacity -= sorted_dictionary[i][0]
            amount += sorted_dictionary[i][0] * sorted_dictionary[i][1]
            continue
        amount += capacity * sorted_dictionary[i][1]
        break
    return amount
