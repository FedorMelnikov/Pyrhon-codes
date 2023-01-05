students = int(input("How many students are registering? "))
# Creating a for loop that runs for that amount of students
# Each time the loop runs it needs to ask the next student to enter their ID
# number.
f = open('ref_form.txt', 'a+')
for i in range (students):
    id = int(input("Enter your ID number: "))
    f.write("The ID:" + str(id) + "\n" + "Your signature:" + "\n" + "\n" + "............." + "\n" + "\n")
f.close()
# with open('ref_form.txt', 'a+') as f: