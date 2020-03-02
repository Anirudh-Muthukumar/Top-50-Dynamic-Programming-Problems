def fillLookup(x, y, m, n):
    maxLen = 0
    ending_index = m
    for i in range(1,m):
        for j in range(1,n):
            if x[i-1]==y[j-1]:
                lookup[i][j] = lookup[i-1][j-1] + 1
                
                if lookup[i][j] > maxLen:
                    maxLen = lookup[i][j]
                    ending_index = i

    return maxLen, ending_index


x = "ABC"
y = "BABA"

m, n = len(x), len(y)

lookup = [ [0 for i in range(30)] for j in range((30))]

# fill lookup table
i, j = fillLookup(x, y, m, n)
print(x[j-i:j])