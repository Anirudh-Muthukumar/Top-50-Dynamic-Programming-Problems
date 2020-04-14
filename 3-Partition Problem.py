'''
Given an array of integers, check (find) if array can be partitioned into
3 disjoint sets of equal sum and cover the array.     

Time complexity : 
Space complexity:
''' 

def subsetSum(A, n, sum1, sum2, sum3, lookup):
    if sum1==0 and sum2==0 and sum3==0:
        return True
    
    key = (sum1, sum2, sum3) 

    if key not in lookup:
        a, b, c = False, False, False            
        
        if sum1 - A[n]>=0:
            a = subsetSum(A, n-1, sum1 - A[n], sum2, sum3, lookup)
        
        if (not a) and (sum2 - A[n])>=0:
            b = subsetSum(A, n-1, sum1, sum2-A[n], sum3, lookup) 
        
        if (not a) and (not b) and (sum3-A[n])>=0:
            c = subsetSum(A, n-1, sum1, sum2, sum3-A[n], lookup)
        
        lookup[key] = a or b or c       
    
    return lookup[key]

def partition(A):
    if len(A)<3:
        return False   
    sum3 = sum(A)
    return sum3%3==0 and subsetSum(A, len(A)-1, sum3//3, sum3//3, sum3//3, {})

if __name__ == '__main__':
    nums = [7,3,2,1,5,4,8]
    print(partition(nums))