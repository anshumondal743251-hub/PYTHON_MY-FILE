# # #inheritance
# # class car:
# #     color = "red"

# #     @staticmethod
# #     def start():
# #         print("car started")

# #     @staticmethod
# #     def stop():
# #         print("car stopped")

# # class bmw(car):
# #     def __init__(self, model):
# #         self.model = model
# # car1 =bmw('x5')
# # print(car1.model)
# # print(car1.start())

# # how to use super in python ???
# class car:
#     def __init__(self, car_type, color):
#         self.type = car_type
#         self.color = color

#     @staticmethod
#     def start():
#         return "car started"

#     @staticmethod
#     def stop():
#         return "car stopped"


# class toyota(car):
#     def __init__(self, model, color):
#         super().__init__(model, color)      #in this line we can use the super class to access the parent class construct or control the parent class 


# car1 = toyota("sedan", "blue")
# print(car1.type)
# print(car1.color)
