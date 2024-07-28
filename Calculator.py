
d='Y'
print(" CALCULATOR PROGRAM ")
while((d=='Y')or(d=='y')):
    d='N'
    a=int(input("\nEnter the first operand :"))
    b=int(input("\nEnter the second operand:"))
    c=input("\nEnter the operation to be done :\n1)Addition(+) \n2)Substraction(-) \n3)Multiplication (*) \n4)Division (/) \n5)Remainder (%)\n")
    print(" \nThe operation to be done :  ",a,c,b)
    match c:
        case '+':
            print( "\n ",a,c,b,"=",a+b)
        case '-':
             print("\n",a,c,b,"=",a-b)
        case '/':
            print("\n",a,c,b,"=",a/b)
        case '*':
            print("\n",a,c,b,"=",a*b)
        case '%':
             print("\n",a,c,b,"=",a%b)
        case '_':
            print("\nInvalid operation!!!")
    d=input("\nDo you want to continue? [Y/N]")
print("\nCalculation Completed !!!")
