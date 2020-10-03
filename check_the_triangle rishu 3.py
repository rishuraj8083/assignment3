print ("this program is made by Rishu Raj")
a = int (input("enter the length of 1st side of triangle  : "))
b = int (input("enter the length of 2nd side of triangle : "))
c = int(input("enter the last length of the triangle :  "))
if a<(b+c) or b<(a+c) or c<(a+b) :
    print ("this is a valid triangle")
if a>(b+c) or b>(a+c) or  c>(a+c):
    print ("this triangle is not valid")
