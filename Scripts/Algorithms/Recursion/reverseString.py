def reverseStringItrative(string):
    return "".join([x for x in reversed(string)])
    # return string[::-1]

# print(reverseStringItrative("yoyo mastery"))

def reverseStringRecursive(string):
    if len(string) == 0:
        return string
    else:
        return reverseStringRecursive(string[1:]) + string[0]
print(reverseStringRecursive("yoyo mastery"))
