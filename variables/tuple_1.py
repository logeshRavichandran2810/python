# roll_number=(121,122,123,124,125,126,127,128,129,130)
# mixed_type=('Loki',123,True,78.90)
# print(type(roll_number))
# print(type(mixed_type))
# print(len(roll_number))
# print(len(mixed_type))
# print(mixed_type[0])
# print(mixed_type[2])
# print(mixed_type[-3:-1])
# print(roll_number[-7:-4])

# print(type(()))

employee_details=('loki','Admin','Triner',True,123)
(name,*role,roll_no)=employee_details
print(employee_details)
print("name : ",name)
print("role : ",role)
print("roll no : ",roll_no)
