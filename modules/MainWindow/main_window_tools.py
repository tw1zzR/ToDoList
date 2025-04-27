
def clear_layout(layout):
    reversed_layout = reversed(range(layout.count()))
    for i in reversed_layout:
        item = layout.itemAt(i).widget()
        layout.removeItem(item)

def connect_checkbox_buttons(main_window):
    def connect_button(button, handler):
        if not hasattr(button, "_clicked_connected"):
            button.clicked.connect(handler)
            button._clicked_connected = True

    for dictionary in main_window.dicts:
        for checkbox, data in dictionary.items():
            task_info_button, edit_task_button, delete_task_button  = data["buttons"]
            reorder_buttons = data["reorder_buttons"]

            connect_button(task_info_button, main_window.on_click_controller.on_click_task_info_checkbox_button)
            connect_button(edit_task_button, main_window.on_click_controller.on_click_edit_task_checkbox_button)
            connect_button(delete_task_button, main_window.on_click_controller.on_click_delete_task_checkbox_button)

            for button in reorder_buttons:
                connect_button(button, main_window.on_click_controller.on_click_reorder_button)