# Longest Common Subsequence

def util(x, y, m, n):
    if m==0 or n==0:
        return 0
    
    key = str(m) + '|' + str(n)

    if key not in lookup:
        if x[m-1]==y[n-1]:
            lookup[key] = util(x, y, m-1, n-1) + 1
        else:
            lookup[key] = max(util(x, y, m, n-1), util(x, y, m-1, n))
    
    return lookup[key]

def LCS(x, y):
    return util(x, y, len(x), len(y))


x = 'ABCBDAB'
y = 'BCDABA'

lookup = {}

print(LCS(x, y))