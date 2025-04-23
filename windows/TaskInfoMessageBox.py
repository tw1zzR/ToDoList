from core.TaskInfoMessageBox.change_visual_ui import ChangeVisualUI
from modules.TaskInfoMessageBox import task_display_tools, task_info_dialog_builder
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class CustomTaskInfoMessageBox(QDialog):
    def __init__(self, task_name, task_deadline, task_description):
        super().__init__()
        self.visual_changer = ChangeVisualUI(self)

        self.main_layout = QVBoxLayout()
        self.dark_theme = True

        self.task_name_label = QLabel("Name:", self)
        self.task_deadline_label = QLabel("Deadline:", self)
        self.task_description_label = QLabel("Description:", self)

        self.user_task_name_label = QLabel(self)
        self.user_task_deadline_label = QLabel(self)
        self.user_task_description_textedit = QTextEdit(self)

        self.OK_Button = QPushButton("OK", self)

        task_display_tools.set_task_info_msgbox_new_data(self, task_name, task_deadline, task_description)

        self.initUI()

    def initUI(self):
        task_info_dialog_builder.setup_UI(self)
        self.visual_changer.change_UI_theme()
        self.show()