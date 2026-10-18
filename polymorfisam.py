print(1+2)
print("anshu"+"mandal") #this is the string concatination 
print([1,2,3,4]+[5,6,7]) #merge



class complex:
    def __init__(self, real, img):
      self.real = real
      self.img = img

    def show_number(self):
      print(self.real, "i+", self.img, "j") 
    def add(self,num2):
        return complex(self.real + num2.real, self.img + num2.img)


num1=complex(2,3)
num1.show_number()
num2=complex(4,5)
num2.show_number()
num3=num1.add(num2)
num3.show_number()