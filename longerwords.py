lst=["abc","xyz","opo","python","language"]
n=3
long=[]
for lst in lst:
    if len(lst)>n:
        long.append(lst)
print(f"words longer then{n} character",long)


