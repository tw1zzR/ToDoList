from windows.TaskInfoMessageBox import CustomTaskInfoMessageBox
from windows.TaskDialogBox import TaskDialogBox
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ComponentBuilderUI:

    def __init__(self, main_window):
        self.main_window = main_window
        self.visual_mgr = self.main_window.visual_changer

        self.current_task_info_window = None


    def create_task_checkbox_with_buttons(self, user_task_name, user_task_deadline, user_task_description):
        task_checkbox = QCheckBox(user_task_name, self.main_window)
        task_checkbox.stateChanged.connect(self.main_window.on_click_controller.on_click_task_checkbox)
        task_checkbox.setFixedHeight(50)

        reorder_buttons = self.create_reorder_buttons()
        checkbox_buttons = self.create_checkbox_buttons()

        self.main_window.checkbox_order.append(task_checkbox)
        self.main_window.checkbox_dict[task_checkbox] = {
            "buttons": checkbox_buttons,
            "reorder_buttons": reorder_buttons,
            "name": user_task_name,
            "deadline": user_task_deadline,
            "description": user_task_description
        }

        self.visual_mgr.change_checkboxes_button_icons_theme()
        self.main_window.task_button_manager.connect_checkbox_buttons()


    def create_reorder_buttons(self):
        moveup_button = QPushButton(self.main_window)
        movedown_button = QPushButton(self.main_window)
        for button in [moveup_button, movedown_button]:
            button.setFixedSize(50, 25)
            button.setStyleSheet("background-color: transparent;")
        return [moveup_button, movedown_button]


    def create_checkbox_buttons(self):
        task_info_button = QPushButton(self.main_window)
        edit_task_button = QPushButton(self.main_window)
        delete_task_button = QPushButton(self.main_window)

        for button in [task_info_button, edit_task_button, delete_task_button]:
            button.setFixedSize(50, 50)
            button.setIconSize(QSize(30, 30))
            self.visual_mgr.set_default_widget_style(button)

        task_info_button.setToolTip("View task details")
        edit_task_button.setToolTip("Edit task")
        delete_task_button.setToolTip("Delete task")

        return [task_info_button, edit_task_button, delete_task_button]


    def create_task_info_messagebox_checkbox_button(self, checkbox_sender):
        task_info = None

        for dictionary in self.main_window.dicts:
            if checkbox_sender in dictionary:
                task_info = dictionary[checkbox_sender]
                break

        if task_info:
            task_name = task_info["name"]
            task_deadline = task_info["deadline"]
            task_description = task_info["description"]

            if self.current_task_info_window:
                self.current_task_info_window.close()
                self.current_task_info_window.set_task_info_msgbox_new_data(task_name, task_deadline, task_description)
            else:
                self.current_task_info_window = CustomTaskInfoMessageBox(task_name, task_deadline, task_description)

            self.current_task_info_window.compare_with_main_win_theme(self.main_window.dark_theme)
            self.current_task_info_window.show()


    def create_and_open_edit_task_dialog(self, sender_checkbox, primary_task_name, primary_task_deadline, primary_task_description):
        edit_task_dialog = TaskDialogBox()

        edit_task_dialog.compare_with_main_win_theme(self.main_window.dark_theme)

        date_format = "dd.MM.yyyy HH:mm"

        # Set primary checkbox data
        edit_task_dialog.user_input_task_name.setText(primary_task_name)
        edit_task_dialog.user_input_task_deadline.setDateTime(
            QDateTime.fromString(primary_task_deadline, date_format)
        )
        edit_task_dialog.user_input_task_description.setText(primary_task_description)

        if edit_task_dialog.exec_():
            # Change to edited checkbox data
            edited_task_name, edited_task_deadline, edited_task_description = edit_task_dialog.get_task_data()

            for dictionary in self.main_window.dicts:
                if sender_checkbox in dictionary:
                    dictionary[sender_checkbox].update({
                        "name": edited_task_name,
                        "deadline": edited_task_deadline,
                        "description": edited_task_description
                    })
                    break

            sender_checkbox.setText(edited_task_name)


    def create_and_setup_delete_confirmation_dialog(self):
        delete_confirmation_dialog = QMessageBox()

        delete_confirmation_dialog.setWindowTitle("Delete All Tasks")
        delete_confirmation_dialog.setWindowIcon(QIcon("assets/TaskDialogBox/addtask_dialogbox_icon.png"))
        delete_confirmation_dialog.setText("Are you sure you want to delete all tasks?")
        delete_confirmation_dialog.setIcon(QMessageBox.Warning)
        delete_confirmation_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        self.visual_mgr.set_default_widget_style(delete_confirmation_dialog)

        return delete_confirmation_dialog


    def create_and_setup_about_app_dialog(self):
        about_app_dialog = QMessageBox()

        about_app_dialog.setWindowTitle("About App")
        about_app_dialog.setWindowIcon(QIcon("assets/AboutAppMessageBox/information_icon.png"))
        about_app_dialog.setTextFormat(Qt.RichText)
        about_app_dialog.setText("My GitHub: <a href=\"https://github.com/tw1zzR\">tw1zzR</a>")
        about_app_dialog.setIcon(QMessageBox.Information)

        self.visual_mgr.set_default_widget_style(about_app_dialog)

        return about_app_dialog

    def create_warning_messagebox(self, title, message):
        warning_msgbox = QMessageBox()

        warning_msgbox.setWindowTitle(title)
        warning_msgbox.setWindowIcon(QIcon("assets/warning_icon_1.png"))
        warning_msgbox.setTextFormat(Qt.RichText)
        warning_msgbox.setText(message)
        warning_msgbox.setIcon(QMessageBox.Warning)

        self.visual_mgr.set_default_widget_style(warning_msgbox)

        return warning_msgbox

    # Show all task checkboxes methods
    def create_title_and_task_layouts(self):
        title_tasks_layout = QHBoxLayout()
        title_tasks_layout.addStretch()
        title_tasks_layout.addWidget(self.main_window.title_tasks_label, alignment=Qt.AlignCenter)
        title_tasks_layout.addStretch()
        self.main_window.tasks_layout.addLayout(title_tasks_layout)

        for checkbox in self.main_window.checkbox_order:
            if checkbox in self.main_window.checkbox_dict:
                data = self.main_window.checkbox_dict[checkbox]
                checkbox_layout = self.create_task_checkbox_layout(checkbox, data)
                self.main_window.tasks_layout.addLayout(checkbox_layout)

    def create_task_checkbox_layout(self, checkbox, data):
        checkbox_layout = QHBoxLayout()
        checkbox_layout.setContentsMargins(0, 0, 0, 0)
        checkbox_layout.setSpacing(0)

        # Reorder buttons
        reorder_layout = QVBoxLayout()
        for button in data["reorder_buttons"]:
            button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            button.show()
            reorder_layout.addWidget(button)
        checkbox_layout.addLayout(reorder_layout)

        # Checkbox
        checkbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        checkbox_layout.addWidget(checkbox)

        # Action buttons
        for button in data["buttons"]:
            button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            button.show()
            checkbox_layout.addWidget(button)

        checkbox_layout.addSpacing(50)
        data["checkbox_layout"] = checkbox_layout
        return checkbox_layout

    def create_plus_button_layout(self):
        plus_button_layout = QHBoxLayout()
        plus_button_layout.addSpacing(50)
        plus_button_layout.addWidget(self.main_window.add_task_plus_button, alignment=Qt.AlignLeft)
        plus_button_layout.addStretch()

        self.main_window.add_task_plus_button.setFixedSize(50, 50)
        self.main_window.tasks_layout.addLayout(plus_button_layout)

    def create_completed_task_button_layout(self):
        completed_tasks_button_layout = QHBoxLayout()
        completed_tasks_button_layout.addSpacing(50)
        completed_tasks_button_layout.addWidget(self.main_window.completed_task_open_button, alignment=Qt.AlignCenter)
        completed_tasks_button_layout.addSpacing(50)

        self.main_window.completed_task_open_button.hide()
        self.main_window.tasks_layout.addLayout(completed_tasks_button_layout)

    # Show completed tasks methods
    def create_completed_task_layout(self, checkbox, data):
        checkbox_layout = QHBoxLayout()
        checkbox_layout.setContentsMargins(0, 0, 0, 0)
        checkbox_layout.setSpacing(0)
        checkbox_layout.addSpacing(50)

        checkbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        checkbox.show()
        checkbox_layout.addWidget(checkbox)

        for reorder_button in data["reorder_buttons"]:
            reorder_button.hide()
        for button in data["buttons"]:
            button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            button.show()
            checkbox_layout.addWidget(button)

        checkbox_layout.addSpacing(50)
        return checkbox_layout