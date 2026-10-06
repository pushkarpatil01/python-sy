# 0 = Available , 1 = Reserved

bus = [
[0, 0, 1, 0],
[1, 0, 0, 0],
[0, 1, 0, 1],
[0, 0, 0, 0]
]

print("===== BUS SEAT LAYOUT =====")

for row in bus: 
    for seat in row:
if seat == 0:
print("Available", end=" | ") 
else:
print("Reserved ", end=" | ") 
print()
row = int(input("\nEnter row number (1-4): "))
seat = int(input("Enter seat number (1-4): "))

row_index = row - 1 
seat_index = seat - 1
if bus[row_index][seat_index] == 0:
     bus[row_index][seat_index] = 1 
     print("Seat reserved successfully!")
else:
     print("Sorry! Seat is already reserved.")

print("\n===== UPDATED BUS SEAT LAYOUT =====")
for i in range(len(bus)):
for j in range(len(bus[i])):
     if bus[i][j] == 0:
print("Available", end=" | ") else:
print("Reserved ", end=" | ") print()
