'''
Shortest Common Supersequence (SCS) is the problem of finding a shortest supersequence 
Z of given strings X and Y such that both X and Y are subsequences of Z.
'''

# If last two characters are same: 
#   SCS(X[1..m-1], Y[1..n-1]) + X[m]
# If last two characters are different: 
#   min(SCS(X[1..m-1], Y[1..n]) + X[m], SCS(X[1..m], Y[1..n-1]) + Y[n])

def SCS(X, Y, m, n, lookup):
    
    # if end of either of string is reached
    if m==0 or n==0:
        return m+n  
    
    # unique from dynamic input elements
    key = str(m) + '|' + str(n)

    if key not in lookup:

        # if last characters are same 
        if X[m-1]==Y[n-1]:
            lookup[key] = SCS(X, Y, m-1, n-1, lookup) + 1 
        
        # if last characters are not same 
        else:
            lookup[key] = min(SCS(X, Y, m, n-1, lookup), SCS(X, Y, m-1, n, lookup)) + 1 
    
    return lookup[key]
    

if __name__ == '__main__':
    X = "ABCBDAB"
    Y = "BDCABA"

    print("SCS = ", SCS(X, Y, len(X), len(Y), {}))