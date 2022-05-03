contacts = {
    "number":4,
    "students":[
        {"name":"Sarah Holderness", "email":"sarah@example.com"},
        {"name":"Pop Pip", "email":"pop@example.com"},
        {"name":"Bob Howard", "email":"bob@example.com"},
        {"name": "Vincent Gut", "email":"vincent@example.com"}
    ]
}

for student in contacts["students"]:
    print(student["email"])