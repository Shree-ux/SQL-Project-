from database import create_connection

def add_student(first_name, last_name, email, phone_number, date_of_birth):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO Students (first_name, last_name, email, phone_number, date_of_birth) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (first_name, last_name, email, phone_number, date_of_birth))
    conn.commit()
    cursor.close()
    conn.close()

def enroll_student(student_id, course_id):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO Enrollments (student_id, course_id) VALUES (%s, %s)"
    cursor.execute(sql, (student_id, course_id))
    conn.commit()
    cursor.close()
    conn.close()

def track_progress(student_id, course_id):
    conn = create_connection()
    cursor = conn.cursor()
    sql = """
    SELECT a.assessment_name, g.score
    FROM Grades g
    JOIN Assessments a ON g.assessment_id = a.assessment_id
    WHERE g.student_id = %s AND a.course_id = %s AND g.is_deleted = 0 AND a.is_deleted = 0
    """
    cursor.execute(sql, (student_id, course_id))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
