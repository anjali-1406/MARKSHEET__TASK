
import random
from datetime import datetime


def Grade(per):
    if per >= 75:
        return "A"
    elif per >= 60:
        return "B"
    elif per >= 45:
        return "C"
    elif per >= 33:
        return "D"
    else:
        return "F"


def generate_student_info():

    return {
        "centre_no": random.randint(100000, 999999),
        "school_no": random.randint(100000, 999999),
        "serial_no": random.randint(100000, 999999)
    }


def get_student_details():

    while True:
        name = input("Enter Your Name: ").strip()

        if name == "":
            print("Name cannot be empty")

        elif len(name) > 20:
            print("Name max 20 characters")

        elif all(ch.isalpha() or ch.isspace() for ch in name):
            break

        else:
            print("Invalid Name")

    while True:
        father_name = input("Enter Father Name: ").strip()

        if father_name == "":
            print("Father Name cannot be empty")

        elif len(father_name) > 20:
            print("Father Name max 20 characters")

        elif all(ch.isalpha() or ch.isspace() for ch in father_name):
            break

        else:
            print("Invalid Father Name")

    while True:

        try:
            dob = input("Enter DOB (YYYY-MM-DD): ")
            datetime.strptime(dob, "%Y-%m-%d")
            break

        except:
            print("Invalid Date Format")

    while True:

        school_name = input("Enter School Name: ").strip()

        if school_name == "":
            print("School Name cannot be empty")

        elif len(school_name) > 40:
            print("School Name max 40 characters")

        else:
            break

    while True:

        roll_no = input("Enter Roll Number: ")

        if roll_no.isdigit() and len(roll_no) <= 10:
            break

        print("Roll Number should contain only digits")

    return {
        "name": name,
        "father_name": father_name,
        "dob": dob,
        "school_name": school_name,
        "roll_no": roll_no
    }


def get_marks():

    subjects = [
        "Hindi",
        "English",
        "Business Studies",
        "Accountancy",
        "Economics"
    ]

    theory_marks = []
    practical_marks = []

    print("\nENTER MARKS\n")

    for sub in subjects:

        if sub in ["Accountancy", "Economics"]:

            while True:

                theory = int(input(f"{sub} Theory Marks (0-80): "))

                if 0 <= theory <= 80:
                    break

                print("Theory marks must be between 0 to 80")

            while True:

                practical = int(input(f"{sub} Practical Marks (0-20): "))

                if 0 <= practical <= 20:
                    break

                print("Practical marks must be between 0 to 20")

            theory_marks.append(theory)
            practical_marks.append(practical)

        else:

            while True:

                theory = int(input(f"{sub} Marks (0-100): "))

                if 0 <= theory <= 100:
                    break

                print("Marks must be between 0 to 100")

            theory_marks.append(theory)
            practical_marks.append(0)

    return theory_marks, practical_marks


def calculate_result(theory_marks, practical_marks):

    total = sum(theory_marks) + sum(practical_marks)

    percentage = (total / 500) * 100

    grade = Grade(percentage)

    failed = False

    for i in range(len(theory_marks)):

        subject_total = theory_marks[i] + practical_marks[i]

        if subject_total < 33:
            failed = True
            break

    result = "FAILED" if failed else "PASS"

    return total, percentage, grade, result


def build_marksheet_data(student, theory_marks, practical_marks):

    info = generate_student_info()

    total, percentage, grade, result = calculate_result(
        theory_marks,
        practical_marks
    )

    return {

        **student,

        **info,

        "theory_marks": theory_marks,
        "practical_marks": practical_marks,

        "total": total,
        "percentage": percentage,
        "grade": grade,
        "result": result
    }


def print_marksheet(data):

    subjects = [
        "Hindi",
        "English",
        "Business Studies",
        "Accountancy",
        "Economics"
    ]

    print("\n")
    print("+" + "-" * 85 + "+")
    print("|{:^85}|".format("BOARD OF SECONDARY EDUCATION, MADHYA PRADESH, BHOPAL"))
    print("|{:^85}|".format("HIGHER SECONDARY SCHOOL CERTIFICATE EXAMINATION (10+2)"))
    print("|{:^85}|".format("MARKSHEET CUM CERTIFICATE"))
    print("+" + "-" * 85 + "+")

    print("|{:^20}|{:^20}|{:^20}|{:^22}|".format(
        "CENTRE NO",
        "SCHOOL NO",
        "ROLL NO",
        "SERIAL NO"
    ))

    print("|{:^20}|{:^20}|{:^20}|{:^22}|".format(
        data["centre_no"],
        data["school_no"],
        data["roll_no"],
        data["serial_no"]
    ))

    print("+" + "-" * 85 + "+")

    print("| {:<84}|".format(f"NAME        : {data['name']}"))
    print("| {:<84}|".format(f"FATHER NAME : {data['father_name']}"))
    print("| {:<84}|".format(f"DOB         : {data['dob']}"))
    print("| {:<84}|".format(f"SCHOOL NAME : {data['school_name']}"))

    print("+" + "-" * 85 + "+")

    print("|{:<24}|{:^8}|{:^8}|{:^8}|{:^10}|{:^8}|{:^13}|".format(
        "SUBJECT",
        "MAX",
        "MIN",
        "THEORY",
        "PRACTICAL",
        "TOTAL",
        "REMARK"
    ))

    print("+------------------------+--------+--------+--------+----------+--------+-------------+")

    for i in range(len(subjects)):

        total_marks = data["theory_marks"][i] + data["practical_marks"][i]

        if total_marks >= 75:
            remark = "DISTIN"
        elif total_marks >= 33:
            remark = "PASS"
        else:
            remark = "FAIL"

        practical = data["practical_marks"][i]

        if practical == 0:
            practical = "-"

        print("|{:<24}|{:^8}|{:^8}|{:^8}|{:^10}|{:^8}|{:^13}|".format(
            subjects[i],
            100,
            33,
            data["theory_marks"][i],
            practical,
            total_marks,
            remark
        ))

    print("+------------------------+--------+--------+--------+----------+--------+-------------+")

    print("| {:<84}|".format(f"GRAND TOTAL : {data['total']}/500"))
    print("| {:<84}|".format(f"PERCENTAGE  : {data['percentage']:.2f}%"))
    print("| {:<84}|".format(f"GRADE       : {data['grade']}"))
    print("| {:<84}|".format(f"RESULT      : {data['result']}"))

    print("+" + "-" * 85 + "+")
def main():

    student = get_student_details()

    theory_marks, practical_marks = get_marks()

    data = build_marksheet_data(
        student,
        theory_marks,
        practical_marks
    )

    print_marksheet(data)


if __name__ == "__main__":
    main()