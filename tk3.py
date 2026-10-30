total_classes = int(input("Enter total number of classes: "))
attended_classes = int(input("Enter attended classes: "))

# Calculate attendance percentage
percentage = (attended_classes / total_classes) * 100

print("Attendance Percentage:", round(percentage, 2), "%")

# Check attendance
if percentage >= 75:
    print("You have reached 75% attendance.")
else:
    # Calculate additional classes needed
    needed = 0
    while ((attended_classes + needed) / (total_classes + needed)) * 100 < 75:
        needed += 1

    print("Additional consecutive classes needed:", needed)
    print("Attend", needed, "more classes to reach 75%.")