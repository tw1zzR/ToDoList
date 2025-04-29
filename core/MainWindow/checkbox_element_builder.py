from modules.MainWindow import main_window_tools
from modules import global_tools
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class CheckboxElementBuilder:

    def __init__(self, main_window):
        self.main_window = main_window
        self.visual_mgr = self.main_window.visual_changer

    def create_checkbox_with_buttons(self, task_name):
        checkbox = QCheckBox(task_name)
        checkbox.stateChanged.connect(self.main_window.on_click_controller.on_click_task_checkbox)
        checkbox.setFixedHeight(50)

        checkbox_buttons = self.create_checkbox_buttons()
        reorder_buttons = self.create_reorder_buttons()

        return checkbox, checkbox_buttons, reorder_buttons

    def create_reorder_buttons(self):
        moveup_button = QPushButton(self.main_window)
        movedown_button = QPushButton(self.main_window)
        for button in [moveup_button, movedown_button]:
            button.setFixedSize(50, 25)
            button.setStyleSheet("background-color: transparent;")
        return [moveup_button, movedown_button]

    def create_checkbox_buttons(self):
        task_info_button = QPushButton(self.main_window)
        edit_task_button = QPushButton(self.main_window)
        delete_task_button = QPushButton(self.main_window)

        for button in [task_info_button, edit_task_button, delete_task_button]:
            button.setFixedSize(50, 50)
            button.setIconSize(QSize(30, 30))
            global_tools.set_default_widget_style(button, self.main_window)

        task_info_button.setToolTip("View task details")
        edit_task_button.setToolTip("Edit task")
        delete_task_button.setToolTip("Delete task")

        return [task_info_button, edit_task_button, delete_task_button]




    # Show completed tasks methods
    def create_completed_task_layout(self, task_item):
        checkbox_layout = QHBoxLayout()
        checkbox_layout.setContentsMargins(0, 0, 0, 0)
        checkbox_layout.setSpacing(0)
        checkbox_layout.addSpacing(50)

        task_item.checkbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        task_item.checkbox.show()
        checkbox_layout.addWidget(task_item.checkbox)

        for reorder_button in task_item.reorder_buttons:
            reorder_button.hide()
        for button in task_item.buttons:
            button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            button.show()
            checkbox_layout.addWidget(button)

        checkbox_layout.addSpacing(50)
        return checkbox_layout