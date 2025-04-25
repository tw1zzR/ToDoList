from PyQt5.QtCore import Qt

from modules.TaskInputDialog.dialog_tools import get_task_data
from windows.TaskInputDialog import TaskInputDialog
from PyQt5.QtCore import QDateTime

def update_window_fields(task_window, task_info=None):
    if isinstance(task_info, dict):
        task_name = task_info.get("name", "")
        task_deadline = task_info.get("deadline", "")
        task_description = task_info.get("description", "")
    else:
        task_name = ""
        task_deadline = ""
        task_description = ""

    if isinstance(task_window, TaskInputDialog):
        if task_deadline:
            task_deadline_datetime = QDateTime.fromString(task_deadline, "MM-dd-yyyy HH:mm")
            task_window.user_input_task_deadline.setMinimumDateTime(task_deadline_datetime)

            task_window.user_input_task_deadline.setDateTime(task_deadline_datetime)
        else:
            task_window.user_input_task_deadline.setMinimumDateTime(QDateTime())

    else:
        task_window.user_input_task_deadline.setText(task_deadline)

    task_window.user_input_task_name.setText(task_name)
    task_window.user_input_task_description.setText(task_description)

    task_window.user_input_task_description.setAlignment(Qt.AlignCenter)
    task_window.update()

def edit_task_data(task_window, checkbox, *dicts):
    edited_task_name, edited_task_deadline, edited_task_description = get_task_data(task_window)

    for dictionary in dicts:
        if checkbox in dictionary:
            dictionary[checkbox].update({
                "name": edited_task_name,
                "deadline": edited_task_deadline,
                "description": edited_task_description
            })
            break

    checkbox.setText(edited_task_name)