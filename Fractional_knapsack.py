# uses python3


import sys

'''fractional knapsack algorithm uses greedy algorithm. Have an option to
 take an entire item or just half of it. 

'''
if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split())) # data entered in one array and is split
    n, capacity = data[0:2]                 # the first two numbers equal n and capacity respectively
    values = data[2:(2 * n + 2):2]          # values are obtained by walking every two steps after the first index
    weights = data[3:(2 * n + 2):2]         # weights are are obtained by walking every two steps after the second index


newlist=[vals/wets for vals,wets in zip(values, weights) ]  # for loop creates the ratio of val to weights used to determine order


items=[]
for i in range(len(values)):
    items.append([values[i], weights[i], newlist[i]]) # creation of a an 2 D array with values,weights and ratio as 0,1 and 2 index res


def getkey(item):
    return item[2]              # function returns the ratio to be used in sorting the key

arr=sorted(items, key=getkey, reverse=True) # array sorted in decreasing order according to the val/wet ratio

def get_optimal_value(capacity, weights, values): # greedy knapsack function
    
    currentweight=0 # initialize weight to 0
    finalvalue=0 # initialize final value
    
    for i in range (len(arr)): # counter
        
        if currentweight + arr[i][1] <= capacity: # checks if weight has reached the allowed weight
            
            currentweight+=arr[i][1]
            finalvalue+=arr[i][0]
            
        else: # take a fraction of the item is we can't take it as a whole
            remainingweight=capacity-currentweight
            finalvalue+= arr[i][0] * (remainingweight/arr[i][1])
            
            break
        
        
    return finalvalue
  

            

opt_value = get_optimal_value(capacity, weights, values)
print("{:.10f}".format(opt_value))



   



       
