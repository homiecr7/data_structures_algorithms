def fibonacciItrative(num):
    last = 0
    current = 1
    for i in range(1, num + 1):
        sum = last + current
        last = current
        current = sum
    return sum

print(fibonacciItrative(6))

def fibonacciRecursive(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacciRecursive(num - 1) + fibonacciRecursive(num - 2)
    
print(fibonacciRecursive(2))