# Longest Common Substring

def LCS(x, y):
    n, m = len(x), len(y)

    lookup = [ [0 for _ in range(m+1)] for _ in range(n+1)]
    maxlen = 0
    ending_index = -1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1]==y[j-1]:
                lookup[i][j] = lookup[i-1][j-1] + 1
                if maxlen < lookup[i][j]:
                    maxlen = lookup[i][j]
                    ending_index = i
    
    print(x[ending_index - maxlen : maxlen])


if __name__ == '__main__':
    x = 'ABC'
    y = 'BABA'
    LCS(x, y)