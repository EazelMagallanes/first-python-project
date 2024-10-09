age=int(input("Enter your age?"))
member=input("Are you a Fitness Member? yes or no?")
if age <=18 and member=="yes":
    print("Memeber fee is 450.00 pesos")
elif age <=18 and member=="no":
    print ("non-member fee is 600.00 pesos")
if age >=19 and age <=65 and member=="yes":
    print("Member fee is 550.00 pesos")
elif age >=19 and age <=65 and member=="no":
    print("Member fee is 750.00 pesos")
if age >=65 and age <=100 and member=="yes":
    print("Memeber fee is 400.00 pesos")
elif age >=65 and age <=100 and member=="no":
    print("Member fee is 600.00 pesos")