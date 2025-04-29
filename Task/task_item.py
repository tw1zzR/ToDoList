
class TaskItem:

    def __init__(self, task, checkbox, checkbox_buttons, reorder_buttons):
        self.task = task
        self.checkbox = checkbox
        self.checkbox_buttons = checkbox_buttons
        self.reorder_buttons = reorder_buttons
        self.checkbox_layout = None