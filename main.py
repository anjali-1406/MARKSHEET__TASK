
from tables import create_table
from insert  import insert_student
from update import update_student
from update import Delete
from view import view_marksheet_by_roll

from marksheet import (
    get_student_details,
    get_marks,
    build_marksheet_data,
    print_marksheet
)

def main():

    create_table()

    while True:

        print("1. Add Student data ")
        print("2. Update ")
        print("3. View Marksheet")
        print("4. Delete")
        print("5. exit")

        choice = input("Enter choice: ")

        if choice == "1":

            student = get_student_details()
            theory, practical = get_marks()

            data = build_marksheet_data(student, theory, practical)

            insert_student(data)
            print_marksheet(data)

        elif choice == "2":
            update_student()

        elif choice == "3":
            view_marksheet_by_roll()

        elif choice == "4":
             Delete()
        elif choice == "5":
        	break 

        else:
            print("Invalid choice")

main()  