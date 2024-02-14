student = {
    "name": "Max Wigdahl",
    "age": 20,
    "major": "MIS",
    "hobbies": ["basketball", "soccer", "music"]
}

student["State"] = "NJ"

student["age"] += 1

for key, value in student.items():
    print(f"{key}: {value}")