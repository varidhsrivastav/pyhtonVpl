import arithmatic as ar
print("1. Arithmatic calculation")
print("2. Scientific calculation")
print("3. area calculation")
choice = int(input("Enter the choice 1,2,3: "))
if(choice==1):
    print("Enter 1 for add ")
    print("Enter 2 for sub ")
    print("Enter 3 for mul ")
    print("Enter 4 for div ")
    print("Enter 5 for floatdiv ")
    print("Enter 6 for mod ")
    archoice = int(input("Enter the choice 1,2,3: "))
    num1=int(input("Enter number 1 "))
    num2=int(input("Enter number 2 "))
    if(archoice==1):
        ar.add(num1,num2)
    elif(archoice==2):
        ar.sub(num1,num2)
    elif(archoice==3):
        ar.mul(num1,num2)
    elif(archoice==4):
        ar.div(num1,num2)
    elif(archoice==5):
        ar.floatdiv(num1,num2)
    elif(archoice==6):
        ar.mod(num1,num2)
elif(choice==2):
    
        