
class TaskButtonManager:

    def __init__(self, main_window):
        self.main_window = main_window
        self.on_click_mgr = self.main_window.on_click_controller

    def find_checkbox_by_checkbox_button(self, clicked_button):
        for dictionary in self.main_window.dicts:
            for checkbox, data in dictionary.items():
                if clicked_button in data["buttons"] or clicked_button in data["reorder_buttons"]:
                    return checkbox

    def connect_checkbox_buttons(self):
        for dictionary in self.main_window.dicts:
            for checkbox, data in dictionary.items():
                task_info_button, edit_task_button, delete_task_button  = data["buttons"]
                reorder_buttons = data["reorder_buttons"]

                self.connect_button(task_info_button, self.on_click_mgr.on_click_task_info_checkbox_button)
                self.connect_button(edit_task_button, self.on_click_mgr.on_click_edit_task_checkbox_button)
                self.connect_button(delete_task_button, self.on_click_mgr.on_click_delete_task_checkbox_button)

                for button in reorder_buttons:
                    self.connect_button(button, self.on_click_mgr.on_click_reorder_button)

    def connect_button(self, button, handler):
        if not hasattr(button, "_clicked_connected"):
            button.clicked.connect(handler)
            button._clicked_connected = True