import argparse
import logging

from gradebook.storage import load_data, save_data
from gradebook.service import (
    add_student,
    add_course,
    enroll,
    add_grade,
    list_students,
    list_courses,
    list_enrollments,
    compute_average,
    compute_gpa,
)


logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def parse_grade(value):
    """Parse and validate grade input from the command line."""
    try:
        grade = float(value)
    except ValueError as error:
        raise ValueError("Grade must be numeric.") from error

    if not 0 <= grade <= 100:
        raise ValueError("Grade must be between 0 and 100.")

    return grade


def main():
    """Run the Gradebook CLI application."""
    parser = argparse.ArgumentParser(description="Gradebook CLI")
    subparsers = parser.add_subparsers(dest="command")

    parser_add_student = subparsers.add_parser("add-student")
    parser_add_student.add_argument("--name", required=True)

    parser_add_course = subparsers.add_parser("add-course")
    parser_add_course.add_argument("--code", required=True)
    parser_add_course.add_argument("--title", required=True)

    parser_enroll = subparsers.add_parser("enroll")
    parser_enroll.add_argument("--student-id", required=True, type=int)
    parser_enroll.add_argument("--course", required=True)

    parser_add_grade = subparsers.add_parser("add-grade")
    parser_add_grade.add_argument("--student-id", required=True, type=int)
    parser_add_grade.add_argument("--course", required=True)
    parser_add_grade.add_argument("--grade", required=True)

    parser_list = subparsers.add_parser("list")
    parser_list.add_argument("target", choices=["students", "courses", "enrollments"])
    parser_list.add_argument("--sort", default=None)

    parser_avg = subparsers.add_parser("avg")
    parser_avg.add_argument("--student-id", required=True, type=int)
    parser_avg.add_argument("--course", required=True)

    parser_gpa = subparsers.add_parser("gpa")
    parser_gpa.add_argument("--student-id", required=True, type=int)

    args = parser.parse_args()
    data = load_data()

    try:
        if args.command == "add-student":
            student_id = add_student(data, args.name)
            save_data(data)
            print(f"Student added successfully. ID: {student_id}")

        elif args.command == "add-course":
            add_course(data, args.code, args.title)
            save_data(data)
            print("Course added successfully.")

        elif args.command == "enroll":
            enroll(data, args.student_id, args.course)
            save_data(data)
            print("Enrollment completed successfully.")

        elif args.command == "add-grade":
            grade = parse_grade(args.grade)
            add_grade(data, args.student_id, args.course, grade)
            save_data(data)
            print("Grade added successfully.")

        elif args.command == "list":
            if args.target == "students":
                items = list_students(data, args.sort or "name")
            elif args.target == "courses":
                items = list_courses(data, args.sort or "code")
            else:
                items = list_enrollments(data)

            for item in items:
                print(item)

        elif args.command == "avg":
            result = compute_average(data, args.student_id, args.course)
            print(f"Average: {result:.2f}")

        elif args.command == "gpa":
            result = compute_gpa(data, args.student_id)
            print(f"GPA: {result:.2f}")

        else:
            parser.print_help()

    except ValueError as error:
        logging.error("Application error: %s", error)
        print(f"Error: {error}")
    except Exception as error:
        logging.error("Unexpected error: %s", error)
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()