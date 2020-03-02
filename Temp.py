# Longest Common Subsequence using DP

def LCS(x, y, m, n, T):
    
    if m==0 or n==0:
        return [""]
    
    if x[m-1]==y[n-1]:
        lcs = LCS(x, y, m-1, n-1, T)
        for i in range(len(lcs)):
            lcs[i] = lcs[i] + x[m-1]
        return lcs

    if T[m-1][n] > T[m][n-1]:
        return LCS(x, y, m-1, n, T)
    elif T[m][n-1] > T[m-1][n]:
        return LCS(x, y, m, n-1, T)
    else:
        left =  LCS(x, y, m-1, n, T)
        top =  LCS(x, y, m, n-1, T)
        return top + left

if __name__ == '__main__':

    x = "ABC"
    y = "BABA"

    # Fill lookup
    T = [[0 for _ in range(len(y)+1)] for _ in range(len(x)+1)]
    maxlen = 0
    end_index = 0

    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            if x[i-1]==y[j-1]:
                T[i][j] = T[i-1][j-1] + 1
            if T[i][j] > maxlen:
                maxlen = T[i][j]
                end_index = i

    m, n = len(x), len(y)
    print("LCS = ", x[end_index - maxlen : maxlen])