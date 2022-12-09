def search(array):

    start = 0
    end = len(array)-1

    while start<=end:
        middle = (start+end)//2

        if array[middle]>array[middle+1]:
            end = middle-1
        else:
            start = middle+1

    return start

array = [0,10,5,2]

print(search(array))