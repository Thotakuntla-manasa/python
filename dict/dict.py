def check_key(dictionary, key):
    if key in dictionary:
        print(f"The key '{key}' exists in the dictionary with value: {dictionary[key]}")
    else:
        print(f"The key '{key}' does not exist in the dictionary")

# Example usage
dictionary = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
key_to_check = input("Enter a key to check: ")
check_key(dictionary, key_to_check)
