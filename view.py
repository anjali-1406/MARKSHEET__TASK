from connection import get_connection
from marksheet import print_marksheet

def view_marksheet_by_roll():

    roll = input("Enter Roll No: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM marksheet WHERE roll_no=%s", (roll,))
    row = cur.fetchone()

    if not row:
        print("Student Not Found")
        return

    data = {
         "roll_no" : row[0],
        "name": row[1],
        "father_name": row[2],
        "dob": row[3],
        "school_name": row[4],

        "theory_marks": [
            row[5],
            row[6],
            row[7],
            row[8],
            row[10]
        ],

        "practical_marks": [
            0,
            0,
            0,
            row[9],
            row[11]
        ],

        "total": row[12],
        "percentage": row[13],
        "grade": row[14],
        "result": row[15],
        "centre_no" : row[16],
        "school_no" : row[17],
        "serial_no" : row[18]
    }

    print_marksheet(data)

    cur.close()
    conn.close()