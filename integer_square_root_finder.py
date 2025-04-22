def binarySearch (num):    
  digits = str(num)
  count = 0
  for digit in digits:
    count += 1
  if count%2!= 0:
    ceiling = 10**((count//2)+1)
    floor = 10**(count//2)
  else:
    ceiling = 10**(count//2)
    floor = 10**((count//2)-1)
    
  high = ceiling
  low = floor
  while high-low>10:
    mid = (low+high)//2
    if mid**2 == num:
      return [False, mid, mid]
    elif mid**2 > num:
      high = mid
    elif mid**2 < num:
      low = mid
  print ()
  return [True, low, high]

def squareTest (num, low, high):
  for i in range (low, high+1):
    if i**2 == num:
      return i
    elif i**2 > num:
      return (i-1)
    elif i**2 < num:
      pass

def findIntegerRoot(testVal):
  if testVal < 100:
    estimated_root = squareTest (testVal, 1, (testVal//2)+1)
    return estimated_root
  elif testVal <= 2500:
    estimated_root = squareTest (testVal, 1, (testVal//2)+1)
    return estimated_root
  proceed, low, high = binarySearch(testVal)
  if proceed == False:
    return low
  estimated_root=squareTest (testVal, low, high)
  return estimated_root
 