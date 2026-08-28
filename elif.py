marks=int(input("enter student marks : "))

if(marks>=80):
    print("grade:A")
elif(marks<90 and marks>=80):
    print("grade:B")  
elif(marks<80 and marks>=70):
    print("grade :c")
elif(marks<70 ):
    print("grade:D")
else:
    print("FAIL")
    print("grade : F")
