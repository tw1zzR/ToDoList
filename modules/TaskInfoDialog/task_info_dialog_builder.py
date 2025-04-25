from PyQt5.QtCore import *
from PyQt5.QtGui import *

def setup_UI(task_info_dialog):
    setup_task_info_dialog(task_info_dialog)
    setup_main_layout(task_info_dialog)
    setup_alignment(task_info_dialog)
    setup_task_info_elements(task_info_dialog)
    setup_object_names(task_info_dialog)
    setup_what_this_button(task_info_dialog)

def setup_task_info_dialog(task_info_dialog):
    task_info_dialog.setWindowTitle("Task Info")
    task_info_dialog.setWindowIcon(QIcon("assets/TaskInfoDialog/gray_task_info_button_V2_icon.png"))
    task_info_dialog.resize(520, 600)

def setup_main_layout(task_info_dialog):
    task_info_dialog.main_layout.setContentsMargins(50, 50, 50, 50)
    task_info_dialog.main_layout.setSpacing(0)

    task_info_dialog.main_layout.addWidget(task_info_dialog.task_name_label)
    task_info_dialog.main_layout.addWidget(task_info_dialog.user_input_task_name)
    task_info_dialog.main_layout.addSpacing(25)
    task_info_dialog.main_layout.addWidget(task_info_dialog.task_deadline_label)
    task_info_dialog.main_layout.addWidget(task_info_dialog.user_input_task_deadline)
    task_info_dialog.main_layout.addSpacing(25)
    task_info_dialog.main_layout.addWidget(task_info_dialog.task_description_label)
    task_info_dialog.main_layout.addWidget(task_info_dialog.user_input_task_description)
    task_info_dialog.main_layout.addSpacing(25)

    task_info_dialog.main_layout.addWidget(task_info_dialog.OK_Button)

    task_info_dialog.setLayout(task_info_dialog.main_layout)

def setup_alignment(task_info_dialog):
    task_info_dialog.user_input_task_name.setAlignment(Qt.AlignCenter)
    task_info_dialog.user_input_task_deadline.setAlignment(Qt.AlignCenter)
    task_info_dialog.user_input_task_description.setAlignment(Qt.AlignCenter)

def setup_task_info_elements(task_info_dialog):
    task_info_dialog.OK_Button.clicked.connect(task_info_dialog.close)
    task_info_dialog.user_input_task_description.setReadOnly(True)

    task_info_dialog.user_input_task_name.setMinimumHeight(50)
    task_info_dialog.user_input_task_deadline.setMinimumHeight(50)
    task_info_dialog.user_input_task_description.setMinimumHeight(50)
    task_info_dialog.OK_Button.setMinimumHeight(50)

def setup_object_names(task_info_dialog):
    task_info_dialog.task_name_label.setObjectName("task_name_label")
    task_info_dialog.task_deadline_label.setObjectName("task_deadline_label")
    task_info_dialog.task_description_label.setObjectName("task_description_label")
    task_info_dialog.user_input_task_name.setObjectName("user_input_task_name")
    task_info_dialog.user_input_task_deadline.setObjectName("user_input_task_deadline")
    task_info_dialog.user_input_task_description.setObjectName("user_input_task_description")
    task_info_dialog.OK_Button.setObjectName("OK_Button")

def setup_what_this_button(task_dialog):
    task_dialog.setWhatsThis("It's a message box containing task information.")
    task_dialog.user_input_task_name.setWhatsThis("It's the task name.")
    task_dialog.user_input_task_deadline.setWhatsThis("It's the task deadline.")
    task_dialog.user_input_task_description.setWhatsThis("It's the task description.")
    task_dialog.OK_Button.setWhatsThis("It's an OK button to close message box.")