
def fillLookup(x ,y, m, n):
    for i in range(1, m):
        for j in range(1, n):
            if x[i-1]==y[j-1]:
                lookup[i][j] = lookup[i-1][j-1] + 1
            else:
                lookup[i][j] = max(lookup[i][j-1], lookup[i-1][j])

def LCS(x, y, m, n):
    if m==0 or n==0:
        return [""]
    
    if x[m-1]==y[n-1]:
        lcs = LCS(x, y, m-1,n-1)
        for i in range(len(lcs)):
            old = lcs[i] 
            lcs[i] = old + x[m-1]
        return lcs

    if lookup[m-1][n] > lookup[m][n-1]:
        return LCS(x, y, m-1, n)
    elif lookup[m-1][n] < lookup[m][n-1]:
        return LCS(x, y, m, n-1)
    else:
        top = LCS(x, y, m-1, n)
        left = LCS(x, y, m, n-1)
        return top + left


str1 = "abcbdab" 
str2 = "bdcaba" 
# x = input("Enter 1st string : ")
# y = input("Enter 2nd string : ")
m, n = len(str1), len(str2)

lookup = [ [0 for i in range(30)] for j in range(30) ]

# fill lookup tables
fillLookup(str1, str2, m, n)

# compute all LCSs
# ans = LCS(m, n)
print()
print(LCS(str1, str2, m, n))

print()
# for lcs in LCS(m, n):
#     print(lcs)

