# moves zeroes to end with the array in place

nums = [0, 0, 1]

def moveZeroes(nums):
    # checking for input
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        return nums
    l = len(nums)
    for i in range(l):
        if nums[i] == 0:
            nums.append(0)
    print(nums)
    j = 0
    c = 0
    while c < l: 
        if nums[j] != 0:
            j += 1 
        else:
            nums.pop(j) 
        c += 1

    return nums

print(moveZeroes(nums))