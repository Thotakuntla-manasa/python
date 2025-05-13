my_list = [1, 2, 3, 4, 5]
print("First element:", my_list[0])
print("Last element:", my_list[-1])
my_list[2] = 10
print("Modified list:", my_list)
my_list.append(6)
print("List after appending:", my_list)
my_list.remove(10)
print("List after removing an element:", my_list)
print("Iterating through the list:")
for item in my_list:
    print(item)
squared_list = [x**2 for x in my_list]
print("Squared list:", squared_list)
