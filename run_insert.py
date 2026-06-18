from marksheet import (
    get_student_details,
    get_marks,
    build_marksheet_data
)

from insert  import insert_student

student = get_student_details()
theory_marks, practical_marks = get_marks()

data = build_marksheet_data(
    student,
    theory_marks,
    practical_marks
)

insert_student(data)

print("Data Inserted Successfully")