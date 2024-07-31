def reverse_string(s):
    return s[::-1]

def reverse_string_program():
    s = input("Enter a string: ")
    reversed_s = reverse_string(s)
    print(f"Reversed string: {reversed_s}")

reverse_string_program()
