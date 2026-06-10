students = [
    ("Ram", 75),
    ("Hari", 92),
    ("Sita", 88),
    ("Gita", 95),
    ("Mohan", 80),
    ("Rita", 85),
    ("Suresh", 78),
    ("Anita", 90),
    ("Kiran", 82),
    ("Pooja", 87)
]

students.sort(key=lambda x: x[0], reverse=False)
print("Students sorted by marks (ascending):")
for student in students:
    print(student)