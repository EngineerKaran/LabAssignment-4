print("\nWelcome to the Program")
year = int(input("Kindly enter a year : "))
if year % 4 == 0 :
    print("The entered year is a Leap Year")
elif year % 100 == 0 :
    print("The entered year is not a Leap Year")
elif year % 400 == 0 :
    print("The entered year is a Leap Year")
else :
    print("The entered year is not a Leap Year")