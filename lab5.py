#write a python code that takes alist of number and 
# returns the largest and second largest number value .ensure the code hanedles lists with duplicate value correctly?

numbers = [10,20,20,5,30,30,15]

largest=None
second_largest=None
for num in numbers:
    if largest is None or num > largest:
        second_largest = largest
        largest = num
    elif num != largest and (second_largest is None or num > second_largest):
        second_largest = num

print("Largest number:", largest)
print("Second largest number:", second_largest)