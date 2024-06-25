from database import create_connection

def add_instructor(first_name, last_name, email, phone_number, bio):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO Instructors (first_name, last_name, email, phone_number, bio) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (first_name, last_name, email, phone_number, bio))
    conn.commit()
    cursor.close()
    conn.close()

def update_instructor(instructor_id, first_name, last_name, email, phone_number, bio):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "UPDATE Instructors SET first_name = %s, last_name = %s, email = %s, phone_number = %s, bio = %s WHERE instructor_id = %s"
    cursor.execute(sql, (first_name, last_name, email, phone_number, bio, instructor_id))
    conn.commit()
    cursor.close()
    conn.close()

def remove_instructor(instructor_id):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "UPDATE Instructors SET is_deleted = 1 WHERE instructor_id = %s"
    cursor.execute(sql, (instructor_id,))
    conn.commit()
    cursor.close()
    conn.close()

def assign_instructor(course_id, instructor_id):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO CourseInstructors (course_id, instructor_id) VALUES (%s, %s)"
    cursor.execute(sql, (course_id, instructor_id))
    conn.commit()
    cursor.close()
    conn.close()
