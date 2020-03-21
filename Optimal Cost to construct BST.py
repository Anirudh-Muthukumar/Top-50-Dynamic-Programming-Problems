'''
Find the optimal cost to construct binary search tree where frequency of each key 
is given in the same order as inorder traversal of the tree

Time complexity : O(n^4)
Space complexity: O(n^4)

'''

def findOptimalCost(freq, i, j, level, lookup):

    # no elements left
    if j<i:
        return 0 
    
    # dynamic input for the subproblem
    key = str(i) + '|' + str(j) + '|' + str(level)

    if key not in lookup:
        
        lookup[key] = float('inf')

        # consider every key as the root and store the cost of subtree

        for k in range(i, j+1):
            # find the cost of left subtree with given root
            leftOptimalCost = findOptimalCost(freq, i, k-1, level+1, lookup)

            # find the cost of right subtree with given root
            rightOptimalCost = findOptimalCost(freq, k+1, j, level+1, lookup)

            # compute cost of given state
            cost = freq[k]*level + leftOptimalCost + rightOptimalCost 

            lookup[key] = min(lookup[key], cost)
    
    return lookup[key]


if __name__ == '__main__':
    freq = [25, 10, 20]
    n = len(freq)
    print("\nOptimal Cost = %d\n" % findOptimalCost(freq, 0, n-1, 1, {}))