import uuid

class Task:

    def __init__(self, name, deadline, description):
        self.id = uuid.uuid4()
        self.name = name
        self.deadline = deadline
        self.description = description

        self.is_done = False