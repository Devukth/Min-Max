def largest(arr, length):
    maximum = arr[0]
    for i in range(1, length):
        if (arr[i] > maximum):
            maximum = arr[i]
    return maximum

def smallest(arr, length):
    minimum = arr[0]
    for i in range(1, length):
        if(arr[i] < minimum):
            minimum = arr[i]
    return minimum

arr = [132, 6574, 134, 87, 4598, 39, 34]

largestItem = largest(arr, len(arr))
smallestItem = smallest(arr, len(arr))
print(largestItem)
print(smallestItem)