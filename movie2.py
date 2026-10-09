rows = 5
cols = 8

# 0 = Available seat
# Other numbers = Group IDs
seats = [[0 for j in range(cols)] for i in range(rows)]

group_count = int(input("Enter number of groups: "))

groups = []

for i in range(group_count):
    print("\nGroup", i + 1)
    size = int(input("Enter group size: "))
    groups.append((i + 1, size))

# Allocate larger groups first to reduce unused seats
groups.sort(key=lambda x: x[1], reverse=True)

for group_id, size in groups:
    allocated = False

    # Find consecutive seats in the same row
    for i in range(rows):
        for j in range(cols - size + 1):
            available = True

            for k in range(size):
                if seats[i][j + k] != 0:
                    available = False
                    break

            if available:
                for k in range(size):
                    seats[i][j + k] = group_id

                allocated = True
                print("Group", group_id,
                      "allocated to Row", i + 1,
                      "Seats", j + 1, "to", j + size)
                break

        if allocated:
            break

    # If a group cannot fit in one row, use any available seats
    if not allocated:
        free_seats = []

        for i in range(rows):
            for j in range(cols):
                if seats[i][j] == 0:
                    free_seats.append((i, j))

        if len(free_seats) >= size:
            for k in range(size):
                i, j = free_seats[k]
                seats[i][j] = group_id

            print("Group", group_id,
                  "allocated using separated seats.")
        else:
            print("Group", group_id,
                  "could not be fully accommodated.")

# Display seating arrangement
print("\n--- THEATRE SEATING PLAN ---")
print("0 = Empty seat")

for i in range(rows):
    print("Row", i + 1, ":", end=" ")
    for j in range(cols):
        if seats[i][j] == 0:
            print("[ - ]", end=" ")
        else:
            print("[G" + str(seats[i][j]) + "]", end=" ")
    print()

# Calculate unused seats
unused = 0
booked = 0

for i in range(rows):
    for j in range(cols):
        if seats[i][j] == 0:
            unused += 1
        else:
            booked += 1

print("\nTotal seats:", rows * cols)
print("Booked seats:", booked)
print("Unused seats:", unused)