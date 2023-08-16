def calculate_gpa(grade):
    if grade == 'O':
        return 10
    elif grade == 'A+':
        return 9
    elif grade == 'A':
        return 8
    elif grade == 'B+':
        return 7
    elif grade == 'B':
        return 6
    else:
        return 0.0

def calculate_semester_gpa(grades, credit_hours):
    total_credit_points = 0
    total_credit_hours = 0

    for grade, credit in zip(grades, credit_hours):
        grade_points = calculate_gpa(grade)
        total_credit_points += grade_points * credit
        total_credit_hours += credit

    semester_gpa = total_credit_points / total_credit_hours
    return semester_gpa

def main():
    num_semesters = int(input(f"Enter the number of semester you want to calculate : "))
    total_cgpa = 0

    for i in range(1, num_semesters + 1):
        print(f"Semester {i}:")
        grades = []
        credit_hours = []

        for j in range(1, 7):  # Assuming 6 courses per semester
            grade = input(f"Enter grade for subject {j}: ").upper()
            credit = int(input(f"Enter credit for subject {j}: "))
            grades.append(grade)
            credit_hours.append(credit)

        semester_gpa = calculate_semester_gpa(grades, credit_hours)
        total_cgpa += semester_gpa

        print(f"Semester {i} GPA: {semester_gpa:.2f}\n")

    overall_cgpa = total_cgpa / num_semesters
    print(f"overall CGPA: {overall_cgpa:.2f}")

if __name__ == "__main__":
    main()
