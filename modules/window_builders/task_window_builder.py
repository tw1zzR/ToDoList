from modules.task_dialog_tools import get_task_data, limit_max_chars_in_textedit
from PyQt5.QtCore import *
from PyQt5.QtGui import *

def setup_ui(task_window):
    setup_window(task_window)
    setup_layouts(task_window)
    setup_connections(task_window)
    setup_fields(task_window)
    setup_object_sizes(task_window)
    setup_object_names(task_window)
    setup_whats_this(task_window)

def setup_window(task_window):
    task_window.setWindowTitle("Task")
    task_window.resize(520, 600)

    if task_window.is_input:
        task_window.setWindowIcon(QIcon("assets/TaskInputDialog/addtask_dialogbox_icon.png"))
    else:
        task_window.setWindowIcon(QIcon("assets/TaskInfoDialog/gray_task_info_button_V2_icon.png"))

def setup_layouts(task_window):
    task_window.main_layout.setContentsMargins(50, 50, 50, 50)
    task_window.main_layout.setSpacing(0)

    task_window.main_layout.addWidget(task_window.task_name_label)
    task_window.main_layout.addWidget(task_window.user_input_task_name)
    task_window.main_layout.addSpacing(25)
    task_window.main_layout.addWidget(task_window.task_deadline_label)
    task_window.main_layout.addWidget(task_window.user_input_task_deadline)
    task_window.main_layout.addSpacing(25)
    task_window.main_layout.addWidget(task_window.task_description_label)
    task_window.main_layout.addWidget(task_window.user_input_task_description)
    task_window.main_layout.addSpacing(25)

    task_window.button_layout.setContentsMargins(0, 0, 0, 0)
    task_window.button_layout.setSpacing(0)

    if task_window.is_input:
        task_window.button_layout.addWidget(task_window.send_button)
        task_window.button_layout.addSpacing(5)
        task_window.button_layout.addWidget(task_window.cancel_button)
    else:
        task_window.button_layout.addWidget(task_window.OK_Button)

    task_window.button_widget.setLayout(task_window.button_layout)
    task_window.main_layout.addWidget(task_window.button_widget)

    task_window.setLayout(task_window.main_layout)

def setup_connections(task_window):
    if task_window.is_input:
        task_window.user_input_task_description.textChanged.connect(lambda: limit_max_chars_in_textedit(task_window))
        task_window.send_button.clicked.connect(lambda: get_task_data(task_window))
        task_window.cancel_button.clicked.connect(task_window.reject)
    else:
        task_window.OK_Button.clicked.connect(task_window.close)

def setup_fields(task_window):
    if task_window.is_input:
        task_window.user_input_task_name.setMaxLength(24)
        task_window.user_input_task_name.setPlaceholderText("Enter task name")
        task_window.user_input_task_deadline.setMinimumDateTime(QDateTime.currentDateTime())
        task_window.user_input_task_description.setPlaceholderText("Enter task description")
    else:
        task_window.user_input_task_name.setReadOnly(True)
        task_window.user_input_task_deadline.setReadOnly(True)
        task_window.user_input_task_description.setReadOnly(True)

def setup_object_sizes(task_window):
    task_window.user_input_task_name.setMinimumHeight(50)
    task_window.user_input_task_deadline.setMinimumHeight(50)
    task_window.user_input_task_description.setMinimumHeight(50)

def setup_object_names(task_window):
    task_window.task_name_label.setObjectName("task_name_label")
    task_window.task_deadline_label.setObjectName("task_deadline_label")
    task_window.task_description_label.setObjectName("task_description_label")
    task_window.user_input_task_name.setObjectName("user_input_task_name")
    task_window.user_input_task_deadline.setObjectName("user_input_task_deadline")
    task_window.user_input_task_description.setObjectName("user_input_task_description")
    if task_window.is_input:
        task_window.send_button.setObjectName("send_button")
        task_window.cancel_button.setObjectName("cancel_button")
    else:
        task_window.OK_Button.setObjectName("OK_Button")

def setup_whats_this(task_window):
    if task_window.is_input:
        task_window.setWhatsThis("It's a dialog box that allows you to enter data for your task.")
        task_window.user_input_task_name.setWhatsThis("It's an input field for the task name.")
        task_window.user_input_task_deadline.setWhatsThis("It's a field displaying the task deadline.")
        task_window.user_input_task_description.setWhatsThis("It's a field for entering the task description.")
        task_window.send_button.setWhatsThis("It's a Send button to submit the task data.")
        task_window.cancel_button.setWhatsThis("It's a Cancel button to close the window and discard the task.")
    else:
        task_window.setWhatsThis("It's a message box containing task information.")
        task_window.user_input_task_name.setWhatsThis("It's the task name.")
        task_window.user_input_task_deadline.setWhatsThis("It's the task deadline.")
        task_window.user_input_task_description.setWhatsThis("It's the task description.")
        task_window.OK_Button.setWhatsThis("It's an OK button to close message box.")