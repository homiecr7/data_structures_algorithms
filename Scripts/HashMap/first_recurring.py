# output the first recurring character in an array
array = [2, 5, 5, 2, 3, 5, 1, 2 , 4]

def firstRecurring(nums):
    recurring = dict() # to hold the object
    for i in nums: # loop over array
        if i in recurring: # checking if the key exists
            recurring[i] += 1 # if exists increment by one
        else:
            recurring[i] = 1 # else create the key
        if recurring[i] >= 2: # after each itration if the key exists retun it
            return i
        else:
            continue
    return "undefined"

# print(firstRecurring(array))

# time complexity = O(n)
# space complexity = O(n)

# only difference between two version is that version 2 is only checking if key already exist and returining it, it is not keeping count of the occurences

def firstRecurring2(nums):
    recurring = dict()
    for i in nums:
        if i in recurring:
            return i
        else:
            recurring[i] = 1
    return "undefined"

print(firstRecurring2(array))