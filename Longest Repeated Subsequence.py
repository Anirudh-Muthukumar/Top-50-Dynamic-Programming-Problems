# LRS is the longest subsequence that appears more than once
# Special case of LCS where i!=j

def LRS(x, y, m, n):
    T = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1]==y[j-1] and i!=j:
                T[i][j] = T[i-1][j-1] + 1
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])


    return T[m][n]

if __name__ == '__main__':

    x = "ATACTCGGA"

    print("LRS = ", LRS(x, x, len(x), len(x)))