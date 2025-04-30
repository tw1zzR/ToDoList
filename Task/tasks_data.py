
class TasksData:

    def __init__(self):
        self.task_items = []

        self.completed_task_items = [task for task in self.task_items if task.is_done]
        self.uncompleted_task_items = [task for task in self.task_items if not task.is_done]

        self.task_lists = [self.task_items, self.completed_task_items, self.uncompleted_task_items]

    def insert_task(self, task_item):
        self.task_items.append(task_item)

        if task_item.task.is_done:
            self.completed_task_items.append(task_item)
        else:
            self.uncompleted_task_items.append(task_item)