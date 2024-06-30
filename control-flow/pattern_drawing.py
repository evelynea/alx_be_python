size = int(input("Enter the size of the pattern: "))
i = 0
while i < size:
    for y in range(0, size):
        print ("*", end="")
    i = i + 1
    print()