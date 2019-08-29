age = 33
text ="my name bodour i am {}"
print(text.format(age))
qunantity = 77
itemno = 123
price= 78
myorder = "i want {} pieces of item {} for {} dollars."
print(myorder.format(qunantity,itemno,price))
qunantity = 77
itemno = 123
price= 78
myorder = "i want {2} pieces of item {0} for {1} dollars."
print(myorder.format(qunantity,itemno,price))