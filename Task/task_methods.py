from Task.task import Task
from Task.task_item import TaskItem


def create_task_item(name, deadline, description, checkbox, checkbox_buttons, reorder_buttons):
    task = Task(name, deadline, description)
    task_item = TaskItem(task, checkbox, checkbox_buttons, reorder_buttons)
    return task_item

def find_task_item_by_element(element, task_items):
    for task_item in task_items:
        if (
            element == task_item.checkbox or
            element in task_item.checkbox_buttons or
            element in task_item.reorder_buttons
        ):
            return task_item

def transfer_task(task_item, is_checked, main_window):
    if is_checked:
        task_item.task.is_done = True
        main_window.tasks_data.uncompleted_task_items.remove(task_item)
        main_window.tasks_data.completed_task_items.append(task_item)
    else:
        task_item.task.is_done = False
        main_window.tasks_data.completed_task_items.remove(task_item)
        main_window.tasks_data.uncompleted_task_items.append(task_item)