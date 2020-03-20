'''
In 0-1 Knapsack problem, we are given a set of weights and associated values for each weight.
The goal of the problem is to find number of elements to include in a collection such that
the value is maximum and sum weight of the elements is less than or equal to given weight. 

Time Complexity: O(nW)
Space Complexity: O(nW)
'''

def knapsack(values, weights, n, W, lookup):

    # if weight becomes negative : prune the path
    if W<0:
        return -float('inf')
    
    # if not items left or weight becomes 0 
    if n<0 or W==0:
        return 0 
    
    # dynamic input of the subproblem
    key = str(n) + '|' + str(W)

    if key not in lookup:
        # include the current item
        include = values[n] + knapsack(values, weights, n-1, W - weights[n], lookup)

        # exclude the current item
        exclude = knapsack(values, weights, n-1, W, lookup)

        lookup[key] = max(include, exclude)
    
    return lookup[key]

if __name__ == '__main__':
    values = [20, 5, 10, 40, 15, 25]
    weights = [1, 2, 3, 8, 7, 4]
    W = 10
    n = len(values)

    print("\nKnapsack value = %d\n" % knapsack(values, weights, n-1, W, {}))
