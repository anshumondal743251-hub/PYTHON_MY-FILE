numbers=[1,2,3,4,5]
for i in range(len(numbers)):
    if numbers[i]%2==0:
        numbers[i]=numbers[i]*2
    else:
        numbers[i]=numbers[i]
print(numbers)

