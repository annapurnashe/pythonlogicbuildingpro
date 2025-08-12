lst=[10,20,30,40,50,10,20,30,40,50]
print(lst)

for i in enumerate(lst):
    print(i)

print("============================================")

s="PYTHON"
for i in enumerate(s):
    print(i)




print("--------------------------------------------")

for ind,val in enumerate(s):
    if(val=="O"):
        print(ind,"==>",val)


