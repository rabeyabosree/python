# import re

# def check_password_strength(password):
#     length_error = len(password) < 8
#     digit_error = re.search(r"\d", password) is None
#     uppercase_error = re.search(r"[A-Z]", password) is None
#     lowercase_error = re.search(r"[a-z]", password) is None
#     symbol_error = re.search(r"[!#$%\'()*+,\-./\[\\\]^_`{|}~]",password) is None

#     if length_error:
#         return "Weak (password should be at least 8 characters)"
#     if digit_error or uppercase_error or lowercase_error or symbol_error:
#         return "Weak (Include uppercase, lowercase, number and symbol)"
#     return "strong password"

# def main():
#     pwd = input("Enter your password to check strength")

#     result = check_password_strength(pwd)
#     print(result)


# if __name__ == "__main__":
#     main()


# import re

# def check_password_strength(password):
#     length_error = len(password) < 8
#     digit_error = re.search(r"\d", password) is None
#     uppercase_error = re.search(r"[A-Z]", password) is None
#     lowercase_error = re.search(r"[a-z]", password) is None
#     symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>~`[\]\\\/'=_+-]", password) is None

#     if length_error:
#         return "❌ Weak: Password should be at least 8 characters long."
    
#     errors = []
#     if digit_error:
#         errors.append("a number")
#     if uppercase_error:
#         errors.append("an uppercase letter")
#     if lowercase_error:
#         errors.append("a lowercase letter")
#     if symbol_error:
#         errors.append("a symbol")

#     if errors:
#         return f"❌ Weak: Add {' ,'.join(errors)} to make your password stronger."
    
#     return "✅ Strong password!"

# def main():
#     pwd = input("Enter your password to check strength: ")
#     result = check_password_strength(pwd)
#     print(result)

# if __name__ == "__main__":
#     main()



# balance = 1500

# password = input("Enter your ATM password")

# if password =="1234":
#     print("\n Login successfully \n")
#     print("______ ATM MENU _____")
#     print("1. chacke balance")
#     print("2. withdrow balacne")
#     print("3. deposite money")
#     print("4. exist")

#     choise = input("choise an opntion (1/4)")

#     if(choise == "1"):
#         print(f"your current balance is : {balance}")
#     elif(choise == "2"):
#         amount = int(input("enter ammount to withdrow : "))
#         if amount <= balance :
#             balance -= amount
#             print(f"withdrow successfully remaining balance : {balance}")

#     elif(choise == "3"):
#         amount  =int( input("enter your amount to deposit : "))
#         balance += amount
#         print(f"deposite successfully. your updated amount is {balance}")
    
#     elif(choise == "4"):
#         print("thank you for ussing out AYM. goodbye")
    
#     else:
#         print("invalid option. please choose 1 to 4")

# else:
#     print("incorrect password. access denied")


# student = {}

# student['name'] = input("Enter student name")

# student['age'] = int(input("Enter age : "))

# student['class'] = input("Enter class : ")


# print("\n student information :")

# for key , value in student.items():
#     print(f"{key.capitalize()} : {value}")



# text = input("Enter a sentence : ").lower()

# words = text.split()

# freq = {}

# for word in words :
#     freq[word] = freq.get(word , 0 ) + 1

# print("\n word frequency")
# for word, count in freq.items():
#     print(f"{word} {count}")


# emails = ["ds@example.com", "bfhsd@example.com", "sdh@example.com" , "djf@example.com"]

# unique_emails = set(emails)

# print("Unique Emails : ")
# for email in emails :
#     print(email)



# user1_freind = {"sdfja", "fsdhkj", "fdskjf", "common"}

# user2_freind =  {"dsajkf", "dsafjsk", "slkfa", "common"}

# common = user1_freind.intersection(user2_freind)

# print('common freind :' , common)


# blog_posts = [
#     {"title" : "react" , "tags": ["code", "reat", "dev"]},
#     {"title" : "java" , "tags": ["code", "reat", "dev", "jsdh"]},
#     {"title" : "python" , "tags": ["code", "reat", "dev"]},
#     {"title" : "Ruby" , "tags": ["code", "reat", "dev"]}
# ]

# all_tags = set()

# for post in blog_posts:
#     all_tags.update(post["tags"])

# print("Total Unique Tags : ", len(all_tags))
# print("all tags", all_tags)


# try:
#     s = set()
#     s.add({"name": "rabeya"})

# except TypeError as e:
#     print("error", e)


students = {}

def add_student(name, age, grade):
    students[name] = {'age': age, grade: grade}


add_student("rabeya", 34, "11th")
add_student("rabeya", 34, "11th")
add_student("rabeya", 34, "11th")

print(students)

text = "pyrhon is easy and python is powerful"

words = text.split()

lenth = sum(len(word) for word in words)

total_length = 0

freq = {}

for word in words:
    for let in word:
        total_length += 1

print(total_length)
print(lenth)