i=0
while i<=5:
    if(i==3):
        i=i+1
        continue #it is basically used to skip the current iteration and move to the next iteration of the loop
    print(i)      # it is the code to how to skip the number 3 in the out put 
    i=i+1

i=0
while i<=10:
    if(i%2==0):
        i=i+1
        continue  #it is the code of print the odd numbers between 1 to 10
    print(i)
    i=i+1          # to print the even numbers between 1 to 10 we have to change the conditio to if(i%2!=0)