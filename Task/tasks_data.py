

class TasksData:

    def __init__(self):
        self.tasks = []
        self.task_items = []

        self.completed_tasks = []
        self.completed_task_items = []

        self.uncompleted_tasks = []
        self.uncompleted_task_items = []


    def move_task_to_another_dict(self, completed_task_checkbox, from_dict, to_dict):
        if completed_task_checkbox in self.main_window.checkbox_order:
            checkbox_index  = self.main_window.checkbox_order.index(completed_task_checkbox)
            checkbox_key = self.main_window.checkbox_order[checkbox_index]

            completed_task_checkbox_data = from_dict.pop(checkbox_key)
            to_dict[completed_task_checkbox] = completed_task_checkbox_data