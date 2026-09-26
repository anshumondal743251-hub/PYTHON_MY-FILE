# creat a new file "practice.text" usiing add the following data to it 
# Hi evertone// we are learning file i/o // using java// i like programming in java ;


# with open ("practice.text","w") as f:
#     f.write("Hi evertone\n we are learning file i/o \n using java\n i like programming in java ;")



with open ("practice.text","r") as f:
        data=f.read()
new_data=data.replace("java", 'python')
print(new_data)

with open ("practice.text","w") as f:
        f.write(new_data)