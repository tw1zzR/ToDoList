from PyQt5.QtCore import Qt, QLine, QDateTime
from PyQt5.QtWidgets import QWidget, QLineEdit, QTextEdit
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
            # Если task_deadline пустое, не устанавливаем минимальную дату/время
            task_window.user_input_task_deadline.setMinimumDateTime(QDateTime())

    else:
        # Если не TaskInputDialog, используем setText для поля deadline
        task_window.user_input_task_deadline.setText(task_deadline)

    # Устанавливаем остальные данные в поля
    task_window.user_input_task_name.setText(task_name)
    task_window.user_input_task_description.setText(task_description)

    # Устанавливаем выравнивание для описания
    task_window.user_input_task_description.setAlignment(Qt.AlignCenter)
    task_window.update()
