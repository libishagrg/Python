email = input("Enter your email: ")

at = email.index("@")

domain = email[at+1:]
print("Domain:", domain)