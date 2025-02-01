full_name = input("Enter your full name: ")

parts = full_name.split(" ")

len(parts)>=2
first_name = parts[0][0].upper() 
last_name = parts[-1][0].upper()

print("Your initials are: " + first_name+"."+ last_name)
