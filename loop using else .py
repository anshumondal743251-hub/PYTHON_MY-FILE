# # for loop is using else statement 
# str="anshu mandal"
# for element in str:
#     print(element)
# else:                 # the else state ment is used to execute a block of code when the loop is finished iteration and loop is end 
#     print("loop is end")




# str = " apna collage "
# for char in str:
#     if char=='o':
#         print(" o is found ")
#         break  #the break state ment is used to exit the loop when a character is found and the loop is end 
#     print(char) # to print the chracter of string one by one..
# else: 
#     print("END")   #


# # using for 
# ## print the element  of the following list ( this is a  question )
    
# list=[1,4,9,16,25,36,49,64,81,100]
# for el in list:
#     print(el) #to print the element of the list one by one 

#SEARCH A NUMBEER X IN THIS TUPEL USING LOOP 
num=(1,4,9,16,25,36,49,64,81,100,49)
x=49
idx = 0
for el in num :
    if (el==x):
        print("number is found at index",idx)
        idx+=1
