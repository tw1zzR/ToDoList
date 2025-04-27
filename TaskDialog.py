from core.task_window_theme_manager import TaskWindowThemeManager
from modules.window_builders import task_window_builder
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


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
        task_window_builder.setup_ui(self)
        self.visual_changer.apply_dark_theme()
        self.show()