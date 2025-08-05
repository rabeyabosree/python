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


import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>~`[\]\\\/'=_+-]", password) is None

    if length_error:
        return "❌ Weak: Password should be at least 8 characters long."
    
    errors = []
    if digit_error:
        errors.append("a number")
    if uppercase_error:
        errors.append("an uppercase letter")
    if lowercase_error:
        errors.append("a lowercase letter")
    if symbol_error:
        errors.append("a symbol")

    if errors:
        return f"❌ Weak: Add {' ,'.join(errors)} to make your password stronger."
    
    return "✅ Strong password!"

def main():
    pwd = input("Enter your password to check strength: ")
    result = check_password_strength(pwd)
    print(result)

if __name__ == "__main__":
    main()
