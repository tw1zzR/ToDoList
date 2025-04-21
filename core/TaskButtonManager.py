
class TaskButtonManager:

    def __init__(self, main_window):
        self.main_window = main_window

    def find_checkbox_by_checkbox_button(self, clicked_button):
        for dictionary in self.main_window.dicts:
            for checkbox, data in dictionary.items():
                if clicked_button in data["buttons"] or clicked_button in data["reorder_buttons"]:
                    return checkbox

    def connect_checkbox_buttons(self):
        for dictionary in self.main_window.dicts:
            for checkbox, data in dictionary.items():
                task_info_button  = data["buttons"][0]
                edit_task_button  = data["buttons"][1]
                delete_task_button = data["buttons"][2]

                if not hasattr(task_info_button, "_clicked_connected"):
                    task_info_button.clicked.connect(self.main_window.on_click_task_info_checkbox_button)
                    task_info_button._clicked_connected = True
                if not hasattr(edit_task_button, "_clicked_connected"):
                    edit_task_button.clicked.connect(self.main_window.on_click_edit_task_checkbox_button)
                    edit_task_button._clicked_connected = True
                if not hasattr(delete_task_button, "_clicked_connected"):
                    delete_task_button.clicked.connect(self.main_window.on_click_delete_task_checkbox_button)
                    delete_task_button._clicked_connected = True
                for reorder_button in data["reorder_buttons"]:
                    if not hasattr(reorder_button, "_clicked_connected"):
                        reorder_button.clicked.connect(self.main_window.on_click_reorder_button)
                        reorder_button._clicked_connected = True