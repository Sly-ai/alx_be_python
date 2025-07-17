pattern = int(input("Enter the size of the pattern: "))
i = 1
print("Pattern Drawing:")

while i <= pattern :
    print("*", end="")
    i += 1
    for j in range(1,pattern):
        print("*",end="")
    print()


