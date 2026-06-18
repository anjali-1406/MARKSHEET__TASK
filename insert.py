from connection import get_connection

def insert_student(data):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO marksheet VALUES (
        %s,%s,%s,%s,%s,
        %s,%s,%s,
        %s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s
    )
    """, (
        data["roll_no"],    
        data["name"],
        data["father_name"],
        data["dob"],
        data["school_name"],

        data["theory_marks"][0],
        data["theory_marks"][1],
        data["theory_marks"][2],

        data["theory_marks"][3],
        data["practical_marks"][3],

        data["theory_marks"][4],
        data["practical_marks"][4],

        data["total"],
        data["percentage"],
        data["grade"],
        data["result"],
        data["centre_no"],
        data["school_no"],
        data["serial_no"]

    ))

    conn.commit()
    cur.close()
    conn.close()