'''
Given N, return the number of N-digit binary strings without any consecutive 1s. 

Time complexity : O(n)
Space complexity: O(n)

'''
def countStrings(n):
    T = [[0 for _ in range(2)] for _ in range(n+1)]

    T[0][0], T[0][1] = 0, 0  # if no digit is left
    T[1][0], T[1][1] = 2, 1  # if one digit is left

    for i in range(2, n+1):
        # if last digit is 0
        T[i][0] = T[i-1][0] + T[i-1][1]

        # if last digit is 1
        T[i][1] = T[i-1][0]
    
    return T[n][0]
    

def printStrings(n, string, prev_digit):
    # method to print all the N-digit binary strings without any consecutive 1s
    if n==0:
        print(string, end = ' ')
        return 
    
    printStrings(n-1, string + '0', 0)

    if prev_digit==0:
        printStrings(n-1, string + '1', 1)

if __name__ == '__main__':
    N = 5 
    print("\n# of strings = %d\n" % countStrings(N))

    printStrings(N, "", 0)
    print("\n")