print ("this program is made by Rishu Raj")
a = int (input("enter the length of 1st side of triangle  :  "))
b = int (input("enter the length of 2nd side of triangle :  "))
c = int (input("enter the length of 3rd side of triangle :  "))
if a==b==c :
    print ("this triangle is equilateral")
if a==b or a==c or b==c :
    print ("this is an isosceles triangle")
if a!=b and a!=c and b!=c :
    print ("this is an scalane triangle")
