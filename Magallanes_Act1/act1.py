name=input("What is your name: ")
print("choose type of conversation")
print("1. Fahrenheit to Celsius")
print("2. Celsius to fahrenheit")
choice1=int(input("Enter 1 or 2: "))
tempinput=float(input("Enter Temperature: "))
if choice1==1:
    converted=(5/9)*(tempinput-32)
    print("hello,",name,"!",tempinput,"fahrenheit","is equal to",converted,"celsius")
if choice1==2:
    converted=(9/5)*(tempinput+32)
    print("hello,",name,"!",tempinput,"celsius","is equal to",converted,"fahrenheit")


