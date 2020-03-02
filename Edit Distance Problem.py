# Levenshtein distance (Edit distance) problem
# Insertion, deletion or substitution
def editDistance(x, m, y, n):
    T = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # source : non-empty, target: empty -> insertion
    for i in range(1, m+1):
        T[i][0] = i
    
    # source: empty, target: non-empty -> deletion
    for j in range(1, n+1):
        T[0][j] = j
    
    for i in range(1, m+1):
        for j in range(1, n+1):

            # compute substitution cost
            if x[i-1]==y[j-1]: 
                substitutionCost = 0
            else:
                substitutionCost = 1

            # total cost is min(insertion, deletion, substitution)
            T[i][j] = min( min(T[i-1][j] + 1, T[i][j-1]+1), T[i-1][j-1] + substitutionCost)
    
    return T[m][n]

if __name__ == '__main__':
    start = "kitten"
    end = "sitting"
    print("Levenshtein distance = ", editDistance(start, len(start), end, len(end)))