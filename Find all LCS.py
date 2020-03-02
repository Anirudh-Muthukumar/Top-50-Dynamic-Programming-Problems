def fillLookup(x, y, m, n):
    # filling up lookup table
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1]==y[j-1]:
                lookup[i][j] = lookup[i-1][j-1] + 1
            else:
                lookup[i][j] = max(lookup[i-1][j], lookup[i][j-1])

def findAllLCS(x ,y, m, n):
    # finding all LCS

    if m==0 or n==0:
        return [""]   # return list of empty string

    if x[m-1]==y[n-1]:
        lcs = findAllLCS(x, y, m-1, n-1)
        # print(lcs)
        for i in range(len(lcs)):
            old = lcs[i]
            lcs[i] = old + x[m-1]

        return lcs
    
    if lookup[m][n-1] > lookup[m-1][n]:
        return findAllLCS(x, y, m, n-1)

    elif lookup[m][n-1] < lookup[m-1][n]:
        return findAllLCS(x, y, m-1, n)

    else: # both are equal
        top = findAllLCS(x, y, m-1, n)
        left = findAllLCS(x, y, m, n-1)
    
        # merge both the lists
        return top + left

str1 = "abcbdab" 
str2 = "bdcaba" 

# str1 = input("Enter 1st string : ")
# str2 = input("Enter 2nd string : ")

m, n = len(str1), len(str2)

lookup = [ [0 for i in range(n+1)] for j in range(m+1) ]

fillLookup(str1, str2, m, n)

for l in lookup:
    print(l)

for str in findAllLCS(str1, str2, m, n):
    print(str)

