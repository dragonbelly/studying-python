from globals import array
from sortArray import sortArray

# a different approach to this problem is solved using python classes
# more details at: https://www.geeksforgeeks.org/sort-elements-by-frequency/

def sortArrayElementsByFrequency(arr):
    sortArray(arr)

    dictionary = {}

    count = 1
    for index, elm in enumerate(arr):
        if (index == 0): continue
        
        if (arr[index - 1] == elm): count += 1
        else:
            dictionary[arr[index - 1]] = count
            count = 1
        
        if (index + 1 == len(arr)): dictionary[arr[index - 1]] = count
    
    dictionary = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])}

    newArray = []

    for item in dictionary.items():
        elm = item[0]
        occurences = item[1]

        newArray.extend([elm] * occurences)

    return newArray

array = sortArrayElementsByFrequency(array)
print(array)