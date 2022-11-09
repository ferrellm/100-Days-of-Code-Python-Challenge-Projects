#Average height calculator

#Split the number of heights input into seperate values in a list called "student_heights"
student_heights = input("Input a list of student heights ").split()

#Assign "n" variable to each number between 0 and the number of heights input
for n in range(0, len(student_heights)):
    #Convert each height input from a string to an integer
  student_heights[n] = int(student_heights[n])

total_height = 0
#assigns "height" variable to each item in "student_heights" list
for height in student_heights:
  #A loop telling python to add each "height" value to the current "total_height" value until the list is complete
  total_height += height


total_students = 0
for students in student_heights:
  #A loop adding "+1" to the total_students variable for each item in the list
  total_students += 1

average_height = round(total_height / total_students)
print(average_height)