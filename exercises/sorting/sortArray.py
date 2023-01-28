from globals import array, array_of_0s_1s_and_2s

def changeArrayElementsPosition(arr, pos1, pos2):
    aux = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = aux

def sortArray(arr):
    for index, elm in enumerate(arr):
        if ((index + 1) == len(arr)): break
        if (elm > arr[index + 1]): changeArrayElementsPosition(arr, index, index + 1)
    
    return arr

sortArray(array)
print(array)

# will fail
# sortArray(array_of_0s_1s_and_2s)
# print(array_of_0s_1s_and_2s)