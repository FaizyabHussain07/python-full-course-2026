name = input("Enter your name ")
marks = int(input("Enter your marks "))


if marks >= 90 and marks <=100:
    print(f"Your grade is A")
elif marks >= 80 and marks <=89:
    print(f"Your grade is A+")
elif marks >= 70 and marks <=79:
    print(f"Your grade is B+")
elif marks >= 60 and marks <=69:
    print(f"Your grade is B")
elif marks >= 50 and marks <=59:
    print(f"Your grade is C")
else:
    print(f"You are Fail")


print(f"Here's your name= {name}")
print(f"Here's your marks= {marks}")
