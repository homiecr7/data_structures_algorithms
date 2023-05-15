# moves zeroes to end with the array in place

nums = [0, 0, 1]

def moveZeroes(nums):
    # checking for input
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        return nums
    l = len(nums)

    # if zeroes are present push zero to the end
    for i in range(l):
        if nums[i] == 0:
            nums.append(0)
    print(nums)
    j = 0
    c = 0
    # loop will run for whole length of array
    while c < l:
        # if there is a non zero object move the index 
        if nums[j] != 0:
            j += 1 
        else:
            # if there is zero dont move the index because next index is already in place
            nums.pop(j) 
        c += 1

    return nums

print(moveZeroes(nums))