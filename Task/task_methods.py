from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QSizePolicy
from Task.task import Task
from Task.task_item import TaskItem
from Task.tasks_data import TasksData
from modules.MainWindow import main_window_tools


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