from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from modules.MainWindow import main_window_tools


class TaskCheckboxManager:

    def __init__(self, main_window):
        self.main_window = main_window
        self.comp_mgr = self.main_window.checkbox_elems_builder

    def refresh_ui_task_checkboxes(self):
        main_window_tools.clear_layout(self.main_window.tasks_layout)

        tasks_title = self.build_tasks_title()
        self.main_window.tasks_layout.addLayout(tasks_title)

        for task_item in self.main_window.tasks_data.task_items:
            new_task_layout = self.create_task_item_layout(task_item)
            self.main_window.tasks_layout.addLayout(new_task_layout)

        plus_button_layout = self.build_plus_button_layout()
        self.main_window.tasks_layout.addLayout(plus_button_layout)

        self.main_window.show()


        # self.comp_mgr.create_completed_task_button_layout()
        #
        # if self.main_window.completed_checkbox_dict:
        #     self.main_window.completed_task_open_button.show()
        # else:
        #     self.main_window.completed_task_open_button.hide()

    def create_task_item_layout(self, task_item):
        task_layout = QHBoxLayout()
        task_layout.setContentsMargins(0, 0, 0, 0)
        task_layout.setSpacing(0)

        # Reorder buttons
        reorder_layout = QVBoxLayout()
        for button in task_item.reorder_buttons:
            button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            button.show()
            reorder_layout.addWidget(button)
        task_layout.addLayout(reorder_layout)

        # Checkbox
        task_item.checkbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        task_layout.addWidget(task_item.checkbox)

        # Action buttons
        for button in task_item.checkbox_buttons:
            button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            button.show()
            task_layout.addWidget(button)

        task_layout.addSpacing(50)

        return task_layout



    def build_tasks_title(self):
        tasks_title = QHBoxLayout()
        tasks_title.addStretch()
        tasks_title.addWidget(self.main_window.title_tasks_label, alignment=Qt.AlignCenter)
        tasks_title.addStretch()

        return tasks_title

    def build_task_layout(self, task_item):

        # Reorder buttons
        reorder_layout = QVBoxLayout()
        for button in task_item.reorder_buttons:
            button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            button.show()
            reorder_layout.addWidget(button)
        task_item.checkbox_layout.addLayout(reorder_layout)

        # Checkbox
        task_item.checkbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        task_item.checkbox_layout.addWidget(task_item.checkbox)

        # Action buttons
        for button in task_item.checkbox_buttons:
            button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            button.show()
            task_item.checkbox_layout.addWidget(button)

        task_item.checkbox_layout.addSpacing(50)

        return task_item.checkbox_layout

    def build_plus_button_layout(self):
        plus_button_layout = QHBoxLayout()
        plus_button_layout.addSpacing(50)
        plus_button_layout.addWidget(self.main_window.add_task_plus_button, alignment=Qt.AlignLeft)
        plus_button_layout.addStretch()

        self.main_window.add_task_plus_button.setFixedSize(50, 50)

        return plus_button_layout




    def create_completed_task_button_layout(self):
        completed_tasks_button_layout = QHBoxLayout()
        completed_tasks_button_layout.addSpacing(50)
        completed_tasks_button_layout.addWidget(self.main_window.completed_task_open_button, alignment=Qt.AlignCenter)
        completed_tasks_button_layout.addSpacing(50)

        self.main_window.completed_task_open_button.hide()
        self.main_window.tasks_layout.addLayout(completed_tasks_button_layout)





    def show_all_task_checkboxes(self):
        main_window_tools.clear_layout(self.main_window.tasks_layout)

        self.comp_mgr.create_title_and_task_layouts()
        self.comp_mgr.create_plus_button_layout()
        self.comp_mgr.create_completed_task_button_layout()

        if self.main_window.completed_checkbox_dict:
            self.main_window.completed_task_open_button.show()
        else:
            self.main_window.completed_task_open_button.hide()

        self.main_window.show()

    def show_completed_tasks(self):
        for checkbox, data in self.main_window.completed_checkbox_dict.items():

            if "checkbox_layout" in data:
                continue

            checkbox_layout = self.comp_mgr.create_completed_task_layout(checkbox, data)
            data["checkbox_layout"] = checkbox_layout
            self.main_window.tasks_layout.addLayout(checkbox_layout)
            self.main_window.show()

    def move_up_down_checkbox(self, target_checkbox, up_down):
        try:
            i = self.main_window.checkbox_order.index(target_checkbox)
        except ValueError:
            return

        if up_down == "up" and i == 0:
            return
        elif up_down == "down" and i == len(self.main_window.checkbox_order) - 1 :
            return

        if up_down == "up":
            self.main_window.checkbox_order[i-1], self.main_window.checkbox_order[i] = self.main_window.checkbox_order[i], self.main_window.checkbox_order[i-1]
        elif up_down == "down":
            self.main_window.checkbox_order[i+1], self.main_window.checkbox_order[i] = self.main_window.checkbox_order[i], self.main_window.checkbox_order[i+1]

        self.delete_completed_tasks_from_ui()

        self.show_all_task_checkboxes()
        if self.main_window.completed_task_opened:
            self.show_completed_tasks()

    def delete_task_checkbox_with_buttons(self, checkbox_sender, *dicts):
        for dictionary in dicts:
            if checkbox_sender in dictionary:
                checkbox_data = dictionary[checkbox_sender]

                for button in checkbox_data["buttons"] + checkbox_data["reorder_buttons"]:
                    button.setParent(None)
                    button.deleteLater()

                checkbox_sender.setParent(None)
                checkbox_sender.deleteLater()

                self.main_window.checkbox_order.remove(checkbox_sender)
                del dictionary[checkbox_sender]
                break

        self.delete_completed_tasks_button()

    def delete_completed_tasks_from_ui(self):
        for checkbox, data in self.main_window.completed_checkbox_dict.items():
            checkbox_layout = data.get("checkbox_layout")
            if checkbox_layout:
                while checkbox_layout.count():
                    item = checkbox_layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.hide()

                self.main_window.tasks_layout.removeItem(checkbox_layout)
                del data["checkbox_layout"]

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
        if completed_task_checkbox in self.main_window.checkbox_order:
            checkbox_index  = self.main_window.checkbox_order.index(completed_task_checkbox)
            checkbox_key = self.main_window.checkbox_order[checkbox_index]

            completed_task_checkbox_data = from_dict.pop(checkbox_key)
            to_dict[completed_task_checkbox] = completed_task_checkbox_data