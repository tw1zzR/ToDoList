from core.TaskInfoDialog.change_visual_ui import ChangeVisualUI
from modules.TaskInfoDialog import task_display_tools, task_info_dialog_builder
from PyQt5.QtWidgets import *


class TaskInfoDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.visual_changer = ChangeVisualUI(self)

        self.main_layout = QVBoxLayout()
        self.dark_theme = True

        self.task_name_label = QLabel("Name:", self)
        self.task_deadline_label = QLabel("Deadline:", self)
        self.task_description_label = QLabel("Description:", self)

        self.user_input_task_name = QLabel(self)
        self.user_input_task_deadline = QLabel(self)
        self.user_input_task_description = QTextEdit(self)

        self.OK_Button = QPushButton("OK", self)

        # Init UI
        task_info_dialog_builder.setup_UI(self)
        self.visual_changer.change_UI_theme()
        self.show()