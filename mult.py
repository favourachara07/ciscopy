# Print the header row
print("  ", end="")
for i in range(1, 11):
    print(f"{i:2d}", end=" ")
#print()

# Print the separator row
#print("  ", end="")
#for i in range(1, 11):
 #   print("--", end=" ")
print()

# Print the rest of the rows
for i in range(1, 11):
    print(f"{i:2d}|", end=" ")
    for j in range(1, 11):
        print(f"{i*j:2d}", end=" ")
    print()
