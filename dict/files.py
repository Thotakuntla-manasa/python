def count_file_stats(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            lines = content.count('\n') + 1
            words = len(content.split())
            characters = len(content)
            
            print(f"File: {filename}")
            print(f"Lines: {lines}")
            print(f"Words: {words}")
            print(f"Characters: {characters}")
    
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Example usage
filename = input("Enter the filename: ")
count_file_stats(filename)

