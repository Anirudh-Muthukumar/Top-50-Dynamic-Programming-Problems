'''
Given a square matrix and starting coordinates, find the probability that a person is alive 
after taking 'N' steps (top, left, bottom, right) in the matrix .

Time complexity : O(n^4)
Space complexity: O(n^4)

'''

def findProbability(side, x, y, N, lookup):

    # man steps out of island
    if not (0<=x<side and 0<=y<side):
        return 0 
    
    # man has taken N steps
    if N==0:
        return 1 
    
    key = str(x) + '|' + str(y) + '|' + str(N)

    if key not in lookup:
        # take a step in each direction
        lookup[key] = (findProbability(side, x-1, y, N-1, lookup) \
                      + findProbability(side, x+1, y, N-1, lookup) \
                        + findProbability(side, x, y-1, N-1, lookup) \
                          + findProbability(side, x, y+1, N-1, lookup))/4

    # return the probability
    return lookup[key]

if __name__ == '__main__':

    side = 3
    x, y = 0, 0 
    N = 3 

    print("\nProbability = %f\n" % findProbability(side, x, y, N, {}))
    
    