# Gradebook CLI

## Project Description

Gradebook CLI is a small command-line application built with Python for managing students, courses, enrollments, and grades.

The application stores data in a JSON file and supports:

* adding students
* adding courses
* enrolling students in courses
* adding grades
* listing students, courses, and enrollments
* computing course averages
* computing a student's GPA

This project was developed to practice Python fundamentals such as OOP, file I/O, exception handling, modular programming, logging, testing, and command-line interfaces with `argparse`.

---

## Implemented Features

### Core Models

The file `gradebook/models.py` contains the following classes:

* `Student`
* `Course`
* `Enrollment`

These classes include basic validation and helper methods such as `to_dict()`.

---

### JSON Persistence

The file `gradebook/storage.py` handles loading and saving data in `data/gradebook.json`.

---

### Business Logic

The file `gradebook/service.py` contains the main operations:

* adding students and courses
* enrolling students
* adding grades
* listing stored data
* computing average and GPA

---

### Command-Line Interface

The file `main.py` provides a CLI using `argparse` with the following commands:

* `add-student`
* `add-course`
* `enroll`
* `add-grade`
* `list`
* `avg`
* `gpa`

---

### Logging

The application uses the `logging` module and writes logs to:

```text
logs/app.log
```

---

## Unit Tests

The file `tests/test_service.py` contains unit tests using `unittest`.

---

## Sample Data

The file `scripts/seed.py` generates sample students, courses, enrollments, and grades.

---

## Project Structure

```text
gradebook_project/
│
├── main.py
├── README.md
│
├── gradebook/
│   ├── __init__.py
│   ├── models.py
│   ├── storage.py
│   └── service.py
│
├── data/
│   └── gradebook.json
│
├── logs/
│   └── app.log
│
├── scripts/
│   └── seed.py
│
└── tests/
    └── test_service.py
```

---

## How to Run on Mac

### 1. Open Terminal and go to the project folder

```bash
cd ~/Desktop/gradebook_project
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Run the seed script

```bash
python3 scripts/seed.py
```

### 4. Run example commands

```bash
python3 main.py list students --sort name
python3 main.py list courses --sort code
python3 main.py list enrollments
python3 main.py avg --student-id 1 --course CS101
python3 main.py gpa --student-id 1
```

---

## Running Tests

```bash
python3 -m unittest discover tests
```

---

## Design Decisions and Limitations

* JSON was used instead of a database for simplicity.
* The project is separated into modules for cleaner structure.
* GPA is calculated as the simple mean of course averages.
* The application is designed for small-scale CLI usage.

---

## Deliverable

The final deliverable includes:

- source code
- README
- sample data
- tests
- GitHub repository link

---

## Expected Output Examples

```text
Listing Students:
{'id': 1, 'name': 'Ali Veli'}
{'id': 2, 'name': 'Ayse Yilmaz'}
{'id': 3, 'name': 'Mehmet Demir'}

Course Average:
Average: 85.00

Student GPA:
GPA: 85.00

---

Developed as part of a Python CLI system project.
