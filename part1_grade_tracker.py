# Part 1 - Python Basics & Control Flow
# Theme: Student Grade Tracker

# ---- Task 1: Data Parsing & Profile Cleaning ----

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students: list[dict[str, object]] = []

print("=" * 32)
print("TASK 1 - Data Parsing & Cleaning")
print("=" * 32)

for student in raw_students:
    # fix name spacing and case
    clean_name: str = str(student["name"]).strip().title()
    # roll stored as string, convert to int
    clean_roll: int = int(str(student["roll"]))
    # split "88, 72" into [88, 72]
    clean_marks: list[int] = [int(x) for x in str(student["marks_str"]).split(", ")]

    cleaned: dict[str, object] = {
        "name":  clean_name,
        "roll":  clean_roll,
        "marks": clean_marks,
    }
    cleaned_students.append(cleaned)

    # check every word is alphabetic
    is_valid: bool = all(word.isalpha() for word in clean_name.split())
    validity: str = "✓ Valid name" if is_valid else "✗ Invalid name"
    print(validity, "—", clean_name)

    # profile card
    print("================================")
    print(f"Student : {clean_name}")
    print(f"Roll No : {clean_roll}")
    print(f"Marks   : {clean_marks}")
    print("================================")

# print roll 103 name in upper and lower
print("\nRoll 103 name in UPPER and lower:")
for s in cleaned_students:
    if s["roll"] == 103:
        name_103: str = str(s["name"])
        print(name_103.upper())
        print(name_103.lower())


# ---- Task 2: Marks Analysis ----

student_name: str   = "Ayesha Sharma"
subjects: list[str] = ["Math", "Physics", "CS", "English", "Chemistry"]
marks: list[int]    = [88, 72, 95, 60, 78]

print("\n" + "=" * 40)
print("TASK 2 - Marks Analysis")
print("=" * 40)

# grade each subject
print(f"\nGrades for {student_name}:")
for subject, mark in zip(subjects, marks):
    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"
    print(f"  {subject:<12}: {mark}  ->  {grade}")

# totals and averages
total: int     = sum(marks)
average: float = round(total / len(marks), 2)
highest_mark: int    = max(marks)
lowest_mark: int     = min(marks)
highest_subject: str = subjects[marks.index(highest_mark)]
lowest_subject: str  = subjects[marks.index(lowest_mark)]

print(f"\nTotal Marks   : {total}")
print(f"Average Marks : {average}")
print(f"Highest       : {highest_subject} — {highest_mark}")
print(f"Lowest        : {lowest_subject} — {lowest_mark}")

# while loop to add new subjects
print("\n--- Add New Subjects (type 'done' to stop) ---")
new_count: int = 0

while True:
    subj: str = input("Enter subject name (or 'done' to stop): ").strip()
    if subj.lower() == "done":
        break
    try:
        entered: str = input(f"Enter marks for {subj} (0-100): ")
        m: int = int(entered)
        if 0 <= m <= 100:
            subjects.append(subj)
            marks.append(m)
            new_count += 1
        else:
            print("Warning: marks must be 0-100, not added.")
    except ValueError:
        print("Warning: not a number, not added.")

print(f"\nNew subjects added : {new_count}")
print(f"Updated average    : {round(sum(marks) / len(marks), 2)}")


# ---- Task 3: Class Performance Summary ----

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("\n" + "=" * 40)
print("TASK 3 - Class Performance Summary")
print("=" * 40)

# compute average and result for each student
student_results: list[dict[str, object]] = []
for stu_name, stu_marks in class_data:
    avg_val: float  = round(sum(stu_marks) / len(stu_marks), 2)
    status_val: str = "Pass" if avg_val >= 60 else "Fail"
    student_results.append({"name": stu_name, "avg": avg_val, "status": status_val})

# print table
print(f"\n{'Name':<18}| {'Average':^7} | Status")
print("-" * 40)
for r in student_results:
    r_name: str   = str(r["name"])
    r_avg: float  = float(str(r["avg"]))
    r_status: str = str(r["status"])
    print(f"{r_name:<18}|  {r_avg:^5}  | {r_status}")

