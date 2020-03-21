'''
Given a string and a pattern containing wildcard characters ie., '*' (matches 0 or more characters)
and '?' (matches any character), determine if the pattern matches with the string.  

Time complexity : O(mn)
Space complexity: O(mn)

'''

def patternMatching(X, Y, m, n, lookup):

    # end of string and pattern
    if m==0 and n==0:
        return True   
    
    if n==0:
        return False
    
    # if string reaches end check if remaining pattern characters are '*'
    if m==0:
        for i in range(n):
            if Y[i]!='*':
                return False 

        return True 
    
    key = str(m) + '|' + str(n)
    # print(key)

    if key not in lookup:
        
        # if last characters match, recur for rest of the characters
        if X[m-1]==Y[n-1]:
            lookup[key] = patternMatching(X, Y, m-1, n-1, lookup)
        
        # if last character of pattern is '?'
        elif Y[n-1]=='?' and m>=1:
            lookup[key] = patternMatching(X, Y, m-1, n-1, lookup) 
        
        # if last character of pattern is '*'
        elif Y[n-1]=='*':
            # covers zero or more characters
            lookup[key] = patternMatching(X, Y, m-1, n, lookup) or patternMatching(X, Y, m, n-1, lookup)
        
        else: # characters do not match
            lookup[key] = False
    
    return lookup[key]


if __name__ == '__main__':
    string = "xyxzzxy"
    pattern = "x**x?"
    m, n = len(string), len(pattern)
    # lookup = [[False for _ in range(n+1)] for _ in range(m+1)]
    print("\nDoes the string match pattern ? - %s\n" % patternMatching(string, pattern, len(string), len(pattern), {}))