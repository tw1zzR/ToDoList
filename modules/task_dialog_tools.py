from PyQt5.QtWidgets import QMessageBox
from modules import global_tools

def get_task_data(task_input_dialog):
    user_task_name = task_input_dialog.user_input_task_name.text()
    user_task_deadline = task_input_dialog.user_input_task_deadline.text()
    user_task_description = task_input_dialog.user_input_task_description.toPlainText()

    if user_task_name.strip():
        task_input_dialog.accept()

        return user_task_name, user_task_deadline, user_task_description
    else:
        empty_task_name_msgbox = global_tools.create_messagebox("Task Error",
                                                                "Task name cannot be blank.",
                                                                QMessageBox.Warning,
                                                                "assets/warning_icon_1.png")
        empty_task_name_msgbox.exec_()