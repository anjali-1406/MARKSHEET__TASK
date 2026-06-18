from connection import get_connection

def create_table():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS marksheet (
        roll_no VARCHAR(10) PRIMARY KEY,
        student_name VARCHAR(50),
        father_name VARCHAR(50),
        dob DATE,
        school_name VARCHAR(100),

        hindi INTEGER,
        english INTEGER,
        business_studies INTEGER,
        accountancy_theory INTEGER,
        accountancy_practical INTEGER,
        economics_theory INTEGER,
        economics_practical INTEGER,

        total INTEGER,
        percentage NUMERIC(5,2),
        grade VARCHAR(2),
        result VARCHAR(10)
    )
    """)

    conn.commit()
    cur.close()
    conn.close()