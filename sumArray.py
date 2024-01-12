def sumArray(arr):
    if not arr:
        print("Empty array")
        return
    
    sumArray = 0
    avg = 0
    
    for i in range(len(arr)):
        sumArray = sumArray + arr[i]
        avg = sumArray % len(arr)
    print("sum of array", avg)
    
sumArray([2,55,6,12,9])

def sumArray(arr):
    if not arr:
        print("Empty array")
        return
    
    sumArray = 0
    
    for i in range(len(arr)):
        sumArray = sumArray + arr[i]
        
    avg = sumArray / len(arr)
    print("Avg of array", avg)
    
sumArray([2,55,6,12,9])
