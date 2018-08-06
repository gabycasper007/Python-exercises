import functools

# Binary Search
def binary_search(a, x):
  half = len(a) // 2
  if half:
    if a[half] == x:
      return True
    elif a[half] > x:
      return binary_search(a[:half],x)
    else:
      return binary_search(a[half:],x)
  return False
  
print(binary_search([0,1,2,4,6,8,10],8))

# Hanoi
def hanoi (n,s,t,a):
  if n > 0:
    hanoi (n-1,s,a,t)
    if s:
      t.append(s.pop())
    hanoi (n-1,a,t,s)

source, target, helper = [4,3,2,1], [], []
hanoi (len(source),source, target, helper)
print (source, helper, target)

# Factorial
def fact (n):
  assert isinstance (n,int) and n >= 0, "n must be a pozitive integer"
  if n == 0:
    return 1
  else:
    return n * fact (n-1)
  
print (*[fact(n) for n in range(10)])

# Fibonacci
@functools.lru_cache()
def fibs (n):
  assert isinstance(n,int) and n > 0, "n must be a pozitive integer"
  if n == 1 or n == 2:
    return 1
  else:
    return fibs (n-1) + fibs (n-2)

print (*[fibs(x) for x in range(1,100)])
