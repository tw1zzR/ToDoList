from modules.TaskDialog.dialog_tools import get_task_data
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


# def update_window_fields(task_window, task_info=None):
#     if isinstance(task_info, dict):
#         task_name = task_info.get("name", "")
#         task_deadline = task_info.get("deadline", "")
#         task_description = task_info.get("description", "")
#     else:
#         task_name = ""
#         task_deadline = ""
#         task_description = ""
#
#     if task_deadline:
#         task_deadline_datetime = QDateTime.fromString(task_deadline, "dd.MM.yyyy HH:mm")
#     else:
#         task_deadline_datetime = QDateTime.currentDateTime()
#
#     task_window.user_input_task_deadline.setMinimumDateTime(task_deadline_datetime)
#     task_window.user_input_task_deadline.setDateTime(task_deadline_datetime)
#
#     task_window.user_input_task_name.setText(task_name)
#     task_window.user_input_task_description.setText(task_description)
#
#     task_window.update()

# def update_opened_task_info_window(task_window, task_item):
#     task_item.task.name
#     task_item.task.deadline
#     task_item.task.description
#
#
#     update_window_fields(task_window,)

def edit_task_data(task_window, task_item, task_items):
    edited_task_name, edited_task_deadline, edited_task_description = get_task_data(task_window)

    for task in task_items:
        if task_item == task:
            task_item.task.name = edited_task_name
            task_item.task.deadline = edited_task_deadline
            task_item.task.description = edited_task_description

    task_item.checkbox.setText(edited_task_name)