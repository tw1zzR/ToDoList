from modules.global_tools import clear_layout
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class TaskCheckboxManager:

    def __init__(self, main_window):
        self.main_window = main_window

    # Show uncompleted tasks method + completed task btn
    def refresh_ui_task_checkboxes(self):
        clear_layout(self.main_window.tasks_layout)

        tasks_title = self.build_tasks_title()
        self.main_window.tasks_layout.addLayout(tasks_title)

        for task_item in self.main_window.tasks_data.uncompleted_task_items:
            new_task_layout = self.build_task_item_layout(task_item)
            task_item.checkbox_layout = new_task_layout
            self.main_window.tasks_layout.addLayout(new_task_layout)

        plus_button_layout = self.build_plus_button()
        self.main_window.tasks_layout.addLayout(plus_button_layout)

        completed_tasks_button_layout = self.build_completed_task_button()
        self.main_window.tasks_layout.addLayout(completed_tasks_button_layout)

        if self.main_window.tasks_data.completed_task_items:
            self.main_window.completed_task_open_button.show()

            if self.main_window.completed_task_opened:
                self.show_completed_tasks()
        else:
            self.main_window.completed_task_open_button.hide()

        self.main_window.show()

    def build_task_item_layout(self, task_item):
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

    def build_plus_button(self):
        plus_button_layout = QHBoxLayout()
        plus_button_layout.addSpacing(50)
        plus_button_layout.addWidget(self.main_window.add_task_plus_button, alignment=Qt.AlignLeft)
        plus_button_layout.addStretch()
        return plus_button_layout

    def build_completed_task_button(self):
        completed_tasks_button_layout = QHBoxLayout()
        completed_tasks_button_layout.addSpacing(50)
        completed_tasks_button_layout.addWidget(self.main_window.completed_task_open_button, alignment=Qt.AlignCenter)
        completed_tasks_button_layout.addSpacing(50)
        return completed_tasks_button_layout

    # Show completed task methods
    def show_completed_tasks(self):

        for task_item in self.main_window.tasks_data.completed_task_items:

            if task_item.checkbox_layout is not None:
                continue

            checkbox_layout = self.create_completed_task_layout(task_item)

            self.main_window.tasks_layout.addLayout(checkbox_layout)
            self.main_window.show()

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
        for button in task_item.checkbox_buttons:
            button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            button.show()
            checkbox_layout.addWidget(button)

        checkbox_layout.addSpacing(50)

        task_item.checkbox_layout = checkbox_layout
        return checkbox_layout


    def move_up_down_checkbox(self, task_item, up_down):
        tasks_list = self.main_window.tasks_data.uncompleted_task_items

        try:
            i = tasks_list.index(task_item)
        except ValueError:
            return

        if up_down == "up" and i == 0:
            print("above")
            return
        elif up_down == "down" and i == len(tasks_list) - 1 :
            print("below")
            return

        if up_down == "up":
            tasks_list[i-1], tasks_list[i] = tasks_list[i], tasks_list[i-1]
        elif up_down == "down":
            tasks_list[i+1], tasks_list[i] = tasks_list[i], tasks_list[i+1]

        self.refresh_ui_task_checkboxes()
        if self.main_window.tasks_data.completed_task_items and self.main_window.completed_task_opened:
            self.main_window.task_checkbox_manager.delete_completed_tasks_from_ui()
            self.main_window.task_checkbox_manager.show_completed_tasks()

    def delete_task_item(self, task_item, *task_lists):
        for task_list in task_lists:
            if task_item in task_list:

                for button in task_item.checkbox_buttons + task_item.reorder_buttons:
                    button.setParent(None)
                    button.deleteLater()

                task_item.checkbox.setParent(None)
                task_item.checkbox.deleteLater()

                task_list.remove(task_item)

        if not task_lists[0]:
            self.delete_completed_tasks_button()
            self.main_window.update()

    def delete_completed_tasks_from_ui(self):
        for task_item in self.main_window.tasks_data.completed_task_items:
            checkbox_layout = task_item.checkbox_layout

            if checkbox_layout:
                while checkbox_layout.count():
                    item = checkbox_layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.hide()
                    else:
                        inner_layout = item.layout()
                        if inner_layout:
                            while inner_layout.count():
                                inner_item = inner_layout.takeAt(0)
                                inner_widget = inner_item.widget()
                                if inner_widget:
                                    inner_widget.hide()
                            inner_layout.setEnabled(False)

                self.main_window.tasks_layout.removeItem(checkbox_layout)
                task_item.checkbox_layout = None

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