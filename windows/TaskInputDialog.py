from core.TaskInputDialog.change_visual_ui import ChangeVisualUI
from modules.TaskInputDialog import task_input_dialog_builder
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class TaskInputDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.visual_changer = ChangeVisualUI(self)

        self.dark_theme = True
        self.current_time = QDateTime.currentDateTime()
        self.max_chars = 150

        self.main_layout = QVBoxLayout()
        self.button_widget = QWidget(self)
        self.button_layout = QHBoxLayout(self.button_widget)

        self.task_name_label = QLabel("Task name", self)
        self.task_deadline_label = QLabel("Deadline", self)
        self.task_description_label = QLabel("Task Description", self)

        self.user_input_task_name = QLineEdit(self)
        self.user_input_task_deadline = QDateTimeEdit(self)
        self.user_input_task_description = QTextEdit(self)

        self.send_button = QPushButton("SEND")
        self.cancel_button = QPushButton("CANCEL")

        # Init UI
        task_input_dialog_builder.setup_UI(self)
        self.visual_changer.change_UI_theme()
        self.show()