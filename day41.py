class myclass:
    j = 7
pl = myclass( )
print(pl.j)
class human:
    def arm(self):# لا تنسين مهم جدا حينا السيلف عشان اعرف انه حقت الكلاس
        print("this is an arm ")
    def head(self):
        print("this is a head ")
human().arm()  
human().head() 
class student:
    def __init__(self,name,age,sex):
        print("the name is : ",name)
        print("the age is : ",age)  
        print("the sex is : ",sex)
u = student("bodour","11 ","f")