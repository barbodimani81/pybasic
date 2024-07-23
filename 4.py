def calculate_gpa(score):
    if score >= 18:
        return 'A'
    elif score >= 15:
        return 'B'
    elif score >= 12:
        return 'C'
    else:
        return 'F'


def main():
    # Get grades from the user
    grades = []
    for i in range(5):
        grade = float(input(f"Enter grade {i + 1}: "))
        if grade > 20:
            print("Grade Invalid")
            return
        grades.append(grade)

    # Calculate average
    average = sum(grades) / len(grades)

    # Convert average to GPA
    gpa = calculate_gpa(average)

    # Display GPA
    print(f"Average GPA: {gpa}")


if __name__ == "__main__":
    main()
