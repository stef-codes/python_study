# student = {
#     "name": "John",
#     "age": 25,
#     "city": "New York", 
#     "courses": ["Math", "Science", "History"]
# }

# student["state"] = "California"

# student.update({"name": "Jane", "age": 26, "city": "Los Angeles"})

# for key, value in student.items():
#     print(key, value)

# del student["city"]

# state = student.pop("state")

# print(state)

# print(student.get("name", "not found"))

#how many keys in the dictionary
# print(len(student))

# print(student.keys())

# print(student.values())

# print(student.items())

# print(student)

# Example 5: Word counter (MOST IMPORTANT PATTERN)
# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# print(word_count)  # {"apple": 3, "banana": 2, "orange": 1}

# Count how many times each letter appears in "hello world"
# text = "hello world"
# letter_count = {}
# # Your code here
# for char in text:
#     if char in letter_count:
#         letter_count[char] += 1
#     else:
#         letter_count[char] = 1
# print(letter_count)
# Expected: {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}

# names = ["Alice", "Bob", "Charlie"]
# phones = ["555-1234", "555-5678", "555-9012"]

# phone_book = {}

# for i in range(len(names)):
#     phone_book[names[i]] = phones[i]

# print(phone_book["Bob"])

# scores = [85, 90, 85, 78, 90, 85, 92]

# score_count = {}

# for i in scores:
#     if i in score_count:
#         score_count[i] += 1
#     else:
#         score_count[i] = 1
# print(score_count)

students = {"Alice": 85, "Bob": 75, "Charlie": 90, "David": 78, "Eve": 92}

high_scores = {}

for name, score in students.items():
    if score > 80:
        high_scores[name] = score
print(high_scores)

