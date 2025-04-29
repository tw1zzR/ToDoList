from Task.tasks_data import TasksData
from core.MainWindow.checkbox_element_builder import CheckboxElementBuilder
from core.MainWindow.main_window_theme_manager import MainWindowThemeManager
from core.MainWindow.TaskCheckboxManager import TaskCheckboxManager
from core.MainWindow.on_click_controller import OnClickController
from core.MainWindow.TimeTracker import TimeTracker
from modules.window_builders import main_window_builder
from TaskDialog import TaskDialog
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # -- Data
        self.tasks_data = TasksData()

        # -- Managers
        self.visual_changer = MainWindowThemeManager(self)
        self.checkbox_elems_builder = CheckboxElementBuilder(self)
        self.time_tracker = TimeTracker(self)
        self.task_checkbox_manager = TaskCheckboxManager(self)
        self.on_click_controller = OnClickController(self)

        # -- Windows
        self.task_info_window = TaskDialog(is_input=False)
        self.task_input_window = TaskDialog(is_input=True)
        self.task_info_window.hide()
        self.task_input_window.hide()

        # -- State Flags
        self.dark_theme = True
        self.completed_task_opened = False

        # -- Widgets
        self.central_widget = QWidget(self)
        self.scroll_area = QScrollArea(self)
        self.task_widget = QWidget(self)

        # Layouts
        self.main_layout = QVBoxLayout()
        self.header_layout = QHBoxLayout()
        self.tasks_layout = QVBoxLayout()
        self.statusbar_layout = QHBoxLayout()
        self.main_window_task_layout = QVBoxLayout()

        # Labels
        self.title_label = QLabel("To Do List", self)
        self.title_tasks_label = QLabel("Tasks", self)
        self.status_label = QLabel(self)

        # PushButtons
        self.add_task_plus_button = QPushButton(self)
        self.user_login_button = QPushButton(self)
        self.add_task_button = QPushButton("ADD TASK", self)
        self.del_tasks_button = QPushButton("DELETE ALL TASKS", self)
        self.change_theme_button = QPushButton("CHANGE THEME  ", self)
        self.about_button = QPushButton("ABOUT APP", self)
        self.completed_task_open_button = QPushButton("Completed Task")

        # ToolMenu
        self.menu = QMenu(self)
        self.menu_buttons = [self.add_task_button, self.del_tasks_button, self.change_theme_button, self.about_button]
        self.tool_button = QToolButton(self)

        # Init UI
        main_window_builder.setup_ui(self)
        self.visual_changer.apply_dark_theme()
        self.task_checkbox_manager.refresh_ui_task_checkboxes()
        self.show()

    def print_dicts(self):
        print(f"Task Items: {self.tasks_data.task_items}")
        print(f"Checked task items: {self.tasks_data.completed_task_items}")
        print(f"Unchecked task items: {self.tasks_data.uncompleted_task_items}")

        for task_item in self.tasks_data.task_items:
            print(f"Task: {task_item.task.name}, {task_item.task.deadline}, {task_item.task.description} - {task_item.task.is_done}")
            print(f"checkbox: {task_item.checkbox}")
            print(f"checkbox_buttons: {task_item.checkbox_buttons}")
            print(f"reorder_buttons: {task_item.reorder_buttons}")