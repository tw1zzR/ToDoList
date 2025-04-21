from collections import OrderedDict
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class TaskCheckboxManager:

    def __init__(self, main_window):
        self.main_window = main_window


    def show_all_task_checkboxes(self):
        self.main_window.clear_layout(self.main_window.tasks_layout)

        title_tasks_layout = QHBoxLayout()

        title_tasks_layout.addStretch()
        title_tasks_layout.addWidget(self.main_window.title_tasks_label, alignment=Qt.AlignCenter)
        title_tasks_layout.addStretch()

        self.main_window.tasks_layout.addLayout(title_tasks_layout)

        for checkbox, data in self.main_window.checkbox_dict.items():

            checkbox_layout = QHBoxLayout()
            checkbox_layout.setContentsMargins(0,0,0,0)
            checkbox_layout.setSpacing(0)

            moveup_btn = data["reorder_buttons"][0]
            movedown_btn = data["reorder_buttons"][1]

            reorder_layout = QVBoxLayout()

            for reorder_button in [moveup_btn, movedown_btn]:
                reorder_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                reorder_button.show()
                reorder_layout.addWidget(reorder_button)

            checkbox_layout.addLayout(reorder_layout)

            checkbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            checkbox_layout.addWidget(checkbox)

            for button in data["buttons"]:
                button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                button.show()
                checkbox_layout.addWidget(button)
            checkbox_layout.addSpacing(50)

            data["checkbox_layout"] = checkbox_layout

            self.main_window.tasks_layout.addLayout(checkbox_layout)

        # (+) button layout
        plus_button_layout = QHBoxLayout()

        plus_button_layout.addSpacing(50)
        plus_button_layout.addWidget(self.main_window.add_task_plus_button, alignment=Qt.AlignLeft)
        plus_button_layout.addStretch()

        self.main_window.add_task_plus_button.setFixedSize(50, 50)
        self.main_window.tasks_layout.addLayout(plus_button_layout)

        # test
        completed_tasks_button_layout = QHBoxLayout()

        completed_tasks_button_layout.addSpacing(50)
        completed_tasks_button_layout.addWidget(self.main_window.completed_task_open_button, alignment=Qt.AlignCenter)
        completed_tasks_button_layout.addSpacing(50)

        self.main_window.completed_task_open_button.hide()

        if self.main_window.completed_checkbox_dict:
            self.main_window.completed_task_open_button.show()

        self.main_window.tasks_layout.addLayout(completed_tasks_button_layout)
        # ---

        self.main_window.set_statusbar_over_all_widgets()


    def show_completed_tasks(self):
        for checkbox, data in self.main_window.completed_checkbox_dict.items():

            if "checkbox_layout" in data:
                continue

            checkbox_layout = QHBoxLayout()
            checkbox_layout.setContentsMargins(0, 0, 0, 0)
            checkbox_layout.setSpacing(0)

            checkbox_layout.addSpacing(50)

            checkbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            checkbox.show()
            checkbox_layout.addWidget(checkbox)

            for reorder_button in data["reorder_buttons"]:
                reorder_button.hide()

            for button in data["buttons"]:
                button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                button.show()
                checkbox_layout.addWidget(button)

            checkbox_layout.addSpacing(50)

            data["checkbox_layout"] = checkbox_layout

            self.main_window.tasks_layout.addLayout(checkbox_layout)


    def move_up_down_checkbox(self, target_checkbox, up_down):
        items = list(self.main_window.checkbox_dict.items())

        for i, (checkbox, _) in enumerate(items):
            if checkbox is target_checkbox:
                break

        if i == 0 and up_down == "up":
            return
        elif i == len(items) - 1 and up_down == "down":
            return

        match up_down:
            case "up":
                items[i-1], items[i] = items[i], items[i-1]
            case "down":
                items[i+1], items[i] = items[i], items[i+1]

        self.main_window.checkbox_dict = OrderedDict(items)
        self.show_all_task_checkboxes()


    def delete_task_checkbox_with_buttons(self, checkbox_sender, *dicts):
        for dictionary in dicts:
            if checkbox_sender in dictionary:
                checkbox_data = dictionary[checkbox_sender]

                checkbox_buttons = checkbox_data["buttons"]
                reorder_buttons = checkbox_data["reorder_buttons"]

                for button in checkbox_buttons[:]:
                    button.setParent(None)
                    button.deleteLater()
                for reorder_button in reorder_buttons[:]:
                    reorder_button.setParent(None)
                    reorder_button.deleteLater()

                checkbox_sender.setParent(None)
                checkbox_sender.deleteLater()

                del dictionary[checkbox_sender]
                break


    def delete_completed_tasks_from_ui(self):
        for checkbox, data in self.main_window.completed_checkbox_dict.items():
            layout = data.get("checkbox_layout")
            if layout:
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.hide()

                self.main_window.tasks_layout.removeItem(layout)
                del  data["checkbox_layout"]


    def remove_completed_task_from_ui(self, sender_checkbox):
        for checkbox, data in self.main_window.completed_checkbox_dict.items():
            if checkbox is sender_checkbox:
                checkbox_layout = data.get("checkbox_layout")
                if checkbox_layout:
                    while checkbox_layout.count():
                        item = checkbox_layout.takeAt(0)
                        widget = item.widget()
                        if widget:
                            widget.hide()

                for reorder_button in data["reorder_buttons"]:
                    reorder_button.hide()

                self.main_window.tasks_layout.removeItem(checkbox_layout)
                del data["checkbox_layout"]


    def delete_completed_tasks_button(self):
        self.main_window.tasks_layout.removeWidget(self.main_window.completed_task_open_button)
        self.main_window.completed_task_open_button.setParent(None)
        self.main_window.update()


    def move_task_to_another_dict(self, completed_task_checkbox, from_dict, to_dict):
        completed_task_checkbox_data = from_dict.pop(completed_task_checkbox)
        to_dict[completed_task_checkbox] = completed_task_checkbox_data