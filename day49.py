h = 700
def myfunc():
    h = 899
print(h)
myfunc()
print(h)
def myfunc():
    global x 
    x = 333
myfunc()
print(x)
o = 23456
def myfunc():
    global c
    c = 7890
myfunc()
print(c)