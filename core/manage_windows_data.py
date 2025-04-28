from modules.TaskDialog.dialog_tools import get_task_data
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

    if task_deadline:
        task_deadline_datetime = QDateTime.fromString(task_deadline, "dd.MM.yyyy HH:mm")
    else:
        task_deadline_datetime = QDateTime.currentDateTime()

    task_window.user_input_task_deadline.setMinimumDateTime(task_deadline_datetime)
    task_window.user_input_task_deadline.setDateTime(task_deadline_datetime)

    task_window.user_input_task_name.setText(task_name)
    task_window.user_input_task_description.setText(task_description)

    task_window.update()

def update_opened_task_info_window(task_window, checkbox, *dicts):
    task_info = None

    for dictionary in dicts:
        if checkbox in dictionary :
            task_data = dictionary[checkbox]

            task_info = {
                "name": task_data["name"],
                "deadline": task_data["deadline"],
                "description": task_data["description"]
            }

    update_window_fields(task_window, task_info)

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