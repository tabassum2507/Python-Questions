def arrySmall(arr):
    if not arr:
        print("Array is empty.")
        return

    minArr = arr[0]

    for i in range(len(arr)):
        if arr[i] < minArr:
            minArr = arr[i]

    for i in range(len(arr)):
        arr[i] = minArr

    print("Smallest array element:", minArr)


arrySmall([])

def arryLarg(arr):
    if not arr:
        print("Array is empty.")
        return

    maxArr = arr[0]

    for i in range(len(arr)):
        if arr[i] > maxArr:
            maxArr = arr[i]

    print("Largest array element:", maxArr)

# Example usage:
arryLarg([22,4,77,89,999,9])
