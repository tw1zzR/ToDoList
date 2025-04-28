import uuid


class Task:

    def __init__(self, name, deadline, description):
        self.id = uuid.uuid4()
        self.name = name
        self.deadline = deadline
        self.description = description

        self.is_complete = False


t = Task("Task 1", 10, "Task description")
t1 = Task("Task 2", 20, "Task description")
print(t.id)
print(t1.id)