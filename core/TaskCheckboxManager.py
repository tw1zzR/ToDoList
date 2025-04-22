from modules import layout_tools

class TaskCheckboxManager:

    def __init__(self, main_window):
        self.main_window = main_window

    def show_all_task_checkboxes(self):
        layout_tools.clear_layout(self.main_window.tasks_layout)

        self.main_window.component_builder.create_title_and_task_layouts()
        self.main_window.component_builder.create_plus_button_layout()
        self.main_window.component_builder.create_completed_task_button_layout()

        if self.main_window.completed_checkbox_dict:
            self.main_window.completed_task_open_button.show()
        else:
            self.main_window.completed_task_open_button.hide()

        self.main_window.show()


    def show_completed_tasks(self):
        for checkbox, data in self.main_window.completed_checkbox_dict.items():

            if "checkbox_layout" in data:
                continue

            checkbox_layout = self.main_window.component_builder.create_completed_task_layout(checkbox, data)
            data["checkbox_layout"] = checkbox_layout
            self.main_window.tasks_layout.addLayout(checkbox_layout)
            self.main_window.show()


    def move_up_down_checkbox(self, target_checkbox, up_down):
        try:
            i = self.main_window.checkbox_order.index(target_checkbox)
        except ValueError:
            return

        if up_down == "up" and i == 0:
            return
        elif up_down == "down" and i == len(self.main_window.checkbox_order) - 1 :
            return

        if up_down == "up":
            self.main_window.checkbox_order[i-1], self.main_window.checkbox_order[i] = self.main_window.checkbox_order[i], self.main_window.checkbox_order[i-1]
        elif up_down == "down":
            self.main_window.checkbox_order[i+1], self.main_window.checkbox_order[i] = self.main_window.checkbox_order[i], self.main_window.checkbox_order[i+1]

        self.delete_completed_tasks_from_ui()

        self.show_all_task_checkboxes()
        if self.main_window.completed_task_opened:
            self.show_completed_tasks()


    def delete_task_checkbox_with_buttons(self, checkbox_sender, *dicts):
        for dictionary in dicts:
            if checkbox_sender in dictionary:
                checkbox_data = dictionary[checkbox_sender]

                for button in checkbox_data["buttons"] + checkbox_data["reorder_buttons"]:
                    button.setParent(None)
                    button.deleteLater()

                checkbox_sender.setParent(None)
                checkbox_sender.deleteLater()

                self.main_window.checkbox_order.remove(checkbox_sender)
                del dictionary[checkbox_sender]
                break

        self.delete_completed_tasks_button()

    def delete_completed_tasks_from_ui(self):
        for checkbox, data in self.main_window.completed_checkbox_dict.items():
            checkbox_layout = data.get("checkbox_layout")
            if checkbox_layout:
                while checkbox_layout.count():
                    item = checkbox_layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.hide()

                self.main_window.tasks_layout.removeItem(checkbox_layout)
                del data["checkbox_layout"]

    def remove_completed_task_from_ui(self, sender_checkbox):
        for checkbox, data in self.main_window.completed_checkbox_dict.items():
            if checkbox is sender_checkbox:
                checkbox_layout = data.get("checkbox_layout")
                if checkbox_layout:
                    while checkbox_layout.count():
                        item = checkbox_layout.takeAt(0)
                        widget = item.widget()
                        if widget:
                            widget.hide()

                for reorder_button in data["reorder_buttons"]:
                    reorder_button.hide()

                self.main_window.tasks_layout.removeItem(checkbox_layout)
                del data["checkbox_layout"]

    def delete_completed_tasks_button(self):
        self.main_window.tasks_layout.removeWidget(self.main_window.completed_task_open_button)
        self.main_window.completed_task_open_button.setParent(None)
        self.main_window.update()

    def move_task_to_another_dict(self, completed_task_checkbox, from_dict, to_dict):
        if completed_task_checkbox in self.main_window.checkbox_order:
            checkbox_index  = self.main_window.checkbox_order.index(completed_task_checkbox)
            checkbox_key = self.main_window.checkbox_order[checkbox_index]

            completed_task_checkbox_data = from_dict.pop(checkbox_key)
            to_dict[completed_task_checkbox] = completed_task_checkbox_data