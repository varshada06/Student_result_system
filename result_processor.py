import csv

with open('students.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Name'], row['Maths'], row['Science'], row['English'])

INPUT_FILE = "students.csv"
OUTPUT_FILE = "final_results.csv"


def calculate_grade(percentage):
    if percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"


def process_results():
    students = []

    with open(INPUT_FILE, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                maths = int(row['Maths'])
                science = int(row['Science'])
                english = int(row['English'])

                total = maths + science + english
                percentage = total / 3
                grade = calculate_grade(percentage)
                status = "Pass" if grade != "Fail" else "Fail"

                students.append({
                    "RollNo": row['RollNo'],
                    "Name": row['Name'],
                    "Total": total,
                    "Percentage": round(percentage, 2),
                    "Grade": grade,
                    "Status": status
                })

            except ValueError:
                print(f"Invalid data for RollNo {row['RollNo']}")

    return students


def save_results(students):
    with open(OUTPUT_FILE, mode='w', newline='') as file:
        fieldnames = ["RollNo", "Name", "Total", "Percentage", "Grade", "Status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for student in students:
            writer.writerow(student)


def display_summary(students):
    print("\n--- RESULT SUMMARY ---")
    total_students = len(students)
    passed = sum(1 for s in students if s['Status'] == "Pass")
    failed = total_students - passed

    topper = max(students, key=lambda x: x['Percentage'])

    print(f"Total Students: {total_students}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Topper: {topper['Name']} ({topper['Percentage']}%)")


def main():
    students = process_results()
    save_results(students)
    display_summary(students)
    print("\nResults saved to final_results.csv")


if __name__ == "__main__":
    main()
