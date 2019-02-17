age=int(input("please Enter your age:"))
if age<18:
    print("you are Minor")
    print("you are not Eligible to work")
else:
    if age>18 and age <=60:
        print("your are Eligibl to work")
        print("please fill your details and Apply")
    else:
        print("you are too old to work as per the government rules")
        print("please collect your pension")
        
