from database import create_connection

def create_assessment(course_id, assessment_name, max_score, assessment_date):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO Assessments (course_id, assessment_name, max_score, assessment_date) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (course_id, assessment_name, max_score, assessment_date))
    conn.commit()
    cursor.close()
    conn.close()

def input_grade(student_id, assessment_id, score):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO Grades (student_id, assessment_id, score) VALUES (%s, %s, %s)"
    cursor.execute(sql, (student_id, assessment_id, score))
    conn.commit()
    cursor.close()
    conn.close()

def view_grades(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    sql = """
    SELECT c.course_name, a.assessment_name, g.score
    FROM Grades g
    JOIN Assessments a ON g.assessment_id = a.assessment_id
    JOIN Courses c ON a.course_id = c.course_id
    WHERE g.student_id = %s AND g.is_deleted = 0 AND a.is_deleted = 0 AND c.is_deleted = 0
    """
    cursor.execute(sql, (student_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
