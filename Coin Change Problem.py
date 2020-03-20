'''
Given a set of denominations and a target find the total number of unique ways 
to reach the target 

Time complexity :
Space complexity:

'''

def coinChange(denominations, n, Sum, lookup):
    
    # solution found
    if Sum==0:
        return 1 

    # if not coins left or sum has become negative, prune the path
    if n<0 or Sum<0:
        return 0 

    # dynamic input for the subproblem
    key = str(n) + '|' + str(Sum)

    if key not in lookup:
        # include current denomination and recur with n coins because you have unlimited supply
        include = coinChange(denomations, n, Sum - denominations[n], lookup)

        # exclude current denomination and recur with other coins
        exclude = coinChange(denomations, n-1, Sum, lookup)

        lookup[key] = include + exclude
    
    return lookup[key]

if __name__ == '__main__':
    N = 4
    denomations = [1, 2, 3]
    n = len(denomations)
    print("\nTotal # of unique ways = %d\n" %coinChange(denomations, n-1, N, {}))