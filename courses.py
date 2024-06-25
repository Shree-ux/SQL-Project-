from database import create_connection

def add_course(course_name, course_description, start_date, end_date):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO Courses (course_name, course_description, start_date, end_date) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (course_name, course_description, start_date, end_date))
    conn.commit()
    cursor.close()
    conn.close()

def update_course(course_id, course_name, course_description, start_date, end_date):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "UPDATE Courses SET course_name = %s, course_description = %s, start_date = %s, end_date = %s WHERE course_id = %s"
    cursor.execute(sql, (course_name, course_description, start_date, end_date, course_id))
    conn.commit()
    cursor.close()
    conn.close()

def remove_course(course_id):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "UPDATE Courses SET is_deleted = 1 WHERE course_id = %s"
    cursor.execute(sql, (course_id,))
    conn.commit()
    cursor.close()
    conn.close()

def search_courses(keyword):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Courses WHERE course_name LIKE %s AND is_deleted = 0"
    cursor.execute(sql, ('%' + keyword + '%',))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def sort_courses(order_by='course_name'):
    conn = create_connection()
    cursor = conn.cursor()
    sql = f"SELECT * FROM Courses WHERE is_deleted = 0 ORDER BY {order_by}"
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
