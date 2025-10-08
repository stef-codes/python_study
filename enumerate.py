#enumerate is a function that returns the index and the element of the list
my_list = ["apple", "banana", "cherry", "date"]

for x, element in enumerate(my_list):
    print(x, element)
    if x % 2 == 0:
        print(f"{x} is even this is the {element}")
