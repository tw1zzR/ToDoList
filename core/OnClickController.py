from windows.TaskDialogBox import TaskDialogBox
from PyQt5.QtWidgets import *


class OnClickController:

    def __init__(self, main_window):
        self.main_window = main_window

    def on_click_task_button(self):
        sender = self.main_window.sender()

        match sender.objectName():
            case "add_task_button" | "add_task_plus_button":
                add_task_dialog_box = TaskDialogBox()
                add_task_dialog_box.compare_with_main_win_theme(self.main_window.dark_theme)

                if add_task_dialog_box.exec_():
                    user_task_name, user_task_deadline, user_task_description = add_task_dialog_box.get_task_data()
                    self.main_window.component_builder.create_task_checkbox_with_buttons(user_task_name,
                                                                                         user_task_deadline,
                                                                                         user_task_description)
                    self.main_window.task_checkbox_manager.show_all_task_checkboxes()

            case "del_tasks_button":
                if any(self.main_window.dicts):
                    delete_confirmation_dialog = self.main_window.component_builder.create_and_setup_delete_confirmation_dialog()

                    user_reply = delete_confirmation_dialog.exec_()
                    if user_reply == QMessageBox.Yes:
                        for dictionary in self.main_window.dicts:
                            list_of_checkboxes = list(dictionary.keys())
                            for checkbox in list_of_checkboxes:
                                self.main_window.task_checkbox_manager.delete_task_checkbox_with_buttons(checkbox, *self.main_window.dicts)
                        self.main_window.component_builder.current_task_info_window = None

                    self.main_window.task_checkbox_manager.show_all_task_checkboxes()
                else:
                    delete_tasks_error = self.main_window.component_builder.create_warning_messagebox("Delete all tasks",
                                                                                          "Task list is empty.")
                    delete_tasks_error.exec_()

        if self.main_window.completed_task_opened:
            self.main_window.task_checkbox_manager.delete_completed_tasks_from_ui()
            self.main_window.task_checkbox_manager.show_completed_tasks()

    def on_click_change_theme_button(self):
        self.main_window.visual_changer.change_UI_theme()

    def on_click_about_button(self):
        about_app_dialog = self.main_window.component_builder.create_and_setup_about_app_dialog()
        about_app_dialog.exec_()

        # Set checkbox checked method
    def on_click_task_checkbox(self):
        sender_checkbox = self.main_window.sender()

        if self.main_window.completed_checkbox_dict:
            self.main_window.completed_task_open_button.show()
        else:
            self.main_window.completed_task_open_button.hide()

        match sender_checkbox.isChecked():
            case True:
                self.main_window.visual_changer.task_checkbox_set_style_sheet(sender_checkbox, True)

                self.main_window.task_checkbox_manager.move_task_to_another_dict(
                    sender_checkbox,
                    self.main_window.checkbox_dict,
                    self.main_window.completed_checkbox_dict
                )
                self.main_window.task_checkbox_manager.remove_completed_task_from_ui(sender_checkbox)

                self.main_window.completed_task_open_button.show()

            case False:
                self.main_window.visual_changer.task_checkbox_set_style_sheet(sender_checkbox, False)

                self.main_window.task_checkbox_manager.move_task_to_another_dict(
                    sender_checkbox,
                    self.main_window.completed_checkbox_dict,
                    self.main_window.checkbox_dict
                )

        if self.main_window.completed_task_opened:
            self.main_window.task_checkbox_manager.show_all_task_checkboxes()
            self.main_window.task_checkbox_manager.delete_completed_tasks_from_ui()
            self.main_window.task_checkbox_manager.show_completed_tasks()


    def on_click_completed_tasks_button(self):
        self.main_window.task_checkbox_manager.show_all_task_checkboxes()

        if self.main_window.completed_task_opened:
            self.main_window.completed_task_opened = False
            self.main_window.task_checkbox_manager.delete_completed_tasks_from_ui()
        else:
            self.main_window.completed_task_opened = True
            self.main_window.task_checkbox_manager.show_completed_tasks()

        self.main_window.visual_changer.change_completed_task_button_icon()

    # Checkbox buttons
    def on_click_task_info_checkbox_button(self):
        sender = self.main_window.sender()
        sender_checkbox = self.main_window.task_button_manager.find_checkbox_by_checkbox_button(sender)

        self.main_window.component_builder.create_task_info_messagebox_checkbox_button(sender_checkbox)

    def on_click_edit_task_checkbox_button(self):
        sender = self.main_window.sender()
        sender_checkbox = self.main_window.task_button_manager.find_checkbox_by_checkbox_button(sender)

        # Get primary checkbox data
        for dictionary in self.main_window.dicts:
            if sender_checkbox in dictionary:
                task_data = dictionary[sender_checkbox]
                task_name = task_data["name"]
                task_deadline = task_data["deadline"]
                task_description = task_data["description"]
                break

        self.main_window.component_builder.create_and_open_edit_task_dialog(
            sender_checkbox,
            task_name,
            task_deadline,
            task_description
        )

    def on_click_delete_task_checkbox_button(self):
        sender = self.main_window.sender()
        sender_checkbox = self.main_window.task_button_manager.find_checkbox_by_checkbox_button(sender)

        self.main_window.task_checkbox_manager.delete_task_checkbox_with_buttons(
            sender_checkbox,
            self.main_window.checkbox_dict,
            self.main_window.completed_checkbox_dict
        )

        self.main_window.task_checkbox_manager.show_all_task_checkboxes()

        if self.main_window.completed_task_opened:
            self.main_window.task_checkbox_manager.delete_completed_tasks_from_ui()
            self.main_window.task_checkbox_manager.show_completed_tasks()

    def on_click_reorder_button(self):
        sender = self.main_window.sender()
        sender_checkbox = self.main_window.task_button_manager.find_checkbox_by_checkbox_button(sender)

        for data in self.main_window.checkbox_dict.values():
            if data["reorder_buttons"][0] is sender:
                self.main_window.task_checkbox_manager.move_up_down_checkbox(sender_checkbox, "up")
            elif data["reorder_buttons"][1] is sender:
                self.main_window.task_checkbox_manager.move_up_down_checkbox(sender_checkbox, "down")
            else:
                continue
            break