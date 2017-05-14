def is_matched(expression):
  open = ['{', '[', '(']
  close = ['}', ']', ')']
  stack = []
  for i in range(0,len(expression)):
    if expression[i] in open:
      stack.append(expression[i])
    if expression[i] in close:
      if len(stack) > 0 :
        tmp = stack.pop()
        idx = close.index(expression[i])
        if tmp != open[idx]:
          return False
      else:
        return False
  if len(stack) > 0:
    return False
  return True

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"