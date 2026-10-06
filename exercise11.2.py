# Daily Class Schedule

# Create a 5 x 5 class schedule
# Rows = Time slots
# Columns = Days of the week

schedule = [
    ["Math", "Python", "AI", "English", "DS"],
    ["Python", "AI", "Math", "DS", "English"],
    ["AI", "DS", "English", "Python", "Math"],
    ["DS", "English", "Python", "Math", "AI"],
    ["English", "Math", "DS", "AI", "Python"]
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Display class schedule
print("===== DAILY CLASS SCHEDULE =====")

for i in range(len(schedule)):
    print("Time Slot", i + 1, ":", end=" ")
    for j in range(len(schedule[i])):
        print(days[j] + "-" + schedule[i][j], end=" | ")
    print()

# Accept row and column from user
row = int(input("\nEnter time slot (1-5): "))
column = int(input("Enter day number (1-5): "))

# Convert to list index
row_index = row - 1
column_index = column - 1

# Display selected subject
print("\nSelected Subject:",
      schedule[row_index][column_index])

# Overwrite subject
new_subject = input("Enter new subject: ")

schedule[row_index][column_index] = new_subject

# Display updated schedule
print("\n===== UPDATED CLASS SCHEDULE =====")

for i in range(len(schedule)):
    print("Time Slot", i + 1, ":", end=" ")
    for j in range(len(schedule[i])):
        print(days[j] + "-" + schedule[i][j], end=" | ")
    print()