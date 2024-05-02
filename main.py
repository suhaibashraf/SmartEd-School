import sys
from PyQt5.QtCore import *
from GUI import *
from dbcon import *
from datetime import *
import qdarkgraystyle  # theme lib
from PyQt5.QtWidgets import *

# global variables
g = None
db = None
items = None


def main_win():
    g.disconnect_btns()
    g.goto_page(g.main_widget)
    g.main_win_btns[0].clicked.connect(teacher_main_win)
    g.main_win_btns[1].clicked.connect(student_detail_win)


def teacher_main_win():
    g.disconnect_btns()
    g.goto_page(g.staff_main_widget)
    g.staff_main_win_btns[0].clicked.connect(students_win)
    g.staff_main_win_btns[1].clicked.connect(staff_detail_win)
    g.staff_main_win_btns[2].clicked.connect(class_table_win)
    g.staff_main_win_btns[3].clicked.connect(main_win)


def student_detail_win():
    g.disconnect_btns()
    g.goto_page(g.student_detail_widget)
    if g.student_detail_widget.findChild(QtWidgets.QComboBox, 'students_list').count() == 0:
        get_students()
    show_student_details()
    g.student_detail_widget.findChild(QtWidgets.QComboBox, 'students_list').currentIndexChanged.connect(show_student_details)
    g.student_detail_win_btns[0].clicked.connect(main_win)

def staff_detail_win():
    g.disconnect_btns()
    g.goto_page(g.staff_detail_widget)
    if g.staff_detail_widget.findChild(QtWidgets.QComboBox, 'staff_list').count() == 0:
        get_staff()
    show_staff_details()
    g.staff_detail_widget.findChild(QtWidgets.QComboBox, 'staff_list').currentIndexChanged.connect(show_staff_details)
    g.staff_detail_win_btns[0].clicked.connect(staff_table_win)
    g.staff_detail_win_btns[1].clicked.connect(main_win)


def students_win():  # revenue window view
    g.disconnect_btns()
    g.goto_page(g.students_widget)
    show_students()
    g.students_win_btns[0].clicked.connect(main_win)
    g.students_win_btns[1].clicked.connect(del_student)
    g.students_win_btns[2].clicked.connect(add_student)


def staff_table_win():  # revenue window view
    g.disconnect_btns()
    g.goto_page(g.staff_table_widget)
    show_staff()
    g.staff_table_win_btns[0].clicked.connect(main_win)
    g.staff_table_win_btns[1].clicked.connect(del_staff)

def class_table_win():  # revenue window view
    g.disconnect_btns()
    g.goto_page(g.class_table_widget)
    show_class()
    g.class_table_win_btns[0].clicked.connect(main_win)


def get_students():
    data = db.fetch_students()
    for d in data:
        g.student_detail_widget.findChild(QtWidgets.QComboBox, 'students_list').addItem(str(d[0]))

def get_staff():
    data = db.fetch_staff()
    for d in data:
        g.staff_detail_widget.findChild(QtWidgets.QComboBox, 'staff_list').addItem(str(d[0]))

def show_student_details():
    std_id = int(g.student_detail_widget.findChild(QtWidgets.QComboBox, 'students_list').currentText())
    data = db.fetch_student_plus_fee(std_id)

    for d in data:
        g.student_detail_widget.findChild(QtWidgets.QLabel, 'Name_txt').setText(d[1])
        g.student_detail_widget.findChild(QtWidgets.QLabel, 'Roll_no_txt').setText(d[0])
        g.student_detail_widget.findChild(QtWidgets.QLabel, 'Class_id_txt').setText(d[2])
        g.student_detail_widget.findChild(QtWidgets.QLabel, 'Percentage_txt').setText(d[3])
        g.student_detail_widget.findChild(QtWidgets.QLabel, 'Position_txt').setText(d[4])
        g.student_detail_widget.findChild(QtWidgets.QLabel, 'Fee_txt').setText(d[5])
        g.student_detail_widget.findChild(QtWidgets.QLabel, 'Deadline_txt').setText(d[6])


def show_staff_details():
    staff_id = int(g.staff_detail_widget.findChild(QtWidgets.QComboBox, 'staff_list').currentText())
    data = db.fetch_staff_plus_salary(staff_id)
    #
    for d in data:
        g.staff_detail_widget.findChild(QtWidgets.QLabel, 'name_txt').setText(d[1])
        g.staff_detail_widget.findChild(QtWidgets.QLabel, 'ID_txt').setText(d[0])
        g.staff_detail_widget.findChild(QtWidgets.QLabel, 'staff_city_txt').setText(d[2])
        g.staff_detail_widget.findChild(QtWidgets.QLabel, 'phone_txt').setText(d[3])
        g.staff_detail_widget.findChild(QtWidgets.QLabel, 'salary_txt').setText(d[4])

