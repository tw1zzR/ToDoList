from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from modules.TaskDialogBox import dialog_tools


def setup_UI(task_dialog):
    setup_task_dialog(task_dialog)
    setup_connections(task_dialog)
    setup_what_this_button(task_dialog)
    setup_object_names(task_dialog)

def setup_task_dialog(task_dialog):
    task_dialog.setWindowTitle("Add Task")
    task_dialog.setWindowIcon(QIcon("assets/TaskDialogBox/addtask_dialogbox_icon.png"))
    task_dialog.resize(520, 600)

def setup_connections(task_dialog):
    task_dialog.user_input_task_description.textChanged.connect(lambda: dialog_tools.limit_max_chars_in_textedit(task_dialog))
    task_dialog.send_button.clicked.connect(lambda: dialog_tools.get_task_data(task_dialog))
    task_dialog.cancel_button.clicked.connect(task_dialog.reject)

def setup_what_this_button(task_dialog):
    task_dialog.setWhatsThis("It's a dialog box that allows you to enter data for your task.")
    task_dialog.user_input_task_name.setWhatsThis("It's an input field for the task name.")
    task_dialog.user_input_task_deadline.setWhatsThis("It's a field displaying the task deadline.")
    task_dialog.user_input_task_description.setWhatsThis("It's a field for entering the task description.")
    task_dialog.send_button.setWhatsThis("It's a Send button to submit the task data.")
    task_dialog.cancel_button.setWhatsThis("It's a Cancel button to close the window and discard the task.")

def setup_object_names(task_dialog):
    task_dialog.task_name_label.setObjectName("task_name_label")
    task_dialog.task_deadline_label.setObjectName("task_deadline_label")
    task_dialog.task_description_label.setObjectName("task_description_label")
    task_dialog.user_input_task_name.setObjectName("user_input_task_name")
    task_dialog.user_input_task_deadline.setObjectName("user_input_task_deadline")
    task_dialog.user_input_task_description.setObjectName("user_input_task_description")
    task_dialog.send_button.setObjectName("send_button")
    task_dialog.cancel_button.setObjectName("cancel_button")