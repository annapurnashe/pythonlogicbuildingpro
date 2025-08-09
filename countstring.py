# count the number of strings "
# "where the string length is 2 or more and the first and"
#" last character are same from a given list of strings.


s=['abc', 'xyz', 'aba', '122']
count=0

for i in s:
    if len(i)>=2 and i[0]==i[-1]:
        count+=1
print("number of string ",count)


