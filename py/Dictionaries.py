
# 1. Create a dictionary called student_record with the following information:

# add students

student_records = {
    "student_001": {
        "name": "John",
        "age": 19,
        "major": "Computer Science",
        "grades": [85, 92, 78]
    },
    "student_002": {
        "name": "Sarah",
        "age": 20,
        "major": "Biology",
        "grades": [90, 88, 95]
    }
}

# Add student_003
student_records["student_003"] = {
    "name": "Mike",
    "age": 18,
    "major": "Math",
    "grades": [82, 79, 91]
}

# Update umur john 20
student_records["student_001"]["age"] = 20

# Print each student's info in required format
for student_id, info in student_records.items():
    print(f"Student ID: {student_id}, Name: {info['name']}, Major: {info['major']}")
