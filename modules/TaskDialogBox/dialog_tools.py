from PyQt5.QtGui import QTextCursor
from modules import global_tools

def get_task_data(task_dialog):
    user_task_name = task_dialog.user_input_task_name.text()
    user_task_deadline = task_dialog.user_input_task_deadline.text()
    user_task_description = task_dialog.user_input_task_description.toPlainText()

    if user_task_name.strip():
        task_dialog.accept()

        return user_task_name, user_task_deadline, user_task_description
    else:
        empty_task_name_msgbox = global_tools.create_warning_messagebox(task_dialog, "About App", "Task name cannot be blank.")
        empty_task_name_msgbox.exec_()

def limit_max_chars_in_textedit(task_dialog):
    text_chars = task_dialog.user_input_task_description.toPlainText()

    if len(text_chars) > task_dialog.max_chars:
        task_dialog.user_input_task_description.setPlainText(text_chars[:task_dialog.max_chars])
        task_dialog.user_input_task_description.moveCursor(QTextCursor.End)