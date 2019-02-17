input_set=[]
input_num=0
while(input_num>=0):
    input_num=int(input("Enter a number or-1 to finish:"))
    if(input_num<0):
        break
    input_set.append(input_num)
print(input_set)
largest=input_set[0]
for i in range(len(input_set)):
    if input_set[i]>largest:
        greatest=input_set[i]
print("largest number is.",greatest)
smallest=input_set[0]
for i in range(len(input_set)):
    if input_set[i]<largest:
        smallest=input_set[i]
print("smallest number is.",smallest)
