
def bubble_sort(nums):
    i = 0
    swapping = True
    while swapping:
        swapping = False
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swapping = True
    return nums