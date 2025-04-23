from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from modules.TaskDialogBox import dialog_tools, task_dialog_builder
from core.TaskDialogBox.change_visual_ui import ChangeVisualUI


class TaskDialogBox(QDialog):

    def __init__(self):
        super().__init__()
        self.visual_changer = ChangeVisualUI(self)

        self.dark_theme = True

        self.main_layout = QVBoxLayout()

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
        self.user_input_task_name.setMaxLength(24)
        self.user_input_task_name.setPlaceholderText("Enter task name")

        self.user_input_task_deadline.setDateTime(self.current_time)
        self.user_input_task_deadline.setMinimumDateTime(self.current_time)

        self.user_input_task_description.setPlaceholderText("Enter task description")


        # -----------------------------------------------
        self.user_input_task_name.setMinimumHeight(50)
        self.user_input_task_deadline.setMinimumHeight(50)
        self.user_input_task_description.setMinimumHeight(50)


        self.button_layout.setContentsMargins(0, 0, 0, 0)
        self.button_layout.setSpacing(0)

        self.button_layout.addWidget(self.send_button)
        self.button_layout.addSpacing(5)
        self.button_layout.addWidget(self.cancel_button)

        self.button_widget.setLayout(self.button_layout)

        self.main_layout.setContentsMargins(50, 50, 50, 50)
        self.main_layout.setSpacing(0)

        self.main_layout.addWidget(self.task_name_label)
        self.main_layout.addWidget(self.user_input_task_name)
        self.main_layout.addSpacing(25)

        self.main_layout.addWidget(self.task_deadline_label)
        self.main_layout.addWidget(self.user_input_task_deadline)
        self.main_layout.addSpacing(25)

        self.main_layout.addWidget(self.task_description_label)
        self.main_layout.addWidget(self.user_input_task_description)
        self.main_layout.addSpacing(25)

        self.main_layout.addWidget(self.button_widget)

        self.setLayout(self.main_layout)

        # self.task_name_label.move(50, 50)
        # self.user_input_task_name.setGeometry(50,75,420,50)
        #
        # self.task_deadline_label.move(50, 150)
        # self.user_input_task_deadline.setGeometry(50,175,420,50)
        #
        # self.task_description_label.move(50, 250)
        # self.user_input_task_description.setGeometry(50,275,420,200)
        #
        # self.button_widget.setGeometry(50,500,420,50)



        # -------------------------------------
        task_dialog_builder.setup_UI(self)
        self.visual_changer.change_UI_theme()
        self.show()