from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from core.task_window_theme_manager import TaskWindowThemeManager
from modules.TaskDialog import dialog_tools


class TaskDialog(QDialog):

    def __init__(self, is_input):
        super().__init__()
        self.is_input = is_input

        self.visual_changer = TaskWindowThemeManager(self)

        self.dark_theme = True

        self.main_layout = QVBoxLayout()

        self.button_widget = QWidget(self)
        self.button_layout = QHBoxLayout(self.button_widget)

        self.task_name_label = QLabel("Name:", self)
        self.task_deadline_label = QLabel("Deadline:", self)
        self.task_description_label = QLabel("Description:", self)

        self.user_input_task_name = QLineEdit(self)
        self.user_input_task_deadline = QDateTimeEdit(self)
        self.user_input_task_description = QTextEdit(self)

        if is_input:
            self.current_time = QDateTime.currentDateTime()
            self.max_chars = 150

            self.send_button = QPushButton("SEND", self)
            self.cancel_button = QPushButton("CANCEL", self)
        else:
            self.OK_Button = QPushButton("OK", self)

        # Init UI
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Task")
        self.resize(520, 600)

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

        self.button_layout.setContentsMargins(0, 0, 0, 0)
        self.button_layout.setSpacing(0)

        if self.is_input:
            self.button_layout.addWidget(self.send_button)
            self.button_layout.addSpacing(5)
            self.button_layout.addWidget(self.cancel_button)
        else:
            self.button_layout.addWidget(self.OK_Button)

        self.button_widget.setLayout(self.button_layout)
        self.main_layout.addWidget(self.button_widget)

        self.setLayout(self.main_layout)

        self.user_input_task_name.setMinimumHeight(50)
        self.user_input_task_deadline.setMinimumHeight(50)
        self.user_input_task_description.setMinimumHeight(50)

        if self.is_input:
            self.setWindowIcon(QIcon("assets/TaskInputDialog/addtask_dialogbox_icon.png"))

            self.user_input_task_name.setMaxLength(24)
            self.user_input_task_name.setPlaceholderText("Enter task name")
            self.user_input_task_deadline.setMinimumDateTime(QDateTime.currentDateTime())
            self.user_input_task_description.setPlaceholderText("Enter task description")

            self.user_input_task_description.textChanged.connect(lambda: dialog_tools.limit_max_chars_in_textedit(self))
            self.send_button.clicked.connect(lambda: dialog_tools.get_task_data(self))
            self.cancel_button.clicked.connect(self.reject)
        else:
            self.setWindowIcon(QIcon("assets/TaskInfoDialog/gray_task_info_button_V2_icon.png"))

            self.user_input_task_name.setReadOnly(True)
            self.user_input_task_deadline.setReadOnly(True)
            self.user_input_task_description.setReadOnly(True)

            self.OK_Button.clicked.connect(self.close)
            self.OK_Button.setMinimumHeight(50)

        self.task_name_label.setObjectName("task_name_label")
        self.task_deadline_label.setObjectName("task_deadline_label")
        self.task_description_label.setObjectName("task_description_label")
        self.user_input_task_name.setObjectName("user_input_task_name")
        self.user_input_task_deadline.setObjectName("user_input_task_deadline")
        self.user_input_task_description.setObjectName("user_input_task_description")

        if self.is_input:
            self.send_button.setObjectName("send_button")
            self.cancel_button.setObjectName("cancel_button")
        else:
            self.OK_Button.setObjectName("OK_Button")

        if self.is_input:
            self.setWhatsThis("It's a dialog box that allows you to enter data for your task.")
            self.user_input_task_name.setWhatsThis("It's an input field for the task name.")
            self.user_input_task_deadline.setWhatsThis("It's a field displaying the task deadline.")
            self.user_input_task_description.setWhatsThis("It's a field for entering the task description.")
            self.send_button.setWhatsThis("It's a Send button to submit the task data.")
            self.cancel_button.setWhatsThis("It's a Cancel button to close the window and discard the task.")
        else:
            self.setWhatsThis("It's a message box containing task information.")
            self.user_input_task_name.setWhatsThis("It's the task name.")
            self.user_input_task_deadline.setWhatsThis("It's the task deadline.")
            self.user_input_task_description.setWhatsThis("It's the task description.")
            self.OK_Button.setWhatsThis("It's an OK button to close message box.")

        self.visual_changer.apply_dark_theme()
        self.show()