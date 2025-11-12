# 1. Store entries in a dictionary
attendance_data = {}

print("--- Start entering attendance ---")
print("(Type 'done' as the name when you are finished)")

while True:
    # 2. Input daily names and timestamps
    name = input("Enter student's name: ").strip().title()

    if name == 'Done':
        break # Exit the loop if user types 'done'

    timestamp = input(f"Enter timestamp for {name} (e.g., 09:05 AM): ").strip()

    # 3. Validate entries using control statements
    if not name or not timestamp:
        print("--> Error: Name or timestamp cannot be empty. Please try again.\n")
        continue # Ask for input again

    if name in attendance_data:
        print(f"--> Error: {name} has already been marked present.\n")
        continue # Ask for a different name

    # Add the valid entry to our dictionary
    attendance_data[name] = timestamp
    print(f"--> Success: {name} marked present at {timestamp}.\n")


# 4. Generate formatted attendance summaries
print("\n------------------------------")
print("   Daily Attendance Summary   ")
print("------------------------------")

if not attendance_data:
    print("No students were marked present today.")
else:
    print(f"Total Students Present: {len(attendance_data)}\n")
    # Loop through the dictionary to print each record
    for student, time in attendance_data.items():
        print(f"- {student}: {time}")