def show_students():  # showing students in table
    clear_rec()
    data = db.fetch_students_plus_fees()
    for rowData in data:
        # print(rowData)
        row = g.students_table.rowCount()
        g.students_table.setRowCount(row + 1)
        rowData = list(rowData)
        col = 0
        for item in rowData:
            cell = QTableWidgetItem(str(item))
            g.students_table.setItem(row, col, cell)
            col += 1


def show_staff():
    clear_rec()
    data = db.fetch_all_staff_plus_salary()
    for rowData in data:
        row = g.staff_table.rowCount()
        g.staff_table.setRowCount(row + 1)
        rowData = list(rowData)
        col = 0
        for item in rowData:
            cell = QTableWidgetItem(str(item))
            g.staff_table.setItem(row, col, cell)
            col += 1


def show_class():
    clear_rec()
    data = db.fetch_all_class_data()
    for rowData in data:
        row = g.class_table.rowCount()
        g.class_table.setRowCount(row + 1)
        rowData = list(rowData)
        col = 0
        for item in rowData:
            cell = QTableWidgetItem(str(item))
            g.class_table.setItem(row, col, cell)
            col += 1


def add_student():
    g.goto_page(g.add_student_widget)
    classes = db.fetch_class_id()
    for c in classes:
        # print(str(c[0]))
        g.add_student_widget.findChild(QtWidgets.QComboBox, 'class_id_list').addItem(str(c[0]))
    g.add_student_win_btns[0].clicked.connect(add_student_in_DB)
    g.add_student_win_btns[1].clicked.connect(main_win)


def add_student_in_DB():
    # print("ss")
    data1 = []
    data2 = []
    check = True

    rollnum = db.fetch_students_roll_no()

    data1.append(str(int(rollnum[(len(rollnum))-1][0]) + 1))
    data2.append(str(int(rollnum[(len(rollnum)) - 1][0]) + 1))

    # getting data from window GUI
    data1.append((g.add_student_widget.findChild(QtWidgets.QLineEdit, 'name_txt')).displayText())
    data1.append((g.add_student_widget.findChild(QtWidgets.QComboBox, 'class_id_list')).currentText())
    data1.append((g.add_student_widget.findChild(QtWidgets.QDoubleSpinBox, 'percentage_txt')).value())
    data1.append((g.add_student_widget.findChild(QtWidgets.QSpinBox, 'position_txt')).value())

    data2.append((g.add_student_widget.findChild(QtWidgets.QLineEdit, 'name_txt')).displayText())
    data2.append((g.add_student_widget.findChild(QtWidgets.QDoubleSpinBox, 'fee_txt')).value())
    data2.append((g.add_student_widget.findChild(QtWidgets.QDateEdit, 'date_txt')).date().toString("yy-MM-dd"))

    for d in data1:
        if d == "":
            check = False
    if check:  # check if any field is empty or not
        (g.add_student_widget.findChild(QtWidgets.QLineEdit, 'name_txt')).clear()
        db.insert_student(tuple(data1))
        db.insert_student_fee(tuple(data2))
        main_win()
    else:
        g.add_student_widget.findChild(QtWidgets.QLabel, 'error_msg').setText("Invalid Entry")


def del_student():
    rows = g.students_table.selectionModel().selectedRows()
    if not rows:
        g.students_widget.findChild(QtWidgets.QLabel, 'error_msg').setText(
            "Select the row by clicking the most left of row")
    else:
        id = rows[0].data()
        db.delete_student(id)
        clear_rec()
        main_win()

def del_staff():
    rows = g.staff_table.selectionModel().selectedRows()
    if not rows:
        g.staff_table_widget.findChild(QtWidgets.QLabel, 'error_msg').setText(
            "Select the row by clicking the most left of row")
    else:
        id = rows[0].data()
        db.delete_staff(id)
        clear_rec()
        main_win()

def clear_rec():  # clear all tables and global data
    g.disconnect_btns()
    g.class_table.clearContents()
    g.class_table.model().removeRows(0, g.class_table.rowCount())
    g.staff_table.clearContents()
    g.staff_table.model().removeRows(0, g.staff_table.rowCount())
    g.students_table.clearContents()
    g.students_table.model().removeRows(0, g.students_table.rowCount())


def main():  # main function
    global db
    db = dbcon()  # loading DB
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkgraystyle.load_stylesheet())
    global g
    g = GUI()  # loading GUI
    global items
    items = []  # setting global variable
    main_win()  # starting with login
    g.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
