
def quick_sort(nums, low, high):
    if low < high:
        part = partition(nums, low, high)
        quick_sort(nums, low, part - 1)
        quick_sort(nums, part + 1, high)
    return nums

def partition(nums, low, high):
    pivot = nums[high]
    i = low
    j = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i
    

list = [5, 90, 202, 12, 4, 67, 72, 37, 63, 89, 93, 105]
quick_sort(list, 0, len(list) - 1)

print(list)