# find subarray with the largest integer

nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):
    # checking for input
    if not nums:
        return "wrong input"
    elif len(nums) == 1:
        return nums[0]
    


print(maxSubArray(nums))