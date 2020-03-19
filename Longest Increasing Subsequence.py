'''
Longest Increasing Subsequence (LIS) problem is to find a subsequence of a given sequence such that
elements of the subsequence are arranged in ascending order.

Time Complexity: O(n^2)
# Space complexity: O(n) - to find LIS
# Space complexity: O(n^2) - to find all LIS

'''

def LIS(A):
    # array to store sub-problem: LIS of subsequence ending at i
    n = len(A)
    L = [0] * n 

    # first element forms a subsequence on its own
    L[0] = 1
    
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and L[j] > L[i]:
                L[i] = L[j]

        # every element forms a subsequence of its own irrespective of other elements
        L[i] += 1 

    return max(L)

def findAllLIS(A):
    n = len(A)
    L = [[] for _ in range(n)]

    L[0].append(A[0])
    # print(L)

    for i in range(1, n):
        for j in range(i):
            if A[j]<A[i] and len(L[j]) > len(L[i]):
                L[i] = L[j][:]  # shallow copy using slice
                
        L[i].append(A[i])


    for size, lis in sorted((-len(lis), lis) for lis in L):
        print(lis)
        break

if __name__ == '__main__':
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 17, 5]

    print("Length of LIS = ", LIS(arr))

    findAllLIS(arr)
