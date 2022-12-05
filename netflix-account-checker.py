import sys

print("-----------------------------------")
print("Netflix Account Profile")
print("-----------------------------------")

try:
  age = int(input("How old are you?\n: "))

except ValueError:
    print("ERROR: You can only enter numbers.")
    sys.exit(1)

print("-----------------------------------")
name = str(input("What's your username?\n: "))

if not name.replace(" ", '').isalpha():
    print("ERROR: You can only enter letters! (American letters).")
    sys.exit(1)

print("-----------------------------------")
location = str(input("Where do you reside?\n: "))

if not location.replace(" ", '').isalpha():
    print("ERROR: You can only enter letters! (American letters).")
    sys.exit(1)

print("-----------------------------------")
print("Profile:")
print("-----------------------------------")

if age <18: print("Age:",age,"Years Old (Kids Account).")
else: print("Age:",age,"Years Old (Adult Account).")

print("-----------------------------------")
print("Username:",name + ".")
print("-----------------------------------")
print("Location:",location + ".")
print("-----------------------------------")
