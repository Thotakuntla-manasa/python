def check_parentheses(n):
    left_count = n.count('(')
    right_count = n.count(')')
    if left_count == right_count:
        return 0
    else:
        return 1
n= "((a + b) * (c - d))"
s= check_parentheses(n)
print(f"s: {s}")
