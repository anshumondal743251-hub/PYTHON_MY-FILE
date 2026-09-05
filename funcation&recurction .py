 

def fact(n):
    if n == 0 or n== 1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(5))  # it is the code to find the factorial of a number using recursion