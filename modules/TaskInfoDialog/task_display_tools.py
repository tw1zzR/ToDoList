from PyQt5.QtCore import Qt

def set_task_info_msgbox_new_data(task_info_dialog, task_name, task_deadline, task_description):
    task_info_dialog.user_input_task_name.setText(task_name)
    task_info_dialog.user_input_task_deadline.setText(task_deadline)
    task_info_dialog.user_input_task_description.setText(task_description)

    task_info_dialog.user_input_task_description.setAlignment(Qt.AlignCenter)