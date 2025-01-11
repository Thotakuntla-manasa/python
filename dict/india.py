f = 'india.txt'  # Specify the file name

try:
    # Attempt to open the file in read mode
    with open(f, 'r') as file:
        lines = file.readlines()  # Read all lines from the file
        print(lines)  # Print the lines read from the file

except FileNotFoundError:
    # Handle the case where the file is not found
    print(f"Error: The file '{f}' was not found.")

