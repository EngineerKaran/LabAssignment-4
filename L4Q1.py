print("\nWelcome to the Program")
marks = int(input("Kindly enter the marks : "))
if ( marks < 25 ):
    print("\nGrade = F")
elif ( marks >= 25 and marks < 45 ):
    print("\nGrade = E")
elif ( marks >= 45 and marks < 50 ):
    print("\nGrade = D")
elif ( marks >= 50 and marks < 60 ):
    print("\nGrade = C")
elif( marks >= 60 and marks < 80 ):
    print("\nGrade = B")
elif( marks >= 80 ):
    print("\nGrade = A")
else:
    print("\nNo result")