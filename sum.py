def sum_of_elements(lst):
    total = 0
    index = 0 
    while index < len(lst):
        total += lst[index]
        index += 1
    return total
numbers = [1, 2, 3, 4, 5]
result = sum_of_elements(numbers)
print(f"The sum of the elements in the list is: {result}")
