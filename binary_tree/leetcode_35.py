def search(nums, target):
    start = 0
    end = len(nums)-1

    while start <= end:
        #calculate the middle value
        middle = (start + end)//2

        if nums[middle] > target:
            end = middle - 1
        elif nums[middle] < target:
            start = middle + 1
        else:
            return middle

    return end+1


nums = [1,3,5,6]
target = 7
print(search(nums, target))