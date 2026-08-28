nums=(1,2,3,4,3,2,1)
x=4
i=0
while i<len(nums):
    if (nums[i]==x):
        print("FOUND AT INDEX ",i)
        break
    else:
        print("not  found at index")
        i+=1
        print ("end of loop ")


# i=0
# while i<=5:
#     if(i==3):
#         i=i+1
#         continue #it is basically used to skip the current iteration and move to the next iteration of the loop
#     print(i)
#     i=i+1

