seq = [2,7,11,15]
output = 9

def twoSums(number, target):
    # checking input
    if not (number or target):
        return "wrong input"
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            if number[i] + number[j] == output:
                return [i, j]

print(twoSums(seq, output))

# time complexity = O(n^2)
# space complexity = O(1)