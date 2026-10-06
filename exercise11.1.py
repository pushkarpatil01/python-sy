# Movie Theatre Booking Simulation

# Create a 3 x 3 seating grid
seats = [
    ['O', 'O', 'O'],
    ['O', 'O', 'O'],
    ['O', 'O', 'O']
]

print("Movie Theatre Booking System")

while True:
    # Display seating layout
    print("\nSeating Layout:")
    print("   1 2 3")

    for i in range(3):
        print(i + 1, " ", end="")
        for j in range(3):
            print(seats[i][j], end=" ")
        print()

    # Get row and column from user
    row = int(input("\nEnter row (1-3): "))
    col = int(input("Enter column (1-3): "))

    # Check whether the input is valid
    if row < 1 or row > 3 or col < 1 or col > 3:
        print("Invalid row or column. Please enter values from 1 to 3.")
        continue

    # Check seat status
    if seats[row - 1][col - 1] == 'X':
        print("Sorry! This seat is already reserved.")
    else:
        # Change O to X
        seats[row - 1][col - 1] = 'X'
        print("Seat reserved successfully!")

    # Ask if the user wants another booking
    choice = input("\nDo you want to book another seat? (y/n): ")

    if choice.lower() != 'y':
        break

# Display final seating arrangement
print("\nFinal Seating Layout:")
print("   1 2 3")

for i in range(3):
    print(i + 1, " ", end="")
    for j in range(3):
        print(seats[i][j], end=" ")
    print()

print("\nThank you for using the Movie Theatre Booking System!")
