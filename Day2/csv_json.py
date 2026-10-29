
import csv
import json

students = []

# Read CSV file
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append({
            "name": row["name"],
            "marks": int(row["marks"])
        })

# Calculate summary
total_students = len(students)

average_marks = sum(student["marks"] for student in students) / total_students

topper = max(students, key=lambda student: student["marks"])

summary = {
    "total_students": total_students,
    "average_marks": average_marks,
    "topper": topper["name"],
    "highest_marks": topper["marks"]
}

# Write JSON file
with open("summary.json", "w") as file:
    json.dump(summary, file, indent=4)

print("CSV data processed successfully!")
print(summary)
