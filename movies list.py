# While the string is not “John”, add every string entered to a list until “John”
# is entered. This program basically stores all incorrectly entered strings in a
# list where “John” is the only correct string.
# ● Print out the list of incorrect names.
# ● Example program run (what should show up in the Python Console when
# you run it):
# Enter your name : <user enters Tim>
# Enter your name : <user enters Mark>
# Enter your name: <user enters John>
# Incorrect names: [‘Tim’, ‘Mark’]
names = []
names1 = ""
while names1.upper() != "JOHN":
    names1 = input("Enter a name: ")
    if names1.upper() != "JOHN":
        names.append(names1)
print(f"Incorrect names are {names}")