"""Python Assignment: Student Record File Management
Objective

Create a Python program that manages student records using file I/O operations.

Problem Statement

Write a Python program that performs the following operations using a file named students.txt.

The program should display a menu to the user:
Add a new student record
View all student records
Exit

File Format
Each student record in the file should be stored as:

StudentID,Name,Age,Course


Example:
101,Rahul,20,Python
102,Anita,21,Data Science
103,Arjun,19,AI


Read the file.

Display all student records in a formatted way."""

from random import choice


def add_student():
    with open('students.txt', 'a') as f:  # append mode
        roll_no = int(input('Enter roll no: '))
        student = input('Enter student name: ')
        age = int(input('Enter student age: '))
        course = input('Enter course: ')

        # convert to string and proper format
        record = f"{roll_no},{student},{age},{course}\n"
        f.write(record)


def view_student():
    try:
        with open('students.txt', 'r') as f:
            data = f.readlines()
            print("\n--- Student Records ---\n")

            if not data:
                print("No records found.")

            for line in data:
                roll_no, student, age, course = line.strip().split(',')
                print(f"Roll No: {roll_no}, Name: {student}, Age: {age}, Course: {course}")

    except FileNotFoundError:
        print("File not found. No records yet.")


# --- menu ---
while True:
    print("\n1. Add a new record")
    print("2. View all records")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:  # fixed type
        view_student()
    elif choice == 3:
        print('Exiting...')
        break
    else:
        print("Invalid choice\n")