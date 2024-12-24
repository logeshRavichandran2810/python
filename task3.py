foods=['burger','veg pizza','momos','chinese','garlic bread','french fries','non-veg pizza']
print("Food available at restaurent : ",foods)
print("Data type of food : ",type(foods))
print("Total food Items : ",len(foods))
foods.append('kabab')
print("add one more item : ",foods)
print("Total food Items : ",len(foods))
print("Food at present not available : ",foods[2:5])
del foods[2:5]
print("Foods available: ",foods)