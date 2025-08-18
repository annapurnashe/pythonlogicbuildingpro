from typing import overload

'''s='python'
itobj=iter(s)
while True:
    try:
        item=next(s)
        print(item)
    except StopIteration:
          break'''''


s = 'Python'
itobj = iter(s)
while True:
    try:
         item = next(itobj)      # Iterate by calling next
         print(item)
    except  StopIteration:         # exception will happen when iteration will over
     break

