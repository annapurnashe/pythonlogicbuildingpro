def multi(x):
    def multiply(n):
        return x*n
    return multiply

disp1=multi(3)
disp2=multi(6)

print(disp1(10))
print(disp2(10))

print("==================================")

def ankita():

    def sunny():
        print("inner fun")
    return sunny

disp=ankita()
print("outer function.")
disp()

print("=====================================")

def getname(sname):
    def gree(gm):
        print("hi {},{}".format(sname,gm))
    return gree

grt=getname("ankita")
grt("good morning")
grt("good evening")

