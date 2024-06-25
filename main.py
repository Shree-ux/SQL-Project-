import courses
import instructors
import students
import assessments

def main():
    while True:
        print("Welcome to EduSchema!")
        print("1. Course Management")
        print("2. Instructor Management")
        print("3. Student Enrollment")
        print("4. Assessment and Grades")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            manage_courses()
        elif choice == '2':
            manage_instructors()
        elif choice == '3':
            manage_students()
        elif choice == '4':
            manage_assessments()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_courses():
    while True:
        print("\nCourse Management")
        print("1. Add Course")
        print("2. Update Course")
        print("3. Remove Course")
        print("4. Search Courses")
        print("5. Sort Courses")
        print("6. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            course_name = input("Course Name: ")
            course_description = input("Course Description: ")
            start_date = input("Start Date (YYYY-MM-DD): ")
            end_date = input("End Date (YYYY-MM-DD): ")
            courses.add_course(course_name, course_description, start_date, end_date)
        elif choice == '2':
            course_id = int(input("Course ID: "))
            course_name = input("Course Name: ")
            course_description = input("Course Description: ")
            start_date = input("Start Date (YYYY-MM-DD): ")
            end_date = input("End Date (YYYY-MM-DD): ")
            courses.update_course(course_id, course_name, course_description, start_date, end_date)
        elif choice == '3':
            course_id = int(input("Course ID: "))
            courses.remove_course(course_id)
        elif choice == '4':
            keyword = input("Search Keyword: ")
            results = courses.search_courses(keyword)
            for row in results:
                print(row)
        elif choice == '5':
            order_by = input("Order by (course_name/start_date/end_date): ")
            results = courses.sort_courses(order_by)
            for row in results:
                print(row)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_instructors():
    while True:
        print("\nInstructor Management")
        print("1. Add Instructor")
        print("2. Update Instructor")
        print("3. Remove Instructor")
        print("4. Assign Instructor to Course")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            email = input("Email: ")
            phone_number = input("Phone Number: ")
            bio = input("Bio: ")
            instructors.add_instructor(first_name, last_name, email, phone_number, bio)
        elif choice == '2':
            instructor_id = int(input("Instructor ID: "))
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            email = input("Email: ")
            phone_number = input("Phone Number: ")
            bio = input("Bio: ")
            instructors.update_instructor(instructor_id, first_name, last_name, email, phone_number, bio)
        elif choice == '3':
            instructor_id = int(input("Instructor ID: "))
            instructors.remove_instructor(instructor_id)
        elif choice == '4':
            course_id = int(input("Course ID: "))
            instructor_id = int(input("Instructor ID: "))
            instructors.assign_instructor(course_id, instructor_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_students():
    while True:
        print("\nStudent Enrollment")
        print("1. Add Student")
        print("2. Enroll Student in Course")
        print("3. Track Student Progress")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            email = input("Email: ")
            phone_number = input("Phone Number: ")
            date_of_birth = input("Date of Birth (YYYY-MM-DD): ")
            students.add_student(first_name, last_name, email, phone_number, date_of_birth)
        elif choice == '2':
            student_id = int(input("Student ID: "))
            course_id = int(input("Course ID: "))
            students.enroll_student(student_id, course_id)
        elif choice == '3':
            student_id = int(input("Student ID: "))
            course_id = int(input("Course ID: "))
            results = students.track_progress(student_id, course_id)
            for row in results:
                print(row)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_assessments():
    while True:
        print("\nAssessment and Grades")
        print("1. Create Assessment")
        print("2. Input Grade")
        print("3. View Grades")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            course_id = int(input("Course ID: "))
            assessment_name = input("Assessment Name: ")
            max_score = int(input("Max Score: "))
            assessment_date = input("Assessment Date (YYYY-MM-DD): ")
            assessments.create_assessment(course_id, assessment_name, max_score, assessment_date)
        elif choice == '2':
            student_id = int(input("Student ID: "))
            assessment_id = int(input("Assessment ID: "))
            score = int(input("Score: "))
            assessments.input_grade(student_id, assessment_id, score)
        elif choice == '3':
            student_id = int(input("Student ID: "))
            results = assessments.view_grades(student_id)
            for row in results:
                print(row)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
