# print("hello faizyab")
# print("hello talha")

# def greet(name):
#     print(f"hello {name}")

# greet("faizyab")


# def number():
#     num = int(input("Enter any number: "))
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# number()
# number()


# def user(name,age,gender):
#     print(f"Hello {name}")
#     print(f"your {age}")
#     print(f"your {gender}")

# n= input("Enter your name: ")
# a=int(input("Enter your age: "))
# g= input("Enter your gender: ")


# user(n,a,g )


# def add(n1,n2):
#     print(n1+n2)

# num1= int(input("Enter your first number: "))
# num2= int(input("Enter your second number: "))

# add(num1,num2)




# def add(n1,n2,n3):
#     print(n1+n2+n3)
#     # return n1+ n2+n3

# # num1= int(input("Enter your first number: "))
# # num2= int(input("Enter your second number: "))
# # num3= int(input("Enter your Third number: "))

# ans = add(10,30,50)
# # add(30,60,90)
# print(ans)



# def can_vote(age):
#     if age>18:
#         return True
#     else:
#         return False

# ans = can_vote(20)
# print(can_vote(17))
# print(ans)




# def user(name,age):
#     return f"{name}, {age}"
#     print("hello")

# ans = user("faizyab",12)

# print(ans)


# def is_prime(num):
#     count = 0
#     for i in range(1,num+1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         return True
#     return False


# print(is_prime(17))

# que

# def square(num):
#     return num*num

# print(square(20))


# question

# def mid_num(n1,n2,n3):
#     if n1 < n2 and n1<n3:
#         return n1
#     elif n2 < n1 and n2<n3:
#         return n2
#     return n3

# print(mid_num(23,34,64))


# question

# build in function for abslutoe value like - wali + mai hujatai 



# def absu(num):
#     if num>=0:
#         return num
#     return num * -1

# ans = absu(-44)
# print(ans)
# print(absu(34))


# defult argu

# def calculate(math,eng,comp,urdu=0):
#     print(f" Math score =  {math}")
#     print(f" Eng score =  {eng}")
#     print(f" Computer score =  {comp}")
#     print(f" urdu score =  {urdu}")

#     total = math + eng+ comp+urdu
#     print(f" total score =  {total}")


# calculate(12,34,45)



# def calculate(math,eng,comp,urdu=0):
#     print(f" Math score =  {math}")
#     print(f" Eng score =  {eng}")
#     print(f" Computer score =  {comp}")
#     print(f" urdu score =  {urdu}")

#     total = math + eng+ comp+urdu
#     print(f" total score =  {total}")


# calculate(comp= 90, urdu= 78 , math= 56,eng=78)



# lamda 


# def square(n):
#     return n*n

# ans = lambda n: n*n

# print(ans(12))
# print(square(12))


# def adult(age):
#     if age >= 18:
#         return True
#     return False

# is_adult=lambda age: True if age>= 18 else False

# print(is_adult(20))
# print(adult(17))


# def number(num):
#     if num%3 == 0 :
#         return "Fizz"
#     if num%5 == 0 :
#             return "buzz"
#     if num%3 == 0 and num%5 :
#             return "Fizzbuzz"
#     return num

# print(number(7))

