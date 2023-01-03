# Open the file
f = open('DOB.txt', 'r')

# Initialize variables
content = ""
dates = ""

# Loop over the file and make 2 lists
for line in f:
    content_list = line.split()
    dates_list = line.split()[2:]

    # Loop over the content and print it in different lines
    for i in content_list:
        if i != content_list[4]:
            content += i + " "
        else:
            content += i + " " + "\n"

    # Loop over the dates and print it in different lines
    for i in dates_list:
        if i != dates_list[2]:
            dates += i + " "
        else:
            dates += i + " " + "\n"

print(f"{content}")
print(f"{dates}")

characters = len(content)
print(f"The number of characters is {characters}")

words = len(content.split())
print ("The number of words in file are: " + str(words))

lines = content.count('\n')
print("The number of lines is " + str(lines))



count = 0
i = 0
for i in range(len(content)):
    if (
        (content[i] == "a")
        or (content[i] == "e")
        or (content[i] == "i")
        or (content[i] == "o")
        or (content[i] == "u")
    ):
        count += 1

print("Number of vowels in the given fail is: ", count)



f.close()