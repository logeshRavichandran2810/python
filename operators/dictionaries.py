# # dictionary

# watch_details = {
# 'Titan':6000,
# 'Fastrack':4000,
# 'Sonata':2000,
# 'Noise':1000,
# 'Noise':500,
# }
# print(watch_details)
# print('Length : ',len(watch_details))
# print('Length : ',watch_details['Titan'])
# watch_details['Titan']=5000
# print(watch_details)
# watch_details['us polo']=8000
# print(watch_details)

employee_details={
    'name':'Logesh',
    'emp_id':4565,
    'is_active':True,
    'package':7.5
}
print('GET Method : ',employee_details.get('is_active'))
print('keys Method : ',employee_details.keys())
print(type(employee_details.keys()))
print('values Method : ',employee_details.values())
print(type(employee_details.values()))
print('items Method : ',employee_details.items())
print(type(employee_details.items()))
print('pop items Method : ',employee_details.popitem())
print(employee_details)
print('pop Method : ',employee_details.pop('is_active'))
print(employee_details)
print(employee_details.update({'package':8.0}))
print(employee_details.update({'role':'Developer'}))
print(employee_details.update({'role':' '}))
print(employee_details)