# summary
passed_count: int  = sum(1 for r in student_results if r["status"] == "Pass")
failed_count: int  = len(student_results) - passed_count
topper_entry       = max(student_results, key=lambda r: float(str(r["avg"])))
topper_name: str   = str(topper_entry["name"])
topper_avg: float  = float(str(topper_entry["avg"]))
all_avgs: list[float] = [float(str(r["avg"])) for r in student_results]
class_avg: float   = round(sum(all_avgs) / len(all_avgs), 2)

print(f"\nPassed    : {passed_count}")
print(f"Failed    : {failed_count}")
print(f"Topper    : {topper_name} — {topper_avg}")
print(f"Class Avg : {class_avg}")


# ---- Task 4: String Manipulation ----

essay: str = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

print("\n" + "=" * 40)
print("TASK 4 - String Manipulation")
print("=" * 40)

# step 1: strip spaces
clean_essay: str = essay.strip()

# step 2: title case
print("\nTitle Case:")
print(clean_essay.title())

# step 3: count 'python'
py_count: int = clean_essay.count("python")
print(f"\n'python' appears : {py_count} time(s)")

# step 4: replace python
replaced: str = clean_essay.replace("python", "Python")
print("\nAfter replacement:")
print(replaced)

# step 5: split into sentences
sentences: list[str] = clean_essay.split(". ")
print("\nSentences list:")
print(sentences)

# step 6: print numbered sentences
print("\nNumbered sentences:")
for i, sentence in enumerate(sentences, 1):
    final_sentence: str = sentence if sentence.endswith(".") else sentence + "."
    print(f"{i}. {final_sentence}")


'''
Output:
================================
TASK 1 - Data Parsing & Cleaning
================================
✓ Valid name — Ayesha Sharma
================================
Student : Ayesha Sharma
Roll No : 101
Marks   : [88, 72, 95, 60, 78]
================================
✓ Valid name — Rohit Verma
================================
Student : Rohit Verma
Roll No : 102
Marks   : [55, 68, 49, 72, 61]
================================
✓ Valid name — Priya Nair
================================
Student : Priya Nair
Roll No : 103
Marks   : [91, 85, 88, 94, 79]
================================
✓ Valid name — Karan Mehta
================================
Student : Karan Mehta
Roll No : 104
Marks   : [40, 55, 38, 62, 50]
================================
✓ Valid name — Sneha Pillai
================================
Student : Sneha Pillai
Roll No : 105
Marks   : [75, 80, 70, 68, 85]
================================

Roll 103 name in UPPER and lower:
PRIYA NAIR
priya nair

========================================
TASK 2 - Marks Analysis
========================================

Grades for Ayesha Sharma:
  Math        : 88  ->  A
  Physics     : 72  ->  B
  CS          : 95  ->  A+
  English     : 60  ->  C
  Chemistry   : 78  ->  B

Total Marks   : 393
Average Marks : 78.6
Highest       : CS — 95
Lowest        : English — 60

--- Add New Subjects (type 'done' to stop) ---
Enter subject name (or 'done' to stop): history
Enter marks for history (0-100): 98
Enter subject name (or 'done' to stop): biology
Enter marks for biology (0-100): 32
Enter subject name (or 'done' to stop): done

New subjects added : 2
Updated average    : 74.71

========================================
TASK 3 - Class Performance Summary
========================================

Name              | Average | Status
----------------------------------------
Ayesha Sharma     |  78.6   | Pass
Rohit Verma       |  61.0   | Pass
Priya Nair        |  87.4   | Pass
Karan Mehta       |  49.0   | Fail
Sneha Pillai      |  75.6   | Pass

Passed    : 4
Failed    : 1
Topper    : Priya Nair — 87.4
Class Avg : 70.32

========================================
TASK 4 - String Manipulation
========================================

Title Case:
Python Is A Versatile Language. It Supports Object Oriented, Functional, And Procedural Programming. Python Is Widely Used In Data Science And Machine Learning.    

'python' appears : 2 time(s)

After replacement:
Python is a versatile language. it supports object oriented, functional, and procedural programming. Python is widely used in data science and machine learning.    

Sentences list:
['python is a versatile language', 'it supports object oriented, functional, and procedural programming', 'python is widely used in data science and machine learning.']

Numbered sentences:
1. python is a versatile language.
2. it supports object oriented, functional, and procedural programming.
3. python is widely used in data science and machine learning.
'''