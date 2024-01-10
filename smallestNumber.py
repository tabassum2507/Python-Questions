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
