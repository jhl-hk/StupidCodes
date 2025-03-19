#Write a program to track student grades. 
# The program should allow the user to input student names and grades, store them in a list, and then calculate the average grade.

students = []

while True:
    print("\nStudent Grade Tracker")
    print("1. Add Student")
    print("2. Calculate Average Grade")
    print("3. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter the student's name: ")
        grade = float(input("Enter the student's grade: "))
        students.append({"name": name, "grade": grade})
    elif choice == "2":
        if not students:
            print("No students added yet.")
        else:
            total_grade = sum(student["grade"] for student in students)
            average_grade = total_grade / len(students)
            print(f"\nTotal Students: {len(students)}")
            print(f"Average Grade: {average_grade:.2f}")
    elif choice == "3":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
        
