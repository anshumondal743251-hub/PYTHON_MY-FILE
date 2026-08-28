nums=(1,2,3,4,3,2,1)
x=3
i=0
while i<len(nums):
    if (nums[i]==x):
        print("FOUND AT INDEX ",i)
    else:
        print("not  found at index")
        i+=1