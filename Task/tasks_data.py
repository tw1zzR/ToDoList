

class TasksData:

    def __init__(self):
        self.task_items = []

        self.completed_task_items = [task for task in self.task_items if task.is_done]

        self.uncompleted_task_items = [task for task in self.task_items if not task.is_done]

    def insert_task(self, task_item):
        self.task_items.append(task_item)

        if task_item.task.is_done:
            self.completed_task_items.append(task_item)
        else:
            self.uncompleted_task_items.append(task_item)

    # def move_task_to_another_dict(self, completed_task_checkbox, from_dict, to_dict):
    #     if completed_task_checkbox in self.main_window.checkbox_order:
    #         checkbox_index  = self.main_window.checkbox_order.index(completed_task_checkbox)
    #         checkbox_key = self.main_window.checkbox_order[checkbox_index]
    #
    #         completed_task_checkbox_data = from_dict.pop(checkbox_key)
    #         to_dict[completed_task_checkbox] = completed_task_checkbox_data