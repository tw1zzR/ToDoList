from modules.TaskInputDialog import dialog_tools
from PyQt5.QtGui import *

def setup_UI(task_input_dialog, title):
    setup_task_input_dialog(task_input_dialog, title)
    setup_input_fields(task_input_dialog)
    setup_connections(task_input_dialog)
    setup_button_layout(task_input_dialog)
    setup_main_layout(task_input_dialog)
    setup_what_this_button(task_input_dialog)
    setup_object_names(task_input_dialog)

def setup_task_input_dialog(task_input_dialog, title):
    task_input_dialog.setWindowTitle(title)
    task_input_dialog.setWindowIcon(QIcon("assets/TaskInputDialog/addtask_dialogbox_icon.png"))
    task_input_dialog.resize(520, 600)

def setup_input_fields(task_input_dialog):
    task_input_dialog.user_input_task_name.setMaxLength(24)
    task_input_dialog.user_input_task_name.setPlaceholderText("Enter task name")

    task_input_dialog.user_input_task_deadline.setDateTime(task_input_dialog.current_time)
    task_input_dialog.user_input_task_deadline.setMinimumDateTime(task_input_dialog.current_time)

    task_input_dialog.user_input_task_description.setPlaceholderText("Enter task description")

    task_input_dialog.user_input_task_name.setMinimumHeight(50)
    task_input_dialog.user_input_task_deadline.setMinimumHeight(50)
    task_input_dialog.user_input_task_description.setMinimumHeight(50)

def setup_connections(task_input_dialog):
    task_input_dialog.user_input_task_description.textChanged.connect(lambda: dialog_tools.limit_max_chars_in_textedit(task_input_dialog))
    task_input_dialog.send_button.clicked.connect(lambda: dialog_tools.get_task_data(task_input_dialog))
    task_input_dialog.cancel_button.clicked.connect(task_input_dialog.reject)

def setup_button_layout(task_input_dialog):
    task_input_dialog.button_layout.setContentsMargins(0, 0, 0, 0)
    task_input_dialog.button_layout.setSpacing(0)

    task_input_dialog.button_layout.addWidget(task_input_dialog.send_button)
    task_input_dialog.button_layout.addSpacing(5)
    task_input_dialog.button_layout.addWidget(task_input_dialog.cancel_button)

    task_input_dialog.button_widget.setLayout(task_input_dialog.button_layout)

def setup_main_layout(task_input_dialog):
    task_input_dialog.main_layout.setContentsMargins(50, 50, 50, 50)
    task_input_dialog.main_layout.setSpacing(0)

    task_input_dialog.main_layout.addWidget(task_input_dialog.task_name_label)
    task_input_dialog.main_layout.addWidget(task_input_dialog.user_input_task_name)
    task_input_dialog.main_layout.addSpacing(25)

    task_input_dialog.main_layout.addWidget(task_input_dialog.task_deadline_label)
    task_input_dialog.main_layout.addWidget(task_input_dialog.user_input_task_deadline)
    task_input_dialog.main_layout.addSpacing(25)

    task_input_dialog.main_layout.addWidget(task_input_dialog.task_description_label)
    task_input_dialog.main_layout.addWidget(task_input_dialog.user_input_task_description)
    task_input_dialog.main_layout.addSpacing(25)

    task_input_dialog.main_layout.addWidget(task_input_dialog.button_widget)

    task_input_dialog.setLayout(task_input_dialog.main_layout)

def setup_what_this_button(task_input_dialog):
    task_input_dialog.setWhatsThis("It's a dialog box that allows you to enter data for your task.")
    task_input_dialog.user_input_task_name.setWhatsThis("It's an input field for the task name.")
    task_input_dialog.user_input_task_deadline.setWhatsThis("It's a field displaying the task deadline.")
    task_input_dialog.user_input_task_description.setWhatsThis("It's a field for entering the task description.")
    task_input_dialog.send_button.setWhatsThis("It's a Send button to submit the task data.")
    task_input_dialog.cancel_button.setWhatsThis("It's a Cancel button to close the window and discard the task.")

def setup_object_names(task_input_dialog):
    task_input_dialog.task_name_label.setObjectName("task_name_label")
    task_input_dialog.task_deadline_label.setObjectName("task_deadline_label")
    task_input_dialog.task_description_label.setObjectName("task_description_label")
    task_input_dialog.user_input_task_name.setObjectName("user_input_task_name")
    task_input_dialog.user_input_task_deadline.setObjectName("user_input_task_deadline")
    task_input_dialog.user_input_task_description.setObjectName("user_input_task_description")
    task_input_dialog.send_button.setObjectName("send_button")
    task_input_dialog.cancel_button.setObjectName("cancel_button")