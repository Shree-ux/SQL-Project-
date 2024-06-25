CREATE DATABASE EduSchema;
USE EduSchema;
drop database EduSchema;
CREATE TABLE Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(255) NOT NULL,
    course_description TEXT,
    start_date DATE,
    end_date DATE,
    UNIQUE (course_name)
);
CREATE TABLE Instructors (
    instructor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone_number VARCHAR(15),
    bio TEXT
);
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone_number VARCHAR(15),
    date_of_birth DATE,
    enrollment_date DATE 
);
CREATE TABLE Enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE ,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    UNIQUE (student_id, course_id)
);
CREATE TABLE Assessments (
    assessment_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    assessment_name VARCHAR(255) NOT NULL,
    max_score INT NOT NULL CHECK (max_score > 0),
    assessment_date DATE,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
CREATE TABLE Grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    assessment_id INT NOT NULL,
    score INT NOT NULL CHECK (score >= 0),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (assessment_id) REFERENCES Assessments(assessment_id),
    UNIQUE (student_id, assessment_id)
);
CREATE TABLE CourseInstructors (
    course_instructor_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    instructor_id INT NOT NULL,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id),
    UNIQUE (course_id, instructor_id)
);
select * from courses;
ALTER TABLE Courses ADD is_deleted TINYINT(1) DEFAULT 0;
ALTER TABLE Instructors ADD is_deleted TINYINT(1) DEFAULT 0;
ALTER TABLE Students ADD is_deleted TINYINT(1) DEFAULT 0;
ALTER TABLE Enrollments ADD is_deleted TINYINT(1) DEFAULT 0;
ALTER TABLE Assessments ADD is_deleted TINYINT(1) DEFAULT 0;
ALTER TABLE Grades ADD is_deleted TINYINT(1) DEFAULT 0;
ALTER TABLE CourseInstructors ADD is_deleted TINYINT(1) DEFAULT 0;




