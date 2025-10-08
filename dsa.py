# create list
# empty = []
# letters = ["a", "b", "c", "d"] # this is a list of objects 
# print(type(empty))
# print(type(letters))

# unpacking a list
person = ["John", 25, 33,  "New York"]
name, *_, city = person # *age is a list of all the ages
print(name, city) # it skipped the ages
# more standard name, *details
# only one asterisk per list

