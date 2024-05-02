
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QColor
from PyQt5.QtChart import QChart, QChartView, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis
from PyQt5.Qt import Qt

# fetching all windows .ui file
Ui_students, _ = uic.loadUiType("UIs\StudentsWindow.ui")
Ui_main, _ = uic.loadUiType("UIs\MainWindow.ui")
Ui_staff_main, _ = uic.loadUiType("UIs\StaffMainWindow.ui")
Ui_student_detail, _ = uic.loadUiType("UIs\StudentDetailWindow.ui")
Ui_staff_detail, _ = uic.loadUiType("UIs\StaffDetailWindow.ui")
Ui_staff_table, _ = uic.loadUiType("UIs\StaffTableWindow.ui")
Ui_class_table, _ = uic.loadUiType("UIs\ClassTableWindow.ui")
Ui_add_student, _ = uic.loadUiType("UIs\AddStudentWindow.ui")

class GUI(QtWidgets.QMainWindow):

    def __init__(self):  # Constructor
        super().__init__()
        self.stacked_widget = QtWidgets.QStackedWidget()

        # initializing all widgets
        self.main_win()
        self.staff_main_win()
        self.student_detail_win()
        self.staff_detail_win()
        self.staff_table_win()
        self.class_table_win()
        self.students_win()
        self.add_student_win()

        self.setCentralWidget(self.stacked_widget)
        self.resize(600, 500)

    def main_win(self):  # main window widget
        self.main_win_btns = []
        self.main_widget = QtWidgets.QMainWindow()
        Ui_main().setupUi(self.main_widget)
        self.stacked_widget.addWidget(self.main_widget)
        self.main_win_btns.append(self.main_widget.findChild(QtWidgets.QPushButton, 'TeacherBtn'))
        self.main_win_btns.append(self.main_widget.findChild(QtWidgets.QPushButton, 'StudentBtn'))

    def staff_main_win(self):  # main window widget
        self.staff_main_win_btns = []
        self.staff_main_widget = QtWidgets.QMainWindow()
        Ui_staff_main().setupUi(self.staff_main_widget)
        self.stacked_widget.addWidget(self.staff_main_widget)
        self.staff_main_win_btns.append(self.staff_main_widget.findChild(QtWidgets.QPushButton, 'StudentsBtn'))
        self.staff_main_win_btns.append(self.staff_main_widget.findChild(QtWidgets.QPushButton, 'StaffBtn'))
        self.staff_main_win_btns.append(self.staff_main_widget.findChild(QtWidgets.QPushButton, 'ClassBtn'))
        self.staff_main_win_btns.append(self.staff_main_widget.findChild(QtWidgets.QPushButton, 'MainMenuBtn'))

    def student_detail_win(self):  # main window widget
        self.student_detail_win_btns = []
        self.student_detail_widget = QtWidgets.QMainWindow()
        Ui_student_detail().setupUi(self.student_detail_widget)
        self.stacked_widget.addWidget(self.student_detail_widget)
        self.student_detail_win_btns.append(self.student_detail_widget.findChild(QtWidgets.QPushButton, 'mainMenuBtn'))

    def staff_detail_win(self):  # main window widget
        self.staff_detail_win_btns = []
        self.staff_detail_widget = QtWidgets.QMainWindow()
        Ui_staff_detail().setupUi(self.staff_detail_widget)
        self.stacked_widget.addWidget(self.staff_detail_widget)
        self.staff_detail_win_btns.append(self.staff_detail_widget.findChild(QtWidgets.QPushButton, 'staffTableBtn'))
        self.staff_detail_win_btns.append(self.staff_detail_widget.findChild(QtWidgets.QPushButton, 'mainMenuBtn'))

    def students_win(self):  # students window widget
        self.students_win_btns = []
        self.students_widget = QtWidgets.QMainWindow()
        Ui_students().setupUi(self.students_widget)
        self.stacked_widget.addWidget(self.students_widget)
        self.students_table = self.students_widget.findChild(QtWidgets.QTableWidget, 'StudentsTable')
        self.students_win_btns.append(self.students_widget.findChild(QtWidgets.QPushButton, 'mainMenuBtn'))
        self.students_win_btns.append(self.students_widget.findChild(QtWidgets.QPushButton, 'delBtn'))
        self.students_win_btns.append(self.students_widget.findChild(QtWidgets.QPushButton, 'addBtn'))

    def staff_table_win(self):  # students window widget
        self.staff_table_win_btns = []
        self.staff_table_widget = QtWidgets.QMainWindow()
        Ui_staff_table().setupUi(self.staff_table_widget)
        self.stacked_widget.addWidget(self.staff_table_widget)
        self.staff_table = self.staff_table_widget.findChild(QtWidgets.QTableWidget, 'StaffTable')
        self.staff_table_win_btns.append(self.staff_table_widget.findChild(QtWidgets.QPushButton, 'mainMenuBtn'))
        self.staff_table_win_btns.append(self.staff_table_widget.findChild(QtWidgets.QPushButton, 'delBtn'))

    def class_table_win(self):  # students window widget
        self.class_table_win_btns = []
        self.class_table_widget = QtWidgets.QMainWindow()
        Ui_class_table().setupUi(self.class_table_widget)
        self.stacked_widget.addWidget(self.class_table_widget)
        self.class_table = self.class_table_widget.findChild(QtWidgets.QTableWidget, 'ClassTable')
        self.class_table_win_btns.append(self.class_table_widget.findChild(QtWidgets.QPushButton, 'mainMenuBtn'))

    def add_student_win(self):  # main window widget
        self.add_student_win_btns = []
        self.add_student_widget = QtWidgets.QMainWindow()
        Ui_add_student().setupUi(self.add_student_widget)
        self.stacked_widget.addWidget(self.add_student_widget)
        self.add_student_win_btns.append(self.add_student_widget.findChild(QtWidgets.QPushButton, 'add_std_btn'))
        self.add_student_win_btns.append(self.add_student_widget.findChild(QtWidgets.QPushButton, 'main_menu_btn'))

    def goto_page(self, widget):  # traverse between windows
        self.disconnect_btns()
        index = self.stacked_widget.indexOf(widget)
        # print("index")
        wide_screen_indexes = [4, 5, 6]
        if index >= 0:  # check if widget exists
            if index in wide_screen_indexes:
                self.resize(600, 500)
            else:
                self.resize(300, 500)
            self.stacked_widget.setCurrentIndex(index)

    def disconnect_btns(self):  # disconnect buttons
        # print(" ")
        for btn in self.main_win_btns:
            try:
                btn.clicked.disconnect()
            except:
                pass

        for btn in self.staff_main_win_btns:
            try:
                btn.clicked.disconnect()
            except:
                pass

        for btn in self.student_detail_win_btns:
            try:
                btn.clicked.disconnect()
            except:
                pass

        for btn in self.staff_detail_win_btns:
            try:
                btn.clicked.disconnect()
            except:
                pass

        for btn in self.students_win_btns:
            try:
                btn.clicked.disconnect()
            except:
                pass

        for btn in self.staff_table_win_btns:
            try:
                btn.clicked.disconnect()
            except:
                pass

        for btn in self.class_table_win_btns:
            try:
                btn.clicked.disconnect()
            except:
                pass

        for btn in self.add_student_win_btns:
            try:
                btn.clicked.disconnect()
            except:
                pass
