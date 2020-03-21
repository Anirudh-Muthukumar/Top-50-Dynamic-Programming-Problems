'''
Given a pattern and a string determine the number of times the pattern appears in the string 
as a subsequence

Time complexity : O(mn)
Space complexity:

'''

def countPattern(string, pattern):
    m, n = len(string), len(pattern)

    T = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # If pattern is empty, we have found the subsequence
    for i in range(m+1):
        T[i][0] = 1
    
    # If string is empty, we have not the subsequence
    for j in range(1, n+1):
        T[0][j] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            # If two characters are same, recur for two cases:
            # 1. Exclude current character in both string and pattern
            # 2. Exclude current character only in string
            if string[i-1]==pattern[j-1]:
                T[i][j] = T[i-1][j-1] + T[i-1][j]
            # If characters are not same, exclude current character in string
            else:
                T[i][j] = T[i-1][j]
    
    return T[m][n]


if __name__ == '__main__':
    pattern = "sue"
    string = "subsequence"

    print("\n# of subsequences = %d\n" %countPattern(string, pattern))