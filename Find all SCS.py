'''
 Find all SCS of given strings X and Y

 Time Complexity: O(mn)
 Space Complexity: O(mn)
  
 '''

def SCS(X, Y, m, n, lookup):

    # if either of string is empty
    if m==0:
        return [Y[:n]]
    if n==0:
        return [X[:m]]
    
    # if last chars are same
    if X[m-1]==Y[n-1]:
        scs = SCS(X, Y, m-1, n-1, lookup)
        for i in range(len(scs)):
            scs[i] += X[m-1]
        return scs 
    
    # SCS(X[1..m]) < SCS(Y[1..n])
    if lookup[m][n-1] < lookup[m-1][n]:
        scs = SCS(X, Y, m, n-1, lookup)
        for i in range(len(scs)):
            scs[i] += Y[n-1]
        return scs 

    # SCS(X[1..m]) > SCS(Y[1..n])
    if lookup[m][n-1] > lookup[m-1][n]:
        scs = SCS(X, Y, m-1, n, lookup)
        for i in range(len(scs)):
            scs[i] += X[m-1]
        return scs 

    # if both top and left are same 
    top = SCS(X, Y, m-1, n, lookup)
    for i in range(len(top)):
        top[i] += X[m-1]
    
    left = SCS(X, Y, m, n-1, lookup)
    for i in range(len(left)):
        left[i] += Y[n-1]
    
    return top + left

def findAllSCS(X, Y):
    m, n = len(X), len(Y)

    lookup = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # when target is empty
    for i in range(m+1):
        lookup[i][0] = i
    
    # when source is empty
    for j in range(n+1):
        lookup[0][j] = j 
    

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1]==Y[j-1]:
                lookup[i][j] = lookup[i-1][j-1] + 1 
            else:
                lookup[i][j] = min(lookup[i-1][j], lookup[i][j-1]) + 1 
    

    # returns all SCS 
    scs = SCS(X, Y, m, n, lookup)

    print("All SCS of given strings: ")
    for string in set(scs):
        print(string)

if __name__ == '__main__':
    X = "ABCBDAB"
    Y = "BDCABA"

    findAllSCS(X, Y)