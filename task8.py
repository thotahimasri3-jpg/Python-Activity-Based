days = int(input("Enter number of days in the month: "))
start = int(input("Enter starting weekday (0=Mon, 1=Tue, ..., 6=Sun): "))

print("\n MON  TUE  WED  THU  FRI  SAT  SUN")

# Print spaces for days before the starting weekday
for i in range(start):
    print("    ", end="")

# Display calendar dates
for day in range(1, days + 1):
    print("%4d" % day, end="")

    if (start + day) % 7 == 0:
        print()

print()