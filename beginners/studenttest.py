from Student import Student
from CSStudent import CSStudent

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)
student3 = Student("Oscar", "Accounting", 4.5, True)

print(student1.name)
print(student2.name)
print(
    f"Is {student1.name} on honor roll? {'Yes' if student1.on_honor_roll() else 'No'}"
)
print(
    f"Is {student3.name} on honor roll? {'Yes' if student3.on_honor_roll() else 'No'}"
)


cs_student1 = CSStudent("Bob", "AI", 3.1, False, "Java")
cs_student2 = CSStudent("Alice", "AI", 4.1, True, "Python")


print(
    f"Is {cs_student1.name} on honor roll? {'Yes' if cs_student1.on_honor_roll() else 'No'}"
)
print(
    f"Is {cs_student2.name} on honor roll? {'Yes' if cs_student2.on_honor_roll() else 'No'}"
)
