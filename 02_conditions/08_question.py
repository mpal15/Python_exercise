password = "secure3pages"

if len(password) <6:
    strength = "Weak"
elif len(password) <=10:
    strength = "Medium"
else:
    strength = "Strong"


print("password strength",strength)