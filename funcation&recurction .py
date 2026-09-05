from operator import index


def fact(n):
    if n == 0 or n== 1:
        return 1
    else:
        return n * fact(n - 1)  

print(fact(5))  # it is the code to find the factorial of a number using recursion


#write a recursive funcation to calculate the sum of first n natural numbers?
def calculate_sum(n):
    if n == 0:
        return 0
    else:
        return n + calculate_sum(n - 1)

print(calculate_sum(5))  # it is the code to calculate the sum of first 5 natural numbers using recursion


# wirte a recursive funcation to print all elements in a list ?
 def print_list_elements(lst, idx=0):
    if idx == len(lst):
        return
    print(lst[idx])
    print_list_elements(lst, idx + 1)

    fruits=["apple", "banana", "cherry", "date"]
    print_list_elements(fruits, 0)  # it is the code to print all elements in a list using recursion
