def analyze_result(name, roll, marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print("\n===== STUDENT REPORT =====")
    print("Name:", name)
    print("Roll Number:", roll)
    print("Marks:", marks)
    print("Total Marks:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print("\nSubjects Below 40:")
    found = False
    for i in range(len(marks)):
        if marks[i] < 40:
            print(f"Subject {i+1}: {marks[i]}")
            found = True

    if not found:
        print("None")

name = "Vaishnavi"
roll = 58
marks = [95.0, 88.5, 76.0, 39.0, 90.0]

analyze_result(name, roll, marks)