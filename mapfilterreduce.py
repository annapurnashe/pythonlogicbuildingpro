#map
from functools import reduce

num=[1,2,3,4]
res=map(lambda x: x*2,num)
print(list(res))


#filter
num=[1,2,3,4]
res=filter(lambda a:a%2==0,num)
print(list(res))

#Reduce

num=[1,2,3,4]
res=reduce(lambda x,y:x*y,num)
print(res)