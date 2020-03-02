def knapsack(v, w, n, sum):
    T = [[None for _ in range(sum+1)]for _ in range(n+1)]

    # if list has 0 elements, Weight is 0
    for j in range(sum+1):
        T[0][j] = 0
    
    for i in range(1, n+1):
        for j in range(sum+1): # consider all weights from 0 to max-cap
            if w[i-1] > j: # if weight is negative, dont include ith element
                T[i][j] = T[i-1][j]
            else: # max value of including/excluding the element
                T[i][j] = max(T[i-1][j], T[i-1][j-w[i-1]] + v[i-1])

    return T[n][sum]

lookup = {}
v = [ 20,5,10, 40,15,25]
w = [1,2,3,8,7,4]
target = 10
print("Knapsack value = ", knapsack(v, w, 5, target))