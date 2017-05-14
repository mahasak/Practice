def number_needed(a, b):
  count = [0]*26
  for i in range(0,len(a)):
    index = ord(a[i].upper())-65
    count[index] +=1
  for i in range(0,len(b)):
    index = ord(b[i].upper())-65
    count[index] -=1
  return reduce(lambda x,y: abs(x)+abs(y), count)

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)