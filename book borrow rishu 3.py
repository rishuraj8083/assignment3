print ("this program is made by Rishu Raj")
print ("this program will help you to find the fine of books")
a = int(input("enter the days after you return the books  : "))
if a==5 or a<5 :
    print ("you have to pay 50paise for borrowing the book")
if (a==6 or a<10 or a==10) and a>5 :
    print ("you have to pay 1rupee for borrowing the book")
if a>10 or a==30 and a<30 :
    print ("you have to pay 5 rs for borrowing the book")
if (a>30) :
    print ("your membership has been cancelled ")
