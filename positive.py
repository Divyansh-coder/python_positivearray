num=[]
enter=True #boolean value
#While loop for input
while enter:
    num.append(int(input("Enter any random integer number: ")))
    print("Enter another number (Y/N)")
    choice=input().upper()
    if choice=="N":
        enter=False
for n in num:
    if n<0:
        num.remove(n)  #removes negative value
print("List of positive numbers:",num)
