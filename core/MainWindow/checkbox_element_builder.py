from modules import global_tools
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class CheckboxElementBuilder:

    def __init__(self, main_window):
        self.main_window = main_window

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

    def connect_checkbox_buttons(self):
        on_click_mgr = self.main_window.on_click_controller

        def connect_button(button, handler):
            if not hasattr(button, "_clicked_connected"):
                button.clicked.connect(handler)
                button._clicked_connected = True

        for task_item in self.main_window.tasks_data.task_items:
            task_info_button, edit_task_button, delete_task_button = task_item.checkbox_buttons
            reorder_buttons = task_item.reorder_buttons

            connect_button(task_info_button, on_click_mgr.on_click_task_info_checkbox_button)
            connect_button(edit_task_button, on_click_mgr.on_click_edit_task_checkbox_button)
            connect_button(delete_task_button, on_click_mgr.on_click_delete_task_checkbox_button)

            for button in reorder_buttons:
                connect_button(button, on_click_mgr.on_click_reorder_button)