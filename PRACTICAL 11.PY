days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

schedule = [
["Math", "Science", "English", "History", "Computer"],
["English", "Math", "Science", "Computer", "History"],
["Computer", "History", "Math", "Science", "English"],
["Science", "Computer", "History", "Math", "Science"]
]

hours = ["9 AM", "10 AM", "11 AM", "12 PM"]

print("===== CLASS SCHEDULE =====")

print("Time | " + " | ".join(days))
print("-" * 60)

for i in range(len(schedule)):
print(hours[i] + " | " + " | ".join(schedule[i]))

day = int(input("\nEnter day number (1-5): "))
hour = int(input("Enter hour slot (1-4): "))

if 1 <= day <= 5 and 1 <= hour <= 4:
print("Current subject:", schedule[hour - 1][day - 1])

new_subject = input("Enter new subject/topic: ")

schedule[hour - 1][day - 1] = new_subject

print("Schedule updated successfully!")


else:
print("Invalid day or hour.")

print("\n===== UPDATED CLASS SCHEDULE =====")

print("Time | " + " | ".join(days))
print("-" * 60)

for i in range(len(schedule)):
print(hours[i] + " | " + " | ".join(schedule[i]))\
