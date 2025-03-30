
# Read the number of students
n = int(input())

# Create an empty dictionary to store student data
student_marks = {}

# Read student records
for _ in range(n):
    # Split input into name and marks
    data = input().split()
    name = data[0]
    marks = list(map(float, data[1:]))  # Convert marks to float
    student_marks[name] = marks

# Read the query name
query_name = input()

# Calculate the average of the marks for the queried student
average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])

# Print the average with 2 decimal places
print("{:.2f}".format(average_marks))
