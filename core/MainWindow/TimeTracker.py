from PyQt5.QtCore import *

class TimeTracker:

    def __init__(self, main_window):
        self.main_window = main_window

        self.status_timer = QTimer()
        self.refresh_task_timer = QTimer()

        self.init_timer()

    def init_timer(self):
        self.start_track_status_realtime()
        self.status_timer.timeout.connect(self.refresh_status_realtime)

        self.start_track_task_deadline()
        self.refresh_task_timer.timeout.connect(self.refresh_task_deadline)

    def start_track_status_realtime(self):
        self.status_timer.start(1000) # 1 sec

    def start_track_task_deadline(self):
        self.refresh_task_timer.start(60000) # 60 sec

    def refresh_status_realtime(self):
        current_time = QDateTime.currentDateTime()

        # Status bar realtime
        formatted_realtime = current_time.toString("MMMM dd, hh:mm")
        self.main_window.status_label.setText(formatted_realtime)

    def refresh_task_deadline(self):
        current_time = QDateTime.currentDateTime()

        formatted_deadline_realtime = current_time.toString("dd.MM.yyyy HH:mm")
        formatted_deadline_realtime = QDateTime.fromString(formatted_deadline_realtime, "dd.MM.yyyy HH:mm")

        for task_item in self.main_window.tasks_data.uncompleted_task_items:
            task_deadline_str = task_item.task.deadline
            task_deadline = QDateTime.fromString(task_deadline_str, "dd.MM.yyyy HH:mm")

            if current_time > task_deadline:
                task_item.checkbox.setStyleSheet(
                    "background-color: rgb(242, 155, 155);"
                    "border: 3px solid rgb(130, 57, 57);")