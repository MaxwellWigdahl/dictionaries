student = {
    "name": "Max Wigdahl",
    "age": 20,
    "major": "MIS",
    "hobbies": ["basketball", "soccer", "music"]
}

student["State"] = "NJ"
student["age"] += 1

for k, v in student():
    print(f"{k}: {v}")