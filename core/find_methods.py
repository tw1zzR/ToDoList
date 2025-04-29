
def find_checkbox_by_checkbox_button(clicked_button, *dicts):
    for dictionary in dicts:
        for checkbox, data in dictionary.items():
            if clicked_button in data["buttons"] or clicked_button in data["reorder_buttons"]:
                return checkbox

def find_task_info_by_checkbox(checkbox, *dicts, returns=None):
    task_info = None

    for dictionary in dicts:
        if checkbox in dictionary:
            task_info = dictionary[checkbox]
            break

    if task_info is not None and returns:
        return {key: task_info[key] for key in returns if key in task_info}

    return task_info

