from datetime import datetime

import mysql.connector
from mysql.connector import errorcode


class dbcon:
    def __init__(self):
        self.cnx = None
        try:
            self.cnx = mysql.connector.connect(user='root', password='Jugla',
                                          host='localhost',
                                          database='sms')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            self.cnx.close()

        self.cursor = self.cnx.cursor()

    def fetch_students_plus_fees(self):  # get students data
        query = ("SELECT sms.student.*, sms.student_fee.student_fee, sms.student_fee.fee_deadline, sms.class_section.student_section, sms.class_section.student_class "
                 "FROM sms.student "
                 "INNER JOIN sms.class_section ON sms.student.id_1=sms.class_section.id_1 "
                 "INNER JOIN sms.student_fee ON sms.student.roll_number=sms.student_fee.roll_number "
                 "ORDER BY sms.student.roll_number + 0")
        self.cursor.execute(query)
        return self.cursor

    def fetch_all_class_data(self):  # get students data
        query = ("SELECT sms.time_1.*, sms.timetable_roomalotment.room_number, sms.timetable_roomalotment.timing, sms.class_section.student_section, sms.class_section.student_class, sms.subject.subject_name "
                 "FROM sms.time_1 "
                 "INNER JOIN sms.timetable_roomalotment ON sms.time_1.id_1=sms.timetable_roomalotment.id_1 "
                 "INNER JOIN sms.class_section ON sms.time_1.id_1=sms.class_section.id_1 "
                 "INNER JOIN sms.subject ON sms.time_1.subject_id=sms.subject.subject_id "
                 "ORDER BY sms.time_1.id_1 + 0")
        self.cursor.execute(query)
        return self.cursor

    def fetch_students(self):  # get students data
        query = ("SELECT * FROM sms.student ORDER BY roll_number + 0")
        self.cursor.execute(query)
        return self.cursor

    def fetch_class_id(self):
        query = ("SELECT id_1 FROM sms.class_section ORDER BY id_1 + 0")
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_students_roll_no(self):  # get students data
        query = ("SELECT roll_number FROM sms.student ORDER BY roll_number + 0")
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_staff(self):  # get students data
        query = ("SELECT * FROM sms.staff ORDER BY staff_id + 0")
        self.cursor.execute(query)
        return self.cursor

    def fetch_staff_plus_salary(self, staff_id):  # get students data
        query = ("SELECT sms.staff.*, sms.salary.salary FROM sms.staff INNER JOIN sms.salary ON sms.staff.staff_id=sms.salary.staff_id WHERE sms.staff.staff_id = %s")
        staff_id = (staff_id,)
        self.cursor.execute(query, staff_id)
        return self.cursor

    def fetch_all_staff_plus_salary(self):  # get students data
        query = ("SELECT sms.staff.*, sms.salary.salary FROM sms.staff INNER JOIN sms.salary ON sms.staff.staff_id=sms.salary.staff_id")
        self.cursor.execute(query)
        return self.cursor

    def fetch_student_plus_fee(self, std_id):  # get students data
        query = ("SELECT sms.student.*, sms.student_fee.student_fee, sms.student_fee.fee_deadline FROM sms.student INNER JOIN sms.student_fee ON sms.student.roll_number=sms.student_fee.roll_number WHERE sms.student.roll_number = %s")
        std_id = (std_id, )
        self.cursor.execute(query, std_id)
        return self.cursor

    def fetch_student_fee(self, std_id):  # get students data
        query = ("SELECT * FROM sms.student_fee WHERE roll_number = %s")
        std_id = (std_id, )
        self.cursor.execute(query, std_id)
        return self.cursor

    def insert_student(self, student_data):  # get students data
        query = ("INSERT INTO sms.student (roll_number, student_name, id_1, student_term_percentage, student_class_position) "
                 "VALUES (%s, %s, %s, %s, %s)")
        self.cursor.execute(query, student_data)
        self.cnx.commit()

    def insert_student_fee(self, student_fee_data):  # get students data
        query = ("INSERT INTO sms.student_fee (roll_number, student_name, student_fee, fee_deadline) "
                 "VALUES (%s, %s, %s, %s)")
        self.cursor.execute(query, student_fee_data)
        self.cnx.commit()

    def delete_student(self, std_id):  # get students data
        query = ("DELETE sms.student, sms.student_fee FROM sms.student INNER JOIN sms.student_fee "
                 "WHERE sms.student.roll_number = sms.student_fee.roll_number and sms.student.roll_number = %s")
        std_id = (std_id, )
        self.cursor.execute(query, std_id)
        self.cnx.commit()

    def delete_staff(self, staff_id):  # get students data
        query = ("DELETE sms.staff, sms.salary FROM sms.staff INNER JOIN sms.salary "
                 "WHERE sms.staff.staff_id = sms.salary.staff_id and sms.staff.staff_id = %s")
        staff_id = (staff_id, )
        self.cursor.execute(query, staff_id)
        self.cnx.commit()


if __name__ == '__main__':
    mysql = dbcon()
    # mysql.fetch_student()
    students = mysql.fetch_student()
    for student in students:
        print(student[1])