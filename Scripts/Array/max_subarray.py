# find subarray with the largest integer

nums = []

def maxSubArray(nums):
    # checking for input
    if not nums:
        return "wrong input"
    elif len(nums) == 1:
        return nums[0]
    # global variable to track maximum sub array
    maximum = nums[0]
    # looping over each itrations to check
    for i in range(len(nums)):
        # variable for checking each itration's sum
        cum_sum = 0
        for j in range(i, len(nums)):
            cum_sum += nums[j]
            maximum = max(cum_sum, maximum)
    return maximum
    


print(maxSubArray(nums))