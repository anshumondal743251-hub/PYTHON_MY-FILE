#WAP IN PYTHON TO TAKE 10 ELEMENT  FROM USER IN A LIST ONE BY ONE?
# my_list=[]
# for i in range(10):
#     a=int(input("ENTER THE ELEMENT: "))
#     my_list.append(a)
# print("THE LIST IS:", my_list)


# WAP IN PYTHON TO PERFORM SUM OF ODD AND AND EVEN DIGITS WITH IN  A LIST?
# my_list = []
# for i in range(10):
#     a = int(input("ENTER THE ELEMENT: "))
#     my_list.append(a)
    
# sum_odd = 0
# sum_even = 0
# for num in my_list:
#     if num % 2 == 0:
#         sum_even += num
#     else:
#         sum_odd += num
# print("SUM OF ODD DIGITS:", sum_odd)
# print("SUM OF EVEN DIGITS:", sum_even)

# WAP IN PYTHON  TO MOVE ALL ZEROS AT THE END IN A LIST 
my_list = []
for i in range(10):
    a = int(input("ENTER THE ELEMENT: "))
    my_list.append(a)
    
zeros = []
non_zeros = []
for num in my_list:
    if num == 0:
        zeros.append(num)
    else:
        non_zeros.append(num)
my_list = non_zeros + zeros
print("THE LIST WITH ZEROS AT THE END IS:", my_list)