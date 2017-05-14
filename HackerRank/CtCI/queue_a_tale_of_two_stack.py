class MyQueue(object):
    def __init__(self):
        self.new_to_old = []
        self.old_to_new = []
    
    def peek(self):
      self.prepare()
      return self.new_to_old[len(self.new_to_old)-1]
        
    def pop(self):
      self.prepare()
      return self.new_to_old.pop()
    
    def prepare(self):
      if not self.new_to_old:
        while self.old_to_new:
          self.new_to_old.append(self.old_to_new.pop())
        
    def put(self, value):
        self.old_to_new.append(value)

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
        