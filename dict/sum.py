def sum_of_elements(lst):
    total = 0
    for number in lst:
        total += number
    return total

# Example usage
numbers = [1, 2, 3, 4, 5]
print("The sum of all elements in the list is:", sum_of_elements(numbers))
