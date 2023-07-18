import timeit
def findRecursiveFactorial(num):
    if num <= 1:
        return 1
    return num * findRecursiveFactorial(num - 1)

start = timeit.timeit()
print(findRecursiveFactorial(5))
end = timeit.timeit()
print(f"Recursive: {end - start}")

def findItretiveFactorial(num):
    total = 1
    for i in range(1, num + 1):
        total = total * i
    return total

print(findItretiveFactorial(5))
end = timeit.timeit()
print(end, start)
print(f"Itrative: {end - start}")