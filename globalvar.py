count=0

def incre():
    global count
    count+=1
    print("inside function",count)

incre()
print("outside function",count)