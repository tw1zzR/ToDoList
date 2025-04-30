from modules.global_tools import get_task_from_dialog
from PyQt5.QtCore import QDateTime

def update_window_fields(task_window, task_info=None, is_add=False):
    if task_info is not None:
        name = task_info.name
        deadline = QDateTime.fromString(task_info.deadline, "dd.MM.yyyy HH:mm")
        description = task_info.description
    else:
        name = deadline = description = ""

    # Set Deadline
    if task_window.is_input:
        if is_add:
            deadline = QDateTime.currentDateTime()
        else:
            task_window.user_input_task_deadline.setMinimumDateTime(deadline)

    task_window.user_input_task_deadline.setDateTime(deadline)

    # Set task data
    task_window.user_input_task_name.setText(name)
    task_window.user_input_task_description.setText(description)

    task_window.update()

def edit_task_data(task_window, task_item, task_items):
    edited_task_name, edited_task_deadline, edited_task_description = get_task_from_dialog(task_window)

    for task in task_items:
        if task_item == task:
            task_item.task.name = edited_task_name
            task_item.task.deadline = edited_task_deadline
            task_item.task.description = edited_task_description

    task_item.checkbox.setText(edited_task_name)