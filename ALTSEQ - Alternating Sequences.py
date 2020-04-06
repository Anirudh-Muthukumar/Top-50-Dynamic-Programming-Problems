from sys import stdin, stdout 

ip = stdin.readline 
op = stdout.write 

n = int(ip())
A = [int(i) for i in ip().split()]
T = [0 for _ in range(n+1)]

def sign(x, y):
    return (0<x and y<0) or (x<0 and 0<y)
    
def LAS():
    T[0] = 1
    for i in range(1, n):
        for j in range(i):
            if abs(A[j])<abs(A[i]) and sign(A[i], A[j]) and T[j]>T[i]:
                T[i] = T[j]
        T[i] += 1

    return max(T)

print(LAS())
