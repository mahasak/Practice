def ransom_note(magazine, ransom):
  dict = {}
  for i in range(0,len(magazine)):
    if hash(magazine[i]) in dict:
      dict[hash(magazine[i])] += 1
    else:
      dict[hash(magazine[i])] = 1
      
  for j in range(0,len(ransom)):
    if hash(ransom[j]) in dict and dict[hash(ransom[j])] > 0 :
      dict[hash(magazine[j])] -= 1
    else:
      return False
  return True

m = 6
n = 4
magazine = "give me one grand today night".strip().split(' ')
ransom = "give one grand today".strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"