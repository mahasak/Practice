def has_cycle(head):
    if head == None:
        return False
    visited = [head.data]
    node = head.next
    while node != None and node.next != None:
      if node.data in visited:
          return True
      visited.append(node.data)
      node = node.next
    return False