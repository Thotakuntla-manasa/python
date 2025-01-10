# write a basic python program to demonstrate the use of lists in python

# Create a list with initial elements
my_list = [1, 2, 3, 4, 5]

# Access and print the first element of the list
print("First element:", my_list[0])

# Access and print the last element of the list using negative indexing
print("Last element:", my_list[-1])

# Modify the third element (index 2) of the list
my_list[2] = 10
print("Modified list:", my_list)

# Append a new element to the end of the list
my_list.append(6)
print("List after appending:", my_list)

# Remove the first occurrence of the element with value 10 from the list
my_list.remove(10)
print("List after removing an element:", my_list)

# Iterate through the list and print each element
print("Iterating through the list:")
for item in my_list:
    print(item)

# Create a new list with the squares of the elements in the original list using list comprehension
squared_list = [x**2 for x in my_list]
print("Squared list:", squared_list)
