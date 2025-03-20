from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class AddTaskDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Add Task")
        self.resize(420, 560)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")

        # Labels
        task_label = QLabel("Task Description", self)
        task_label.setGeometry(70, 245, 160, 40)

        deadline_label = QLabel("Deadline", self)
        deadline_label.setGeometry(70, 140, 160, 40)

        task_name_label = QLabel("Task name", self)
        task_name_label.setGeometry(70, 35, 160, 40)

        # User Input
        user_input_task_name = QLineEdit(self)
        user_input_task_name.setGeometry(70, 70, 280, 50)
        user_input_task_name.setPlaceholderText("Enter task name")
        user_input_task_name.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        user_input_task = QTextEdit(self)
        user_input_task.setGeometry(QtCore.QRect(70, 280, 280, 150))
        user_input_task.setPlaceholderText("Enter task description")

        user_input_datetime = QDateTimeEdit(self)
        user_input_datetime.setGeometry(QtCore.QRect(70, 175, 280, 50))
        current_time = QDateTime.currentDateTime()
        user_input_datetime.setDateTime(current_time)

        # Buttons Layout
        button_widget = QWidget(self)
        button_widget.setGeometry(70, 450, 281, 58)

        button_layout = QHBoxLayout(button_widget)
        button_layout.setContentsMargins(0, 0, 0, 0)

        send_button = QPushButton("SEND")
        send_button.clicked.connect(self.accept)
        cancel_button = QPushButton("CANCEL")
        cancel_button.clicked.connect(self.reject)

        button_layout.addWidget(send_button)
        button_layout.addWidget(cancel_button)

        # Styling
        label_style = (
            "background-color: transparent;"
            "font-family: Helvetica;"
            "font-size: 20px;"
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

        task_label.setStyleSheet(label_style)
        deadline_label.setStyleSheet(label_style)
        task_name_label.setStyleSheet(label_style)

        user_input_task_name.setStyleSheet(input_style)
        user_input_task.setStyleSheet(input_style)
        user_input_datetime.setStyleSheet(input_style)

        send_button.setStyleSheet(
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

        cancel_button.setStyleSheet(
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
        user_task_deadline =
        user_task_description =