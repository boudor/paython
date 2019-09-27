def my_function(food) :
    for x in food:
        print(x)
fruts = ["apple","banan","cherry"] 
my_function(fruts)
def my_function(x):
    return 6 * x
print(my_function(4))
print(my_function(6))
print(my_function(94))
def my_function(child1,child2,child3):
    print("the youngest child is "+ child3)
my_function(child1 = "emil",child2 = "tobias",child3 = "lines")
def thisRecursion(rec):
    if(rec > 0):
        result = rec + thisRecursion(rec-1)
        print(result)
    else:
        result = 0
    return result
print("\n\nrecursion results:")
thisRecursion(8)