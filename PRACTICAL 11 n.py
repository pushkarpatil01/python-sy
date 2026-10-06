# O = Open, X = Reserved

seats = [
    ["O", "O", "O"],
    ["O", "O", "O"],
    ["O", "O", "O"]
]

print("===== MOVIE THEATRE SEATING =====")

for row in seats:
    print(" | ".join(row))

row = int(input("\nEnter row number (1-3): "))
column = int(input("Enter column number (1-3): "))

row_index = row - 1
column_index = column - 1

if 1 <= row <= 3 and 1 <= column <= 3:
    if seats[row_index][column_index] == "O":
        seats[row_index][column_index] = "X"
        print("Seat reserved successfully!")
    else:
        print("Sorry! Seat is already reserved.")
else:
    print("Invalid row or column. Please enter values from 1 to 3.")

print("\n===== UPDATED SEATING =====")

for row in seats:
    print(" | ".join(row))
