# 0-1 Knapsack problem

def knapsack(values, weights, n, W, lookup):

    if W<0:
        return -float('inf')

    # no elements left to pick
    if n<0 or W==0:
        return 0
    
    key = str(n) + '|' + str(W)

    if key not in lookup:
        # include and exclude the current element and 
        include = values[n] + knapsack(values, weights, n-1, W - weights[n], lookup)
        exclude = knapsack(values, weights, n-1, W, lookup)
        lookup[key] = max(include, exclude)
    
    return lookup[key]


if __name__ == '__main__':
    values = [20, 5, 10, 40, 15, 25]
    weights = [1, 2, 3, 8, 7, 4]
    W = 10
    n = len(values)
    print("\nKnapsack = ", knapsack(values, weights, n-1, W, {}))