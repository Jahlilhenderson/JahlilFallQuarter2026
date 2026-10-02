numberGrade = int(input("Enter Your Grade: "))

if(numberGrade >= 90):
    print("Your letter grade is: A")
elif(80 <= numberGrade < 89):
    print("Your letter grade is: B")
elif(70 <= numberGrade < 79):
    print("Your letter grade is: C")
elif(60 <= numberGrade < 69):
    print("Your letter grade is: D")
else:
    print("Your letter grade is: F")