# Longest Palindromic Subsequence

def util(x, i, j):
    if i>j:
        return 0

    if i==j:
        return 1
    
    if x[i]==x[j]:
        return util(x, i+1, j-1) + 2
    
    else:
        return max(util(x, i+1, j), util(x, i, j-1))

def LPS(x):
    print("LPS = ", util(x, 0, len(x)-1))


if __name__ == '__main__':

    x = 'ABBDCACB'

    LPS(x)