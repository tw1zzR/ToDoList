from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class CustomTaskInfoMessageBox(QDialog):
    def __init__(self, task_name, task_deadline, task_description):
        super().__init__()
        self.dark_theme = True

        self.task_name_label = QLabel("Name:", self)
        self.task_deadline_label = QLabel("Deadline:", self)
        self.task_description_label = QLabel("Description:", self)

        self.user_task_name_label = QLabel(self)
        self.user_task_deadline_label = QLabel(self)
        self.user_task_description_textedit = QTextEdit(self)

        self.set_task_info_msgbox_new_data(task_name, task_deadline, task_description)

        self.OK_Button = QPushButton("OK", self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Task Info")
        self.setWindowIcon(QIcon("assets/TaskInfoMessageBox/gray_task_info_button_V2_icon.png"))
        self.setFixedSize(520,600)

        self.user_task_description_textedit.setReadOnly(True)

        self.OK_Button.clicked.connect(self.close)

        self.setWhatsThis("It's a message box containing task information.")
        self.user_task_name_label.setWhatsThis("It's the task name.")
        self.user_task_deadline_label.setWhatsThis("It's the task deadline.")
        self.user_task_description_textedit.setWhatsThis("It's the task description.")
        self.OK_Button.setWhatsThis("It's an OK button to close message box.")

        self.task_name_label.move(50, 50)
        self.user_task_name_label.move(50, 75)

        self.task_deadline_label.move(50, 150)
        self.user_task_deadline_label.move(50, 175)

        self.task_description_label.move(50, 250)
        self.user_task_description_textedit.move(50, 275)

        self.OK_Button.move(50, 500)

        self.user_task_name_label.setFixedSize(420,50)
        self.user_task_deadline_label.setFixedSize(420,50)
        self.user_task_description_textedit.setFixedSize(420,200)
        self.OK_Button.setFixedSize(420, 50)

        self.user_task_name_label.setAlignment(Qt.AlignCenter)
        self.user_task_deadline_label.setAlignment(Qt.AlignCenter)
        self.user_task_description_textedit.setAlignment(Qt.AlignCenter)

        # Styling
        self.task_name_label.setObjectName("task_name_label")
        self.task_deadline_label.setObjectName("task_deadline_label")
        self.task_description_label.setObjectName("task_description_label")
        self.user_task_name_label.setObjectName("user_task_name_label")
        self.user_task_deadline_label.setObjectName("user_task_deadline_label")
        self.user_task_description_textedit.setObjectName("user_task_description_textedit")
        self.OK_Button.setObjectName("OK_Button")

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
        self.dark_theme = False

        self.setStyleSheet("""
            QDialog {
                background-color: rgb(255, 255, 255);
            }
            QLabel {            
                font-family: Helvetica; 
                color: rgb(255, 255, 255);       
            }
            QLabel#task_name_label, QLabel#task_deadline_label, QLabel#task_description_label {
                background-color: transparent;
                font-family: Helvetica;
                font-size: 18px;
                font: bold;
                color: rgb(44,44,44);
            }
            QLabel#user_task_name_label, QLabel#user_task_deadline_label, QTextEdit#user_task_description_textedit {
                background-color: rgb(60, 60, 60);
                border: 3px solid rgb(30, 30, 30);  
                font-family: Helvetica;
                font-size: 18px;
                color: rgb(235,235,235);
            }
            QTextEdit#user_task_description_textedit {
                padding-top: 5px;
                padding-left: 10px;
                padding-right: 10px;
            }
            QPushButton#OK_Button {
                background-color: rgb(93, 217, 110);
                font-family: Helvetica;
                font-size: 18px;
                border: 3px solid rgb(66, 135, 76);
                font: bold;
                color: rgb(44, 44, 44);
            }
        """)

    def apply_dark_theme(self):
        self.dark_theme = True

        self.setStyleSheet("""
            QDialog {
                background-color: rgb(44, 44, 44);
            }
            QLabel {            
                font-family: Helvetica; 
                color: rgb(0,0,0);       
            }
            QLabel#task_name_label, QLabel#task_deadline_label, QLabel#task_description_label {
                background-color: transparent;
                font-family: Helvetica;
                font-size: 18px;
                font: bold;
                color: rgb(235,235,235);
            }
            QLabel#user_task_name_label, QLabel#user_task_deadline_label, QTextEdit#user_task_description_textedit {
                background-color: rgb(246, 246, 246);
                font-family: Helvetica;
                font-size: 18px;
                border: 3px solid rgb(222, 222, 222);
                color: rgb(44, 44, 44);
            }
            QTextEdit#user_task_description_textedit {
                padding-top: 5px;
                padding-left: 10px;
                padding-right: 10px;
            }
            QPushButton#OK_Button {
                background-color: rgb(93, 217, 110);
                font-family: Helvetica;
                font-size: 18px;
                border: 3px solid;
                border-color: rgb(66, 135, 76);
                font: bold;
                color: rgb(44, 44, 44);
            }
        """)


    def set_task_info_msgbox_new_data(self, task_name, task_deadline, task_description):
        self.task_name = task_name
        self.task_deadline = task_deadline
        self.task_description = task_description

        self.user_task_name_label.setText(task_name)
        self.user_task_deadline_label.setText(task_deadline)
        self.user_task_description_textedit.setText(task_description)

        self.user_task_description_textedit.setAlignment(Qt.AlignCenter)