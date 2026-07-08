a=float(input("Enter First Number"))
operator=input ("operator(+,-,*,/)")
b=float( input ("Enter Second Number"))
if operator=="+":
    result=a+b
elif operator=="-":
    result=a-b 
elif operator=="*":
    result=a*b
elif operator=="/":
    result=a/b
else:
    result="error"
print("Javab:",result)