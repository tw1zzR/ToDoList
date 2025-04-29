from Task.task_methods import create_task_item, find_task_item_by_element, transfer_task
from core.manage_windows_data import update_window_fields, edit_task_data
from core.find_methods import find_checkbox_by_checkbox_button
from core import find_methods
from Task.task import Task
from modules.MainWindow import main_window_tools
from modules.MainWindow.main_window_tools import clear_layout
from modules.TaskDialog.dialog_tools import get_task_data
from modules import global_tools
from PyQt5.QtWidgets import *


class OnClickController:

    def __init__(self, main_window):
        self.main_window = main_window
        self.visual_mgr = self.main_window.visual_changer
        self.comp_mgr = self.main_window.checkbox_elems_builder
        self.checkbox_mgr = self.main_window.task_checkbox_manager

        self.previous_checkbox_sender = None

    def on_click_change_theme_button(self):
        self.visual_mgr.change_UI_theme()
        global_tools.set_app_theme(self.main_window.dark_theme)

    def on_click_about_button(self):
        about_messagebox = global_tools.create_messagebox("About App",
                  "My GitHub: <a href=\"https://github.com/tw1zzR\">tw1zzR</a>",
                          QMessageBox.Information,
                  "assets/AboutAppMessageBox/information_icon.png")
        about_messagebox.exec_()







    def on_click_task_button(self):
        sender = self.main_window.sender()
        object_name = sender.objectName()

        match object_name:
            case "add_task_button" | "add_task_plus_button":
                update_window_fields(self.main_window.task_input_window, is_add=True)

                if self.main_window.task_input_window.exec_():
                    task_name, task_deadline, task_description = get_task_data(self.main_window.task_input_window)

                    checkbox, checkbox_buttons, reorder_buttons = self.comp_mgr.create_checkbox_with_buttons(task_name)

                    task_item = create_task_item(task_name, task_deadline, task_description, checkbox, checkbox_buttons, reorder_buttons)

                    self.main_window.tasks_data.insert_task(task_item)

                    self.visual_mgr.change_checkboxes_button_icons_theme()
                    main_window_tools.connect_checkbox_buttons(self.main_window)

                    self.checkbox_mgr.refresh_ui_task_checkboxes()

            case "del_tasks_button":
                warning_messagebox = global_tools.create_messagebox("Delete All Tasks",
                                                                    "",
                                                                    QMessageBox.Warning,
                                                                    "assets/warning_icon_1.png")

                if not any(self.main_window.tasks_data.task_items):
                    warning_messagebox.setText("Task list is empty.")
                    warning_messagebox.exec_()
                    return

                warning_messagebox.setText("Are you sure you want to delete all tasks?")
                warning_messagebox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

                user_reply = warning_messagebox.exec_()

                if user_reply == QMessageBox.Yes:
                    for task_item in self.main_window.tasks_data.task_items[:]:
                        self.checkbox_mgr.delete_task_item(task_item, *self.main_window.tasks_data.task_lists)

        #         self.checkbox_mgr.show_all_task_checkboxes()
        #
        # if self.main_window.completed_task_opened:
        #     self.checkbox_mgr.delete_completed_tasks_from_ui()
        #     self.checkbox_mgr.show_completed_tasks()





    def on_click_task_checkbox(self):
        sender_checkbox = self.main_window.sender()
        is_checked = sender_checkbox.isChecked()

        self.visual_mgr.task_checkbox_set_style_sheet(sender_checkbox, is_checked)
        task_item = find_task_item_by_element(sender_checkbox, self.main_window.tasks_data.task_items)

        transfer_task(task_item, is_checked, self.main_window)

        if self.main_window.tasks_data.completed_task_items:
            self.main_window.completed_task_open_button.show()
        else:
            self.main_window.completed_task_open_button.hide()

        self.checkbox_mgr.refresh_ui_task_checkboxes()

        if self.main_window.completed_task_opened:
            self.checkbox_mgr.show_completed_tasks()

        # if self.main_window.completed_task_opened:
        #     self.checkbox_mgr.show_all_task_checkboxes()
        #     self.checkbox_mgr.delete_completed_tasks_from_ui()
        #     self.checkbox_mgr.show_completed_tasks()

    def on_click_completed_tasks_button(self):
        self.main_window.completed_task_opened = not self.main_window.completed_task_opened

        self.checkbox_mgr.refresh_ui_task_checkboxes()

        if self.main_window.completed_task_opened:
            self.checkbox_mgr.show_completed_tasks()
        else:
            self.checkbox_mgr.delete_completed_tasks_from_ui()

        self.visual_mgr.change_completed_task_button_icon()




    # Checkbox buttons
    def on_click_task_info_checkbox_button(self):
        task_item = find_task_item_by_element(self.main_window.sender(), self.main_window.tasks_data.task_items)
        task_info = task_item.task

        update_window_fields(self.main_window.task_info_window, task_info)
        global_tools.open_task_dialog(self.main_window.task_info_window)

    def on_click_edit_task_checkbox_button(self):
        task_item = find_task_item_by_element(self.main_window.sender(), self.main_window.tasks_data.task_items)
        task_info = task_item.task

        old_task_name = task_info.name

        update_window_fields(self.main_window.task_input_window, task_info)

        if self.main_window.task_input_window.exec_():
            edit_task_data(self.main_window.task_input_window, task_item, self.main_window.tasks_data.task_items)

            if self.main_window.task_info_window.user_input_task_name.text() == old_task_name:
                update_window_fields(self.main_window.task_info_window, task_item.task)

    def on_click_delete_task_checkbox_button(self):
        task_item = find_task_item_by_element(self.main_window.sender(), self.main_window.tasks_data.task_items)

        self.checkbox_mgr.delete_task_item(task_item, *self.main_window.tasks_data.task_lists)
        self.checkbox_mgr.refresh_ui_task_checkboxes()


    def on_click_reorder_button(self):
        sender = self.main_window.sender()
        task_item = find_task_item_by_element(sender, self.main_window.tasks_data.task_items)

        for task_item in self.main_window.tasks_data.task_items:
            if task_item.reorder_buttons[0] is sender:
                self.checkbox_mgr.move_up_down_checkbox(task_item, "up")
                break
            elif task_item.reorder_buttons[1] is sender:
                self.checkbox_mgr.move_up_down_checkbox(task_item, "down")
                break