from itertools import combinations 
lst = [8,3,5,4,5]
x = 8
y = 9
if  x > y:
  tmp = x
  x = y
  y = x
count = 0
lst.sot()
l = len(lst)
i = 1
while i <= 1:
  for j in sorted(list(combinations(lst,i)), key = lambda x : sum(x), reverse = True):
    print(j)
    if (sum(j) <= x):
      count+= 1
      for x in j:
        lst.remove(x)
      break;
  i+=1

i = 1
while i <= 1:
  for j in sorted(list(combinations(lst,i)), key = lambda x : sum(x), reverse = True):
    print(j)
    if (sum(j) <= y):
      count+= 1
      for x in j:
        lst.remove(x)
      break;
print(count)
