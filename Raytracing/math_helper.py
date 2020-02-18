import math

# Makes sure a new color values is in the range [0-255]  
def clamp(number):
  return max(0, min(255, (math.ceil(number))))

def lengthSquared(l):
  #return sum([x**2 for x in l])
  return (l[0]*l[0])+(l[1]*l[1])+(l[2]*l[2])

def length(l):
  return math.sqrt(lengthSquared(l))

def normalized(l):
  #return [x/length(l) for x in l]
  len = length(l)
  return [l[0]/len, l[1]/len, l[2]/len]

def dot(a, b):
  #return sum([x*y for x,y in zip(a,b)])
  return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def add(a,b):
  #return [x+y for x,y in zip(a,b)]
  return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

def sub(a,b):
  #return [x-y for x,y in zip(a,b)]
  return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]

def mult(l, a):
  return [l[0]*a, l[1]*a, l[2]*a]