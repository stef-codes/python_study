nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = []

# for n in nums:
#     my_list.append(n)
# print(my_list)

# thing to do ----> the iteration 
# my_list = [n * n for n in nums]
# print(my_list)

# thing to do ----> the iteration (put evens in list)
# put the condition after the iteration if it's a filter
my_list = [n for n in nums if n % 2 == 0]
print(my_list)