'''
 Diff utility is a data comparison tool which calculates and displays differences between two texts. 
 It determines the smallest set of deletions and insertions to create one text from another
 Diff utility is a line-oriented unlike edit distance which is character oriented
'''
# It is an extension of LCS problem
# Input: String X and Y
# '+' : If current character of Y is not present in X
# '-' : If current character of X is not present in Y

def util(X, Y, m, n, T):
    
    # if last character of X and Y matches
    if m>0 and n>0 and X[m-1]==Y[n-1]:
        util(X, Y, m-1, n-1, T)
        print(" " + X[m-1], end = ' ')
    
    # current character of Y is not present in X 
    elif n>0 and (m==0 or T[m][n-1] >= T[m-1][n]):
        util(X, Y, m, n-1, T)
        print(" +" + Y[n-1], end = ' ')

    # current character of X is not present in Y
    elif m>0 and (n==0 or T[m-1][n] >= T[m][n-1]):
        util(X, Y, m-1, n, T)
        print(" -" + X[m-1], end = ' ')

def diffUtility(X, Y):
    m, n = len(X), len(Y)
    
    # fill lookup table 
    T = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1]==Y[j-1]:
                T[i][j] = T[i-1][j-1] + 1 
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])
    
    util(X, Y, m, n, T)

         

if __name__ == '__main__':
    X = "XMJYAUZ"
    Y = "XMJAATZ"

    diffUtility(X, Y, )
