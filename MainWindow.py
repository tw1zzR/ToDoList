from core.MainWindow.ComponentBuilderUI import ComponentBuilderUI
from core.MainWindow.ChangeVisualUI import ChangeVisualUI
from core.MainWindow.OnClickController import OnClickController
from core.MainWindow.TaskButtonManager import TaskButtonManager
from core.MainWindow.TaskCheckboxManager import TaskCheckboxManager
from core.MainWindow.TimeTracker import TimeTracker
from PyQt5.QtWidgets import *
from modules.MainWindow import main_window_builder


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # -- Managers
        self.visual_changer = ChangeVisualUI(self)
        self.component_builder = ComponentBuilderUI(self)
        self.time_tracker = TimeTracker(self)
        self.task_checkbox_manager = TaskCheckboxManager(self)
        self.task_button_manager = TaskButtonManager(self)
        self.on_click_controller = OnClickController(self)

        # -- Data Structures
        self.checkbox_order = []
        self.checkbox_dict = {}
        self.completed_checkbox_dict = {}
        self.dicts = [self.checkbox_dict, self.completed_checkbox_dict]

        # -- State Flags
        self.dark_theme = False
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

        self.init_UI()

    def init_UI(self):
        main_window_builder.setup_UI(self)
        self.task_checkbox_manager.show_all_task_checkboxes()
        self.visual_changer.change_UI_theme()
        self.show()

    def print_dicts(self):
        print(f"Checkbox postition: {self.checkbox_order}")
        print(f"Unchecked: {self.checkbox_dict}")
        print(f"Checked: {self.completed_checkbox_dict}")