# lists
# score = 50
# submitted_project = True

# if score >= 90:
#     if submitted_project:
#         print("A+")
#     else:
#         print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

# email validation

# email = ""
# allowed_tlds = ('.com', '.org', '.net')


# if email != "":
#     if "@" in email and "." in email:
#         if email.count("@") == 1:
#             if email.lower().endswith(allowed_tlds):
#                 if len(email) < 255: 
#                     if email[0].isalnum() and email[-1].isalnum(): 
#                         print("Valid email")
#                     else:
#                         print("Invalid email")
#                 else:
#                     print("Invalid email")
#             else:
#                 print("Invalid email")
#         else:
#             print("Invalid email")
#     else:
#         print("Invalid email")
# else:
#     print("Invalid email")

# # password validation
# password = ""

# if password == "":
#     print("Invalid password")
# elif len(password) < 8:
#     print("Invalid password")
# elif password.upper() == password:
#     print("Invalid password")
# elif password.lower() == password:
#     print("Invalid password")
# elif password.isdigit() == password:
#     print("Invalid password")
# elif password.isalpha() == password:
#     print("Invalid password")
# else: 
#     print("Valid password")

# one line 
score = 85
# if score >= 90:
#     print("A")
# else: 
#     print("B")

grade ="A" if score >= 90 else "B"
print(grade)