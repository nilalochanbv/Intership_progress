
import csv
import json
import numpy as np
import pandas as pd

students = []

# Step 1: Read CSV and validate records
try:
    with open("students.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                name = row["name"].strip()
                marks = int(row["marks"])

                if not name:
                    raise ValueError("Student name cannot be empty")

                if marks < 0 or marks > 100:
                    raise ValueError("Marks must be between 0 and 100")

                students.append({
                    "name": name,
                    "marks": marks
                })

            except (ValueError, TypeError) as error:
                print("Skipping invalid record:", row, "-", error)

except FileNotFoundError:
    print("Error: students.csv file not found!")
    raise SystemExit

# Step 2: Check whether valid records exist
if not students:
    print("No valid student records found!")
    raise SystemExit

# Step 3: Convert data into a Pandas DataFrame
df = pd.DataFrame(students)

# Step 4: Analyze marks using NumPy
marks_array = np.array(df["marks"])

average = float(np.mean(marks_array))
highest = int(np.max(marks_array))
lowest = int(np.min(marks_array))

# Step 5: Find the topper using Pandas
topper = df.loc[df["marks"].idxmax()]

# Step 6: Display the report
print("\n===== STUDENT PERFORMANCE REPORT =====")
print(df.to_string(index=False))

print("\nTotal Students:", len(df))
print("Average Marks:", round(average, 2))
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Topper:", topper["name"])

# Step 7: Export report to JSON
report = {
    "total_students": len(df),
    "average_marks": round(average, 2),
    "highest_marks": highest,
    "lowest_marks": lowest,
    "topper": topper["name"],
    "students": students
}

with open("student_report.json", "w") as file:
    json.dump(report, file, indent=4)

print("\nReport exported successfully to student_report.json")
