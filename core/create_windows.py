



def create_task_info_dialog(self, checkbox, task_info, *dicts):
    task_info = None

    for dictionary in self.main_window.dicts:
        if checkbox_sender in dictionary:
            task_info = dictionary[checkbox_sender]
            break

    if task_info:




    if self.current_task_window:
        self.current_task_window.close()

        task_display_tools.set_task_info_msgbox_new_data(self.current_task_window, task_name, task_deadline,
                                                         task_description)
    else:
        self.current_task_window = TaskInfoDialog(task_name, task_deadline, task_description)

    global_tools.compare_with_main_window_theme(self.current_task_window, self.main_window.dark_theme)
    self.current_task_window.show()


def create_and_open_edit_task_input_dialog(self, sender_checkbox, primary_task_name, primary_task_deadline,
                                           primary_task_description):
    if (self.current_task_window is not None
            and self.current_task_window.isVisible()
            and isinstance(self.current_task_window, TaskInfoDialog)
            and task_info["name"] == self.current_task_window.user_input_task_description):
        self.current_task_window.raise_()
        self.current_task_window.activateWindow()
    else:
        edit_task_input_dialog = TaskInputDialog("Edit Task")

        global_tools.compare_with_main_window_theme(edit_task_input_dialog, self.main_window.dark_theme)

        date_format = "dd.MM.yyyy HH:mm"

        # Set primary checkbox data
        edit_task_input_dialog.user_input_task_name.setText(primary_task_name)
        edit_task_input_dialog.user_input_task_deadline.setDateTime(
            QDateTime.fromString(primary_task_deadline, date_format)
        )
        edit_task_input_dialog.user_input_task_description.setText(primary_task_description)

        if edit_task_input_dialog.exec_():
            # Change to edited checkbox data
            edited_task_name, edited_task_deadline, edited_task_description = get_task_data(edit_task_input_dialog)

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
    delete_confirmation_dialog.setWindowIcon(QIcon("assets/TaskInputDialog/addtask_dialogbox_icon.png"))
    delete_confirmation_dialog.setText("Are you sure you want to delete all tasks?")
    delete_confirmation_dialog.setIcon(QMessageBox.Warning)
    delete_confirmation_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

    global_tools.set_default_widget_style(self.main_window, delete_confirmation_dialog)

    return delete_confirmation_dialog


def create_and_setup_about_app_dialog(self):
    about_app_dialog = QMessageBox()

    about_app_dialog.setWindowTitle("About App")
    about_app_dialog.setWindowIcon(QIcon("assets/AboutAppMessageBox/information_icon.png"))
    about_app_dialog.setTextFormat(Qt.RichText)
    about_app_dialog.setText("My GitHub: <a href=\"https://github.com/tw1zzR\">tw1zzR</a>")
    about_app_dialog.setIcon(QMessageBox.Information)

    global_tools.set_default_widget_style(self.main_window, about_app_dialog)

    return about_app_dialog