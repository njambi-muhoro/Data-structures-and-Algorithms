# #  objects
# my_set = {1,2,3,4,5}
# shapes= set({"triangle","oval"})

# # adding an element to a set 
# shapes.add("circle")
# print(shapes)

# # checking for an element in a set
# 2 in my_set
# if 2 in my_set:
#     print("2 is present in my_set")
# else:
#     print("2 is not present in my_set")

# # removing a particular element
# my_set.remove(3)
# print(my_set)



# # adding multiple elements
# shapes.update({"box", "mango", "square"})
# print (shapes)

# #removing elements from the set - this raises an error if the element is not found
# shapes.remove("mango")
# print(shapes)

# #removing elements from the set
# shapes.discard("box")
# print(shapes)

# #removing the first element
# shapes.pop()
# print(shapes)

# #empty a set in python
# shapes.clear()
# print (shapes)

# # sets can be used to perform mathematical operations is performed using OR operator
# # joining two sets
# set1 = {1,2,3,4,5}
# set2={6,7,8,9,10}
#     #union operation
# union_set = set1 | set2
# print (union_set)

# #set intersection is performed using the AND operator - it is used to find the common element between two or more  sets
# set3 = {1,2,3,4,5,6}
# set4 = {5,6,7,8}
# intersection_set = set3 & set4
# print(intersection_set)

# #set difference - finds the elements in one set that are not in the other
# #returns a new set containing elements that are unique to the first set
# set6 = {1,2,3,4,5,6}
# set7 = {5,6,7,8}
# difference_set = set6 - set7
# print(difference_set)


#DICTIONARIES - ARE KEY VALE PAIRS (OBJECTS)
car = {"model":"mustang", "brand":"Ford", "year":1964}

#using the get method to access dictionary elements
print(car.get("model"))

#using the indexing method to access dictionary elements
print(car["brand"])

# changing the value of the key in a dictionary
car['year'] = 1967
print(car)

# adding a new key value pair
car['color'] = "red"
print(car)

#removing a key value pair
del car['color']
print(car)

# creating a nested dictionary
student_marks = {'Ram':{'math':80, 'science':80, 'Eng':80}, 'Brian':{'math':90, 'science':60, 'Eng':90}, 'Dom':{'math':95, 'science':93, 'Eng':98}}
print(student_marks)

# accessing values from a nested dictionary
print(student_marks['Ram']['math'])
print(student_marks['Brian'])

# adding key value pairs in a dictionary
student_marks['Brian']['swahili'] = 80
print(student_marks['Brian'])
# removing key value pairs in a dictionary
student_marks.pop('Ram')
print(student_marks)