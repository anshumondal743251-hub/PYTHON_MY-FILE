# class student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

                                            #(this is the 1st problem where we do change the valu of student marks that will
                                            #  never show me the updeted valu and naever calculate the new value )
# stu1 = student(90, 80, 70)
# print(stu1.percentage)


# in this new problem we can craet the new trick that will help me to update the valu of percentages :


class student:
    def __init__(self, math, phy, chem):
        self.math = math
        self.phy = phy
        self.chem = chem
        self.percentages = str((self.math +self.phy+ self.chem)/3) + "%"

        @property
        def _percentages(self):
            return str((self.math + self.phy + self.chem) / 3) + "%"


stu1 = student(90, 80, 70)
print(stu1.percentages)      #this part will be show the result when it is not updated



stu1.math = 100
print(stu1.math)      #this part will be show the result when it is not updated

stu1.math = 100
print(stu1.math)      #this part will be show the result when it is updated
print(stu1.percentages)      #this part will be show the result when it is updated