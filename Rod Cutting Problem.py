# Rod cutting problem
# Maximize profit given the prices of each length
# rodCut[n] = max(price[i] + rodCut[n-1])

def rodCut(price, n):
    # initialize all prices to be zero
    T = [0] * (n+1)

    for i in range(1,n+1):
        # divide rod of length i into two rods -> j and i-j
        for j in range(1,i+1):
            T[i] = max(T[i], price[j] - T[i-j])
    
    return T[n]


if __name__ == '__main__':
    price = [1,5,8,9,10,17,17,20]
    n = 4
    print("Maximum profit = ", rodCut(price, n))