from marksheet import get_marks, calculate_result
from connection import get_connection

def update_student():

    roll_no = input("Enter Roll No: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM marksheet WHERE roll_no=%s",
        (roll_no,)
    )

    row = cur.fetchone()

    if not row:
        print("Student Not Found")
        return

    name = input("New Name: ")
    father_name = input("New Father Name: ")
    dob = input("New DOB (YYYY-MM-DD): ")
    school_name = input("New School Name: ")

    theory_marks, practical_marks = get_marks()

    total, percentage, grade, result = calculate_result(
        theory_marks,
        practical_marks
    )

    cur.execute("""
    UPDATE marksheet
    SET student_name=%s,
        father_name=%s,
        dob=%s,
        school_name=%s,
        hindi=%s,
        english=%s,
        business_studies=%s,
        accountancy_theory=%s,
        accountancy_practical=%s,
        economics_theory=%s,
        economics_practical=%s,
        total=%s,
        percentage=%s,
        grade=%s,
        result=%s
    WHERE roll_no=%s
    """, (
        name,
        father_name,
        dob,
        school_name,

        theory_marks[0],
        theory_marks[1],
        theory_marks[2],

        theory_marks[3],
        practical_marks[3],

        theory_marks[4],
        practical_marks[4],

        total,
        percentage,
        grade,
        result,

        roll_no
    ))

    conn.commit()

    print("Student Updated Successfully")

    cur.close()
    conn.close()

    
# def Delete():
#     roll = input("Enter Roll No: ")

#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute(" DELETE FROM marksheet WHERE roll_no=%s", (roll,))

#     conn.commit()
#     cur.close()
#     conn.close()

#     print("deleted")

def Delete():

    roll_no = input("Enter Roll No: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM marksheet WHERE roll_no=%s",
        (roll_no,)
    )

    if cur.rowcount == 0:
        print("Student Not Found")
    else:
        conn.commit()
        print("Student Deleted Successfully")

    cur.close()
    conn.close()