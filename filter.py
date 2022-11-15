
numbers = [1,2,3,4,88,90,99,10004,]

def isEven(n):
  return n % 2 == 0

# replacing the avove def func with a lambda func and the filter func

result = filter(lambda n: n % 2 == 0, numbers)

#result = filter(isEven, numbers)
print(list(result))