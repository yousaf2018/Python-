def insertionSort(array):
    size = len(array)
    i = 1
    while i<size:
        current = array[i]
        j = i-1
        while j>=0 and current<array[j]:
            array[j+1]=array[j]
            j -= 1
        array[j+1]=current
        i += 1
list = [3,2,1,3,45,43]
insertionSort(list)
print(list)