from windows.TaskDialogBox import TaskDialogBox
from PyQt5.QtWidgets import *

class OnClickController:

    def __init__(self, main_window):
        self.main_window = main_window
        self.visual_mgr = self.main_window.visual_changer
        self.comp_mgr = self.main_window.component_builder
        self.checkbox_mgr = self.main_window.task_checkbox_manager
        self.button_mgr = self.main_window.task_button_manager

    def on_click_task_button(self):
        sender = self.main_window.sender()
        object_name = sender.objectName()

        match object_name:
            case "add_task_button" | "add_task_plus_button":
                task_dialog = TaskDialogBox()
                task_dialog.compare_with_main_win_theme(self.main_window.dark_theme)

                if task_dialog.exec_():
                    task_name, task_deadline, task_description = task_dialog.get_task_data()
                    self.comp_mgr.create_task_checkbox_with_buttons(task_name, task_deadline, task_description)
                    self.checkbox_mgr.show_all_task_checkboxes()

            case "del_tasks_button":
                if not any(self.main_window.dicts):
                    error_messagebox = self.comp_mgr.create_warning_messagebox("Delete all tasks", "Task list is empty.")
                    error_messagebox.exec_()
                    return

                confirmation_dialog = self.comp_mgr.create_and_setup_delete_confirmation_dialog()
                user_reply = confirmation_dialog.exec_()

                if user_reply == QMessageBox.Yes:
                    for dictionary in self.main_window.dicts:
                        for checkbox in list(dictionary.keys()):
                            self.checkbox_mgr.delete_task_checkbox_with_buttons(checkbox, *self.main_window.dicts)
                    self.comp_mgr.current_task_info_window = None

                self.checkbox_mgr.show_all_task_checkboxes()

        if self.main_window.completed_task_opened:
            self.checkbox_mgr.delete_completed_tasks_from_ui()
            self.checkbox_mgr.show_completed_tasks()

    def on_click_change_theme_button(self):
        self.visual_mgr.change_UI_theme()

    def on_click_about_button(self):
        about_app_dialog = self.comp_mgr.create_and_setup_about_app_dialog()
        about_app_dialog.exec_()

    def on_click_task_checkbox(self):
        sender_checkbox = self.main_window.sender()
        is_checked = sender_checkbox.isChecked()

        self.visual_mgr.task_checkbox_set_style_sheet(sender_checkbox, is_checked)

        if is_checked:
            self.checkbox_mgr.move_task_to_another_dict(
                sender_checkbox,
                self.main_window.checkbox_dict,
                self.main_window.completed_checkbox_dict
            )
            self.checkbox_mgr.remove_completed_task_from_ui(sender_checkbox)
        else:
            self.checkbox_mgr.move_task_to_another_dict(
                sender_checkbox,
                self.main_window.completed_checkbox_dict,
                self.main_window.checkbox_dict
            )

        if self.main_window.completed_checkbox_dict:
            self.main_window.completed_task_open_button.show()
        else:
            self.main_window.completed_task_open_button.hide()

        if self.main_window.completed_task_opened:
            self.checkbox_mgr.show_all_task_checkboxes()
            self.checkbox_mgr.delete_completed_tasks_from_ui()
            self.checkbox_mgr.show_completed_tasks()

    def on_click_completed_tasks_button(self):
        self.main_window.completed_task_opened = not self.main_window.completed_task_opened

        self.checkbox_mgr.show_all_task_checkboxes()

        if self.main_window.completed_task_opened:
            self.checkbox_mgr.show_completed_tasks()
        else:
            self.checkbox_mgr.delete_completed_tasks_from_ui()

        self.visual_mgr.change_completed_task_button_icon()

    # Checkbox buttons
    def on_click_task_info_checkbox_button(self):
        sender_checkbox = self.button_mgr.find_checkbox_by_checkbox_button(
            self.main_window.sender()
        )

        self.comp_mgr.create_task_info_messagebox_checkbox_button(sender_checkbox)

    def on_click_edit_task_checkbox_button(self):
        sender_checkbox = self.button_mgr.find_checkbox_by_checkbox_button(
            self.main_window.sender()
        )

        # Get primary checkbox data
        data = next(dictionary[sender_checkbox]
                    for dictionary in self.main_window.dicts
                    if sender_checkbox in dictionary
        )

        self.comp_mgr.create_and_open_edit_task_dialog(
            sender_checkbox,
            data["name"],
            data["deadline"],
            data["description"]
        )

    def on_click_delete_task_checkbox_button(self):
        sender_checkbox = self.button_mgr.find_checkbox_by_checkbox_button(
            self.main_window.sender()
        )

        self.checkbox_mgr.delete_task_checkbox_with_buttons(
            sender_checkbox,
            self.main_window.checkbox_dict,
            self.main_window.completed_checkbox_dict
        )

        self.checkbox_mgr.show_all_task_checkboxes()

        if self.main_window.completed_task_opened:
            self.checkbox_mgr.delete_completed_tasks_from_ui()
            self.checkbox_mgr.show_completed_tasks()

    def on_click_reorder_button(self):
        sender = self.main_window.sender()
        sender_checkbox = self.button_mgr.find_checkbox_by_checkbox_button(sender)

        for data in self.main_window.checkbox_dict.values():
            if data["reorder_buttons"][0] is sender:
                self.checkbox_mgr.move_up_down_checkbox(sender_checkbox, "up")
                break
            elif data["reorder_buttons"][1] is sender:
                self.checkbox_mgr.move_up_down_checkbox(sender_checkbox, "down")
                break