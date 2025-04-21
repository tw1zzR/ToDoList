from windows.TaskInfoMessageBox import CustomTaskInfoMessageBox
from windows.TaskDialogBox import TaskDialogBox
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ComponentBuilderUI:

    def __init__(self, main_window):
        self.main_window = main_window
        self.current_task_info_window = None


    def create_task_checkbox_with_buttons(self, user_task_name, user_task_deadline, user_task_description):
        task_checkbox = QCheckBox(user_task_name, self.main_window)
        task_checkbox.stateChanged.connect(self.main_window.on_click_task_checkbox)
        task_checkbox.setFixedHeight(50)

        checkbox_moveup_button = QPushButton(self.main_window)
        checkbox_movedown_button = QPushButton(self.main_window)

        checkbox_moveup_button.setFixedSize(50,25)
        checkbox_movedown_button.setFixedSize(50,25)

        checkbox_reorder_buttons = [checkbox_moveup_button, checkbox_movedown_button]

        task_info_button = QPushButton(self.main_window)
        edit_task_button = QPushButton(self.main_window)
        delete_task_button = QPushButton(self.main_window)

        task_info_button.setToolTip("View task details")
        edit_task_button.setToolTip("Edit task")
        delete_task_button.setToolTip("Delete task")

        checkbox_buttons = [task_info_button, edit_task_button, delete_task_button]

        for button in checkbox_buttons:
            button.setFixedSize(50, 50)
            button.setIconSize(QSize(30, 30))
            self.main_window.visual_changer.set_default_widget_style(button)

        for reorder_button in checkbox_reorder_buttons:
            reorder_button.setStyleSheet("background-color: transparent;")

        self.main_window.checkbox_dict[task_checkbox] = {
            "buttons": checkbox_buttons,
            "reorder_buttons": checkbox_reorder_buttons,
            "name": user_task_name,
            "deadline": user_task_deadline,
            "description": user_task_description
        }

        self.main_window.visual_changer.change_checkboxes_button_icons_theme()
        self.main_window.connect_checkbox_buttons()


    def create_task_info_messagebox_checkbox_button(self, checkbox_sender):
        for dictionary in self.main_window.dicts:
            if checkbox_sender in dictionary:
                task_name = dictionary[checkbox_sender]["name"]
                task_deadline = dictionary[checkbox_sender]["deadline"]
                task_description = dictionary[checkbox_sender]["description"]

        if self.current_task_info_window:
            self.current_task_info_window.close()
            self.current_task_info_window.set_task_info_msgbox_new_data(task_name, task_deadline, task_description)
        else:
            self.current_task_info_window = CustomTaskInfoMessageBox(task_name, task_deadline, task_description)

        self.current_task_info_window.compare_with_main_win_theme(self.main_window.dark_theme)

        self.current_task_info_window.show()


    def create_and_open_edit_task_dialog(self, sender_checkbox, primary_task_name, primary_task_deadline, primary_task_description):
        edit_task_dialogbox = TaskDialogBox()

        edit_task_dialogbox.compare_with_main_win_theme(self.main_window.dark_theme)

        date_format = "dd.MM.yyyy HH:mm"
        primary_user_task_deadline = QDateTime.fromString(primary_task_deadline, date_format)

        # Set primary checkbox data
        edit_task_dialogbox.user_input_task_name.setText(primary_task_name)
        edit_task_dialogbox.user_input_task_deadline.setDateTime(primary_user_task_deadline)
        edit_task_dialogbox.user_input_task_description.setText(primary_task_description)

        if edit_task_dialogbox.exec_():
            # Change to edited checkbox data
            edited_task_name, edited_task_deadline, edited_task_description = edit_task_dialogbox.get_task_data()

            for dictionary in self.main_window.dicts:
                if sender_checkbox in dictionary:
                    dictionary[sender_checkbox]["name"] = edited_task_name
                    dictionary[sender_checkbox]["deadline"] = edited_task_deadline
                    dictionary[sender_checkbox]["description"] = edited_task_description
                    break

            sender_checkbox.setText(edited_task_name)


    def create_and_setup_delete_confirmation_dialog(self):
        delete_confirmation_dialog = QMessageBox()

        delete_confirmation_dialog.setWindowTitle("Delete All Tasks")
        delete_confirmation_dialog.setWindowIcon(QIcon("assets/TaskDialogBox/addtask_dialogbox_icon.png"))
        delete_confirmation_dialog.setText("Are you sure you want to delete all tasks?")

        delete_confirmation_dialog.setIcon(QMessageBox.Warning)
        delete_confirmation_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        self.main_window.visual_changer.set_default_widget_style(delete_confirmation_dialog)

        return delete_confirmation_dialog


    def create_and_setup_about_app_dialog(self):
        about_app_dialog = QMessageBox()

        about_app_dialog.setWindowTitle("About App")
        about_app_dialog.setWindowIcon(QIcon("assets/AboutAppMessageBox/information_icon.png"))
        about_app_dialog.setTextFormat(Qt.RichText)
        about_app_dialog.setText("My GitHub: <a href=\"https://github.com/tw1zzR\">tw1zzR</a>")
        about_app_dialog.setIcon(QMessageBox.Information)

        self.main_window.visual_changer.set_default_widget_style(about_app_dialog)

        return about_app_dialog

    def create_warning_messagebox(self, title, message):
        warning_msgbox = QMessageBox()

        warning_msgbox.setWindowTitle(title)
        warning_msgbox.setWindowIcon(QIcon("assets/warning_icon_1.png"))
        warning_msgbox.setTextFormat(Qt.RichText)
        warning_msgbox.setText(message)
        warning_msgbox.setIcon(QMessageBox.Warning)

        warning_msgbox.setStyleSheet("""
            QMessageBox {
                font-family: Helvetica;
                color: rgb(0,0,0);
                font-size: 16px;
            }
            QPushButton {
                font-family: Helvetica;
                font-size: 14px;
            }
            """)

        return warning_msgbox