from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class AddTaskDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.task_name_label = QLabel("Task name", self)
        self.deadline_label = QLabel("Deadline", self)
        self.task_description_label = QLabel("Task Description", self)

        self.user_input_task_name = QLineEdit(self)

        self.user_input_datetime = QDateTimeEdit(self)
        self.user_input_task_description = QTextEdit(self)

        self.button_widget = QWidget(self)
        self.button_layout = QHBoxLayout(self.button_widget)

        self.send_button = QPushButton("SEND")
        self.cancel_button = QPushButton("CANCEL")

        self.current_time = QDateTime.currentDateTime()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Add Task")
        self.setWindowIcon(QIcon("assets/AddTaskDialogBox/addtask_dialogbox_icon.png"))
        self.resize(420, 560)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.task_name_label.setGeometry(70, 35, 160, 40)
        self.deadline_label.setGeometry(70, 140, 160, 40)
        self.task_description_label.setGeometry(70, 245, 160, 40)

        self.user_input_task_name.setMaxLength(24)
        self.user_input_task_name.setGeometry(70, 70, 280, 50)
        self.user_input_task_name.setPlaceholderText("Enter task name")
        self.user_input_task_name.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.user_input_datetime.setGeometry(QtCore.QRect(70, 175, 280, 50))

        self.user_input_datetime.setDateTime(self.current_time)
        self.user_input_datetime.setMinimumDateTime(self.current_time)

        self.user_input_task_description.setGeometry(QtCore.QRect(70, 280, 280, 150))
        self.user_input_task_description.setPlaceholderText("Enter task description")

        self.button_widget.setGeometry(70, 450, 280, 60)
        self.button_layout.setContentsMargins(0, 0, 0, 0)

        self.send_button.clicked.connect(self.get_task_data)
        self.cancel_button.clicked.connect(self.reject)

        self.button_layout.addWidget(self.send_button)
        self.button_layout.addWidget(self.cancel_button)

        # Styling
        label_style = (
            "background-color: transparent;"
            "font-family: Helvetica;"
            "font-size: 18px;"
            "font: bold;"
            "color: rgb(0,0,0);"
        )

        input_style = (
            "background-color: rgb(246, 246, 246);"
            "font-family: Helvetica;"
            "font-size: 18px;"
            "border: 3px solid;"
            "border-color: rgb(222, 222, 222);"
            "color: rgb(0,0,0);"
            "padding-left: 10px;"
            "padding-right: 10px;"
        )

        self.task_name_label.setStyleSheet(label_style)
        self.deadline_label.setStyleSheet(label_style)
        self.task_description_label.setStyleSheet(label_style)

        self.user_input_task_name.setStyleSheet(input_style)
        self.user_input_datetime.setStyleSheet(input_style)
        self.user_input_task_description.setStyleSheet(input_style)

        self.send_button.setStyleSheet(
            "background-color: rgb(93, 217, 110);"
            "font-family: Helvetica;"
            "font-size: 18px;"
            "border: 3px solid;"
            "border-color: rgb(66, 135, 76);"
            "font: bold;"
            "color: rgb(0,0,0);"
            "width: 80px;"
            "height: 50px;"
        )

        self.cancel_button.setStyleSheet(
            "background-color: rgb(242, 155, 155);"
            "font-family: Helvetica;"
            "font-size: 18px;"
            "border: 3px solid;"
            "border-color: rgb(130, 57, 57);"
            "font: bold;"
            "color: rgb(0,0,0);"
            "width: 80px;"
            "height: 50px;"
        )

        self.show()

    def get_task_data(self):
        user_task_name = self.user_input_task_name.text()
        user_task_deadline = self.user_input_datetime.text()
        user_task_description = self.user_input_task_description.toPlainText()
        self.accept()

        return user_task_name, user_task_deadline, user_task_description