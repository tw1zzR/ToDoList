from PyQt5.QtCore import Qt

def set_task_info_msgbox_new_data(task_info_dialog, task_name, task_deadline, task_description):
    task_info_dialog.task_name = task_name
    task_info_dialog.task_deadline = task_deadline
    task_info_dialog.task_description = task_description

    task_info_dialog.user_task_name_label.setText(task_name)
    task_info_dialog.user_task_deadline_label.setText(task_deadline)
    task_info_dialog.user_task_description_textedit.setText(task_description)

    task_info_dialog.user_task_description_textedit.setAlignment(Qt.AlignCenter)