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
# for x in (1, 2, 3): 
#     for y in (1, 2): 
#         print(x, y)

# for year in years: 
#     for month in months: 
#         for day in days: 
#             print(year, month, day.csv)

# for table in tables: 
#     for column in columnns: 
#         for row in rows: 
#             print("")

# Select count(*) from table_name where id IS NULL; 
# data quality check: find all the columns that have null values
# tables = ['users', 'orders', 'products']
# columns = ['id', 'name', 'email']
# for table in tables: 
#     for column in columns: 
#         print(f"Select count(*) from {table} where {column} IS NULL;")

# datalake 
# for c in containers: 
#     for b in buckets: 
#         for f in files: 
#             print("Do Something")

# while loop
# initialization = 0
# condition = True
# update += 1

# while false: 
# answer = ""
# while answer != "yes":
#     answer = input("Are you sure you want to continue? (yes/no): ")
# print("Thank you for your answer")

#while loop with break (true) -- riskier
attempts = 0
while attempts < 3:
    answer = input("Are you sure you want to continue? (yes/no): ")
    if answer == "yes":
        print("glad we're on the same page")
        break
    attempts += 1
else: 
    print("3 strikes and you're out")

