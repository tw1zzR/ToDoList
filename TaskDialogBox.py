from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class TaskDialogBox(QDialog):
    def __init__(self):
        super().__init__()
        self.dark_theme = True

        self.task_name_label = QLabel("Task name", self)
        self.task_deadline_label = QLabel("Deadline", self)
        self.task_description_label = QLabel("Task Description", self)

        self.user_input_task_name = QLineEdit(self)
        self.user_input_task_deadline = QDateTimeEdit(self)
        self.user_input_task_description = QTextEdit(self)

        self.button_widget = QWidget(self)
        self.button_layout = QHBoxLayout(self.button_widget)

        self.send_button = QPushButton("SEND")
        self.cancel_button = QPushButton("CANCEL")

        self.current_time = QDateTime.currentDateTime()
        self.max_chars = 150

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Add Task")
        self.setWindowIcon(QIcon("assets/TaskDialogBox/addtask_dialogbox_icon.png"))
        self.resize(520, 600)

        self.setWhatsThis("It's a dialog box that allows you to enter data for your task.")
        self.user_input_task_name.setWhatsThis("It's an input field for the task name.")
        self.user_input_task_deadline.setWhatsThis("It's a field displaying the task deadline.")
        self.user_input_task_description.setWhatsThis("It's a field for entering the task description.")
        self.send_button.setWhatsThis("It's a Send button to submit the task data.")
        self.cancel_button.setWhatsThis("It's a Cancel button to close the window and discard the task.")

        self.task_name_label.move(50, 50)
        self.user_input_task_name.setGeometry(50,75,420,50)

        self.task_deadline_label.move(50, 150)
        self.user_input_task_deadline.setGeometry(50,175,420,50)

        self.task_description_label.move(50, 250)
        self.user_input_task_description.setGeometry(50,275,420,200)

        self.button_widget.setGeometry(50,500,420,50)

        self.user_input_task_name.setMaxLength(24)
        self.user_input_task_name.setPlaceholderText("Enter task name")

        self.user_input_task_deadline.setDateTime(self.current_time)
        self.user_input_task_deadline.setMinimumDateTime(self.current_time)

        self.user_input_task_description.setPlaceholderText("Enter task description")
        self.user_input_task_description.textChanged.connect(self.limit_max_chars_in_textedit)

        self.button_layout.setContentsMargins(0, 0, 0, 0)

        self.send_button.clicked.connect(self.get_task_data)
        self.cancel_button.clicked.connect(self.reject)

        self.button_layout.addWidget(self.send_button)
        self.button_layout.addWidget(self.cancel_button)


        # Styling
        self.task_name_label.setObjectName("task_name_label")
        self.task_deadline_label.setObjectName("task_deadline_label")
        self.task_description_label.setObjectName("task_description_label")
        self.user_input_task_name.setObjectName("user_input_task_name")
        self.user_input_task_deadline.setObjectName("user_input_task_deadline")
        self.user_input_task_description.setObjectName("user_input_task_description")
        self.send_button.setObjectName("send_button")
        self.cancel_button.setObjectName("cancel_button")

        if self.dark_theme:
            self.apply_dark_theme()
        else:
            self.apply_light_theme()

        self.show()

    def compare_with_main_win_theme(self, main_win_dark_theme):
        if main_win_dark_theme:
            self.apply_dark_theme()
        else:
            self.apply_light_theme()

    def apply_light_theme(self):
        self.setStyleSheet("""
            QDialog {
                background-color: rgb(255, 255, 255);
            }
            QLabel {            
                font-family: Helvetica; 
                color: rgb(44,44,44);       
            }
            QLabel#task_name_label, QLabel#task_deadline_label, QLabel#task_description_label {
                background-color: transparent;
                font-family: Helvetica;
                font-size: 18px;
                font: bold;
            }
            QLineEdit#user_input_task_name, QDateTimeEdit#user_input_task_deadline, QTextEdit#user_input_task_description {
                background-color: rgb(60,60,60);
                font-family: Helvetica;
                font-size: 18px;
                border: 3px solid rgb(30,30,30);
                color: rgb(235,235,235);
            }
            QTextEdit#user_input_task_description, QLineEdit#user_input_task_name, QDateTimeEdit#user_input_task_deadline {
                padding-top: 5px;
                padding-left: 10px;
                padding-right: 10px;
            }
            QPushButton {
                font-family: Helvetica;
                font-size: 18px;
                border: 3px solid;
                font: bold;
                color: rgb(44, 44, 44);
                width: 80px;
                height: 50px;
            }
            QPushButton#send_button {
                background-color: rgb(93, 217, 110);
                border-color: rgb(66, 135, 76);
            }
            QPushButton#cancel_button {
                background-color: rgb(242, 155, 155);
                border-color: rgb(130, 57, 57);
            }
        """)

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QDialog {
                background-color: rgb(44, 44, 44);
            }
            QLabel {            
                font-family: Helvetica; 
                color: rgb(235,235,235);       
            }
            QLabel#task_name_label, QLabel#task_deadline_label, QLabel#task_description_label {
                background-color: transparent;
                font-family: Helvetica;
                font-size: 18px;
                font: bold;
            }
            QLineEdit#user_input_task_name, QDateTimeEdit#user_input_task_deadline, QTextEdit#user_input_task_description {
                background-color: rgb(246, 246, 246);
                border: 3px solid rgb(222, 222, 222);
                font-family: Helvetica;
                font-size: 18px;
                color: rgb(44, 44, 44);          
            }
            QTextEdit#user_input_task_description, QLineEdit#user_input_task_name, QDateTimeEdit#user_input_task_deadline {
                padding-top: 5px;
                padding-left: 10px;
                padding-right: 10px;
            }
            QPushButton {
                font-family: Helvetica;
                font-size: 18px;
                border: 3px solid;
                font: bold;
                color: rgb(44, 44, 44);
                width: 80px;
                height: 50px;
            }
            QPushButton#send_button {
                background-color: rgb(93, 217, 110);
                border-color: rgb(66, 135, 76);
            }
            QPushButton#cancel_button {
                background-color: rgb(242, 155, 155);
                border-color: rgb(130, 57, 57);
            }
        """)

    def get_task_data(self):
        user_task_name = self.user_input_task_name.text()
        user_task_deadline = self.user_input_task_deadline.text()
        user_task_description = self.user_input_task_description.toPlainText()

        if user_task_name.strip():
            self.accept()

            return user_task_name, user_task_deadline, user_task_description
        else:
            empty_task_name_msgbox = self.create_warning_messagebox()
            empty_task_name_msgbox.exec_()


    def limit_max_chars_in_textedit(self):
        text_chars = self.user_input_task_description.toPlainText()

        if len(text_chars) > self.max_chars:
            self.user_input_task_description.setPlainText(text_chars[:self.max_chars])
            self.user_input_task_description.moveCursor(QTextCursor.End)

    def create_warning_messagebox(self):
        warning_msgbox = QMessageBox()

        warning_msgbox.setWindowTitle("About App")
        warning_msgbox.setWindowIcon(QIcon("assets/warning_icon_1.png"))
        warning_msgbox.setTextFormat(Qt.RichText)
        warning_msgbox.setText("Task name cannot be blank.")
        warning_msgbox.setIcon(QMessageBox.Warning)

        warning_msgbox.setStyleSheet("""
            QMessageBox {
                font-family: Helvetica;
                color: rgb(0,0,0);
                font-size: 16px;
            }
            QPushButton {
                font-family: Helvetica;
                font-size: 14px;
            }
            """)

        return warning_msgbox