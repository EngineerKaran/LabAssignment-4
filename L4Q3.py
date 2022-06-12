print("\nWelcome to the Program")
import random
print("\nGenerating 10 random questions for you to solve...")
for i in range(10):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    print("Question number ",i+1," : ")
    print("What is ",num1,"x",num2," ?")
    ans = int(input("Kindly Enter your answer : "))
    if ans == (num1*num2):
        print("Right!")
    else:
        print("Wrong.The right answer is ",num1*num2)
    print("\n")