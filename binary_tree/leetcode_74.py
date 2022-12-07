def search(nums, target):

    for i in nums:
        start = 0
        end = len(i)-1

        while start <= end:
            #calculate the middle value
            middle = (start + end)//2

            if i[middle] > target:
                end = middle - 1
            elif i[middle] < target:
                start = middle + 1
            else:
                return True
    else:
        return False


nums = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(search(nums, target))