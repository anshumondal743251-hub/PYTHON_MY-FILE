
# #wap in python to find the sum of digits of a number?
# A=int(input("enter the number here"))

# sum=0
# while(A>0):
#     sum=sum+A%10
#     A=A//10

# print("the sum of the numbers is :",sum)



#take a number from user and reverse it and print the reverse number

# a=int(input("enter the number here:"))
# rev=0
# while(a>0):
#    p=a%10
#     rev=rev*10+p
#     a=a//10
#     print("the reverse of the number is :",rev)

#

##take a number from user and check it palindrome or not ?

# a=int(input("enetr the number here:"))  
# rev=0
# b=a
# while(a>0):
#     p=a%10
#     rev=rev*10+p
#     a=a//10
# if(b==rev):
#     print("the number is palindrome")
# else:
#     print("the number is not palindrome")


# wap in pyhton to take a number from user and count the no of digits in it?


# a=int(input("etnter the number here:"))
# count=0
# while(a>0):
#     a=a//10
#     count=count+1
# print("the number of digits in the number is :",count)


#wap in python to take two number from user to calculate the gcd and lcm of two numbers?





a=int(input("enter the first number here:"))
b=int(input("enter the second number here:"))

while(b!=0):
    t=a%b
    a=b
    b=t
    gcd=a
    lcm=(a*b)/gcd
    



print("the gcd of the two numbers is :",gcd)
print("the lcm of the two numbers is:", lcm)