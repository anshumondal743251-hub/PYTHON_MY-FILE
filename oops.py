# class car:
#     color =' blue'
#     brand ='toyota'
# car1=car()
# print(car1.color)



class student:
     name='anshu'
     def _init_(self,full_name):
          self.full_name = full_name
          print(self)
          print("this is student class")

s1=student("anshu") 
print(s1.name) #it will print the object address of the class student because we have not defined a __str__ method