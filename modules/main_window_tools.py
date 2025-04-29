
# def clear_layout(layout):
#     for i in reversed(range(layout.count())):
#         item = layout.itemAt(i)
#         widget = item.widget()
#         if widget is not None:
#             widget.setParent(None)
#         layout.removeItem(item)

def clear_layout(layout):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        child_layout = item.layout()

        if widget is not None:
            widget.setParent(None)  # Просто отвязываем виджет
        if child_layout is not None:
            # child_layout.setParent(None)  # Для layouts можно не вызывать setParent
            pass

# def clear_layout(layout, window):
#     window.setUpdatesEnabled(False)
#
#     while layout.count():
#         item = layout.takeAt(0)
#
#         widget = item.widget()
#         if widget is not None:
#             widget.deleteLater()
#
#         child_layout = item.layout()
#         if child_layout is not None:
#             clear_layout(child_layout, window)  # Рекурсивно очищаем вложенный layout
#
#     window.setUpdatesEnabled(True)



def connect_checkbox_buttons(main_window):
    def connect_button(button, handler):
        if not hasattr(button, "_clicked_connected"):
            button.clicked.connect(handler)
            button._clicked_connected = True

    for task_item in main_window.tasks_data.task_items:
        task_info_button, edit_task_button, delete_task_button  = task_item.checkbox_buttons
        reorder_buttons = task_item.reorder_buttons

        connect_button(task_info_button, main_window.on_click_controller.on_click_task_info_checkbox_button)
        connect_button(edit_task_button, main_window.on_click_controller.on_click_edit_task_checkbox_button)
        connect_button(delete_task_button, main_window.on_click_controller.on_click_delete_task_checkbox_button)

        for button in reorder_buttons:
            connect_button(button, main_window.on_click_controller.on_click_reorder_button)