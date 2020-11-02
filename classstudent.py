class Student:
    student_cnt=0
    grades_sum=0
    ages_sum=0
    def __init__(self,age,grade):
        self.age=age
        self.grade=grade

        Student.student_cnt+=1
        Student.grades_sum+=grade
        Student.ages_sum+=age

    @classmethod
    def grade_avg(cls):
        return cls.grades_sum/cls.student_cnt

    @classmethod
    def ages_avg(cls):
        return cls.ages_sum/cls.student_cnt

    def print_info(self):
        print(f"age: {self.age}, grade: {self.grade}")

Students=[
    Student(10,60),
    Student(15,70),
    Student(20,60),
    Student(25,70),
]

for Student in Students:
    Student.print_info()


print("grades_avg:",Student.grades_avg())
print("age_avg:",Student.ages_avg())
