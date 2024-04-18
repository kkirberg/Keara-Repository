from student import Student

student1 = Student("Keara", "Kirberger", 12898)
student2 = Student("Jane", "Doe", 13500, 8)
student3 = Student("Jack", "Jones", 23400, 6)

print(student1)
print(student2)
print(student3)
print()

student1.greeting("Hello!")
student2.greeting("Hey")
student1.take_exam()
print(student1.get_energy_level())
print(student2.get_energy_level())
print(student3.get_energy_level())