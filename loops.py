# items = "Python"
# for item in range(0,10,2):
#     print(f"Round {item}")

# scores = [100, 90, 80, 70, 60]
# total = 0
# for score in scores:
#     total += score 
#     print(f"Current total: {total}")
# print(f"Total: {total}")

# for i in range(1, 11):
#     print(f"7 x {i} = {7 * i}")

# # break and continue and pass
# names = ["John", "Jane", "", "Jill", "Jack"]

# for name in names:
#     if name == "":
#         print("empty value detected")
#         pass #todo: handle empty value
#     print(f"Name = {name}")

#check for even number
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers = [1, 3, 5, 7, 9]

# for num in numbers:
#     if num % 2 == 0:
#         print(f"Even number found: {num}")
#         break
# else: 
#     print("all numbers are odd")

# find duplicate file names
file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]

# for file in file_list:
#     if file_list.count(file) > 1: 
#         print("Duplicate found")
#         break
# else: 
#     print("All files are unique")

#nested loops
for x in (1, 2, 3): 
    for y in (1, 2): 
        print(x, y)