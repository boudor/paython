def myfunc(n) :
    return lambda a : a * n 
mydoubler = myfunc(2)
print(mydoubler(11))
def myfunc(n) :
    return lambda a : a * n 
mydoubler = myfunc(2)
mytripler = myfunc(4)
print(mydoubler(11))
print(mydoubler(66))