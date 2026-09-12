""" กระดานหมากรุก """
# รับค่า
size = int(input())

# แสดงผล
for row in range(1, size+1):
    for col in range(1, size+1):
        if col == size:
            if (row+col) % 2 == 0:
                print("O")
            else:
                print("X")
        else:
            if (row+col) % 2 == 0:
                print("O", end=" ")
            else:
                print("X", end=" ")
