#RECURSIVE FUNCATION 
a=123
def show(n):
    if(n==0):   # this is the condition line to stop the recursion when the value  of n is equal to 0
        return
    show(n-1)
    print(n)

show(5)