# reverse string question

def reverse(str):
    str = str.split() # splitting in array
    rev = [] # initiaze empty array
    for i in range(len(str) - 1, -1, -1): # reverse itrating and inserting
        rev.append(str[i])
    rev = " ".join(rev) # joining into a string
    return rev

print(reverse("stones into turned be can cones"))

# time complexity: O(n)
# space complexity: O(n)

def reverse2(str):
    return " ".join(str.split()[::-1])
print(reverse2("stones into turned be can cones"))