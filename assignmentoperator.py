#AssignmentOpEx4.py

a=int(input("enter value of a:"))
b=int(input("enter value of b:"))

print("original value of a={}".format(a))
print("original value of b={}".format(b))

t=a
a=b
b=t

print("swapped value of a={} b={}".format(a,b))

