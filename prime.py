print("=====prime number============")

n=int(input("enter the number:"))
for i in range(2,n):
    if n%2==0:
         print("not prime number")
         break
    else:
         print("prime number")