age=int(input("please enter your age:"))
if age<0:
    print("you have not borned yet!")
if age>0 and age<=12:
    print("you are child")
if age>12 and age<=19:
    print("your are teenager")
if age>19 and age<40:
    print("you are a young one")
if age>=40:
    print("your are old man")
