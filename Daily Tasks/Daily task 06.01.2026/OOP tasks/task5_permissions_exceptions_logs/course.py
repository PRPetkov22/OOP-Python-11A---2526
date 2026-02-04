from exceptions import (
    PermissionDeniedError,
    NotEnrolledError,
    CapacityError,
    DuplicateEntityError
)
from admin import Admin
from teacher import Teacher

class Course:
    def __init__(self, title, teacher, logger):
        self.title = title
        self.teacher = teacher
        self.logger = logger
        self.students = []

    def add_student(self, actor, student):
        if not isinstance(actor, (Teacher, Admin)):
            self.logger.log(f"**DENIED**: {actor.name} tried to add {student.name} to {self.title}")
            raise PermissionDeniedError("Only Teacher or Admin can add students.")

        if len(self.students) >= 30:
            self.logger.log(f"*FAIL*: course {self.title} is full")
            raise CapacityError("Course is full (max 30 students).")

        for s in self.students:
            if s.name == student.name and s.grade == student.grade:
                self.logger.log(f"*FAIL*: duplicate student {student.name} grade {student.grade} in {self.title}")
                raise DuplicateEntityError("Duplicate student (same name + grade).")

        self.students.append(student)
        self.logger.log(f"OK: {actor.name} added {student.name} to {self.title}")

    def remove_student(self, actor, student):
        if not isinstance(actor, (Teacher, Admin)):
            self.logger.log(f"**DENIED**: {actor.name} tried to remove {student.name} from {self.title}")
            raise PermissionDeniedError("Only Teacher or Admin can remove students.")

        if student in self.students:
            self.students.remove(student)
            self.logger.log(f"OK: {actor.name} removed {student.name} from {self.title}")

    def set_grade(self, actor, student, grade):
        is_admin = isinstance(actor, Admin)
        is_course_teacher = isinstance(actor, Teacher) and actor == self.teacher

        if not (is_admin or is_course_teacher):
            self.logger.log(f"**DENIED**: {actor.name} tried to grade in {self.title}")
            raise PermissionDeniedError("Only the course Teacher or Admin can set grades.")

        if student not in self.students:
            self.logger.log(f"*FAIL*: tried grading not enrolled student {student.name} in {self.title}")
            raise NotEnrolledError("Student is not enrolled in this course.")

        if grade < 2 or grade > 6:
            raise ValueError("Grade must be between 2 and 6.")

        student.add_grade_for_me(self.title, grade)

        self.logger.log(f"OK: {actor.name} gave {grade} to {student.name} in {self.title}")