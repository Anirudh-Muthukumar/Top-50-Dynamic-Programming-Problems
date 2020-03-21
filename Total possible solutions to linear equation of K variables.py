'''
Given the coefficients of linear equation of K variables and the RHS, find the total
possible solutions to the equation.

Time complexity :
Space complexity:

'''

def countSolutions(coeff, k, target, lookup):

    # solution found
    if target==0:
        return 1 
    
    # if run out of elements or target has become negative
    if k<0 or target<0:
        return 0 
    
    key = str(k) + '|' + str(target)

    if key not in lookup:
        # we include current item
        include = countSolutions(coeff, k, target - coeff[k], lookup)

        # we exclude current item
        exclude = countSolutions(coeff, k-1, target, lookup)

        lookup[key] = include + exclude 
    
    return lookup[key]

if __name__ == '__main__':
    coeff = [1, 3, 5, 7]
    target = 8 
    k = len(coeff)
    
    print("\n# of solutions = %d\n" %countSolutions(coeff, k-1, target, {}))