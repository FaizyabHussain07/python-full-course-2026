# # print heloo 10 time
# i = 1

# while i <= 5:
#     print("hello")
#     i += 1

# print(i)



# 1-10 print 
# 1-n print

# n = int(input("Enter number: "))

# i = 1

# while i <= n:
#     print(i ,end=" ")
#     i+=1

#  star and end by users 


# start = int(input("Enter start number: "))
# end = int(input("enter end number: "))

# i = start

# while i <= end:
#     print(i,end=" ")
#     i += 1

# print(f"\n After ending loop , start value is: {start}")


#  start to end print even 

# start = int(input("Enter start number: "))
# end = int(input("enter end number: "))

# i = start 

# while i <=end:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i+=1    
    
# print start to end  which are divisible by 3 and 4

# start = int(input("Enter start number: "))
# end = int(input("enter end number: "))

# i = start 

# while i <= end:
#     if i %3==0 and i%4==0:
#         print(i,end=" ")
#     i +=1    


#  end to start 10-1

# start = int(input("Enter start number: "))
# end = int(input("enter end number: "))

# i = 10

# while i>=1:
#     print(i,end=" ")
#     i-=1


# summ of 1-100

# start = int(input("Enter start number: "))
# end = int(input("enter end number: "))


# i =start
# total=0

# while i <=end:
#     total = total+i
#     i +=1

# print(f"total= {total}")



# start = int(input("Enter start number: "))
# end = int(input("enter end number: "))


# i =start
# total=0

# while i <=end:
#     if i %2==0 and i%7==0:
#         total = total+i
#     i +=1

# print(f"total= {total}")



#  make the 4 table


# num = int(input("Enter table number: "))
# i=1

# while i <= 10:
#     print(f"{num} X  {i} = {num*i}")
#     i+=1


#  print factor

# num = int(input("Enter number: "))
# i = 1
# count = 0
# while i<=num:
#     if num%i == 0:
#         print(i,end=" ")
#         count= count+1
#     i+=1

# print(f"\n total factor {num} are {count}")



# num = int(input("Enter number: "))
# i = 1
# while i<=num:
#     if num%i == 0:
#         print(i,end=" ")
        
#     i+=1



#  for loop


# for i in range(1,11):
#     print(i)

# # steps in loop 

# for i in range (-10,19,2):
#     print(i)



# # loop completed and break continue bhi


# # question 


# total = 0
# while  True:
#     num = int(input("Enter a number = "))
#     if num <0:
#         continue
#     if num == 0:
#         break
#     total +=num 

# print(total )



# nested loop 

# for i in range(1,4):
#     print(  f"i =   {i}")
#     for j in range(10,18):
#         print(f"j = {j}")


# nest loop mai patren like question han ju mainai class mai karliya thai ok

# mai apagi bahir rha hun ok


# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()

# for i in range(2,6):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()


# space patren

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


# for i in range(1,6):
#     for k in range (1,6-i):
#           print("@",end=" ")
#     for j in range(1,i+1):
#           print(j,end=" ")
#     print()



# for i in range(5,0,-1):
#     for k in range (1,i-1 +1):
#         print(" ",end=" ")
#     for j in range(5,i-1,-1):
#           print(j,end=" ")
#     print()



for i in range (1,6):
    for j in range (1,5-i+1):
        print(" ",end=" ")
    for k in range(1,(i*2)):
        print(k,end=" ")
    print()

for i in range (4,0,-1):
    for j in range (1,5-i+1):
        print(" ",end=" ")
    for k in range(1,(i*2)):
        print(k,end=" ")
    print()

