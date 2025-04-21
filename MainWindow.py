from core.ComponentBuilderUI import ComponentBuilderUI
from core.ChangeVisualUI import ChangeVisualUI
from core.OnClickController import OnClickController
from core.TaskButtonManager import TaskButtonManager
from core.TaskCheckboxManager import TaskCheckboxManager
from core.TimeTracker import TimeTracker
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.visual_changer = ChangeVisualUI(self)
        self.component_builder = ComponentBuilderUI(self)
        self.time_tracker = TimeTracker(self)
        self.task_checkbox_manager = TaskCheckboxManager(self)
        self.task_button_manager = TaskButtonManager(self)
        self.on_click_controller = OnClickController(self)


        self.checkbox_dict = {}
        self.completed_checkbox_dict = {}
        self.dicts = [self.checkbox_dict, self.completed_checkbox_dict]

        self.dark_theme = False

        self.completed_task_opened = False
        self.completed_task_open_button = QPushButton("Completed Task")

        self.central_widget = QWidget(self)
        self.main_layout = QVBoxLayout()

        self.header_layout = QHBoxLayout()
        self.tasks_layout = QVBoxLayout()
        self.statusbar_layout = QHBoxLayout()

        self.scroll_area = QScrollArea(self)
        self.task_widget = QWidget(self)
        self.main_window_task_layout = QVBoxLayout()

        self.title_label = QLabel("To Do List", self)
        self.title_tasks_label = QLabel("Tasks", self)
        self.status_label = QLabel(self)

        self.add_task_plus_button = QPushButton(self)
        self.user_login_button = QPushButton(self)

        # ToolMenu PushButtons
        self.add_task_button = QPushButton("ADD TASK", self)
        self.del_tasks_button = QPushButton("DELETE ALL TASKS", self)
        self.change_theme_button = QPushButton("CHANGE THEME  ", self)
        self.about_button = QPushButton("ABOUT APP", self)

        # Menu
        self.menu = QMenu(self)
        self.menu_buttons = [self.add_task_button, self.del_tasks_button, self.change_theme_button, self.about_button]

        self.tool_button = QToolButton(self)

        self.init_UI()


    def init_UI(self):
        self.setWindowTitle("To Do List")
        self.setWindowIcon(QIcon("assets/MainWindow/todolist_icon.png"))
        self.setGeometry(900, 400, 800, 700)

        # completed tasks properties
        self.completed_task_open_button.setLayoutDirection(Qt.RightToLeft)
        self.completed_task_open_button.setIconSize(QSize(25,25))

        self.completed_task_open_button.clicked.connect(self.on_click_controller.on_click_completed_tasks_button)
        # ---

        self.change_theme_button.setLayoutDirection(Qt.RightToLeft)
        self.change_theme_button.setIconSize(QSize(35, 20))

        self.add_task_plus_button.setToolTip("Add new task")

        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)

        self.task_widget.setLayout(self.tasks_layout)
        self.scroll_area.setWidget(self.task_widget)
        self.main_window_task_layout.addWidget(self.scroll_area)

        self.setCentralWidget(self.central_widget)

        self.central_widget.setLayout(self.main_layout)
        self.main_layout.setAlignment(Qt.AlignTop)

        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.main_layout.addLayout(self.header_layout,1)
        self.main_layout.addLayout(self.main_window_task_layout,4)
        self.main_layout.addLayout(self.statusbar_layout,1)

        # add to header layout
        self.header_layout.addWidget(self.tool_button)
        self.header_layout.addWidget(self.title_label)
        self.header_layout.addWidget(self.user_login_button)

        self.tool_button.setFixedSize(100,100)
        self.title_label.setFixedHeight(100)
        self.user_login_button.setFixedSize(100,100)

        self.tool_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.user_login_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # add to tasks layout widgets and show
        self.tasks_layout.setAlignment(Qt.AlignTop)

        self.tasks_layout.setContentsMargins(75, 25, 75, 25)
        self.tasks_layout.setSpacing(30)

        self.title_tasks_label.setFixedHeight(50)

        self.task_checkbox_manager.show_all_task_checkboxes()

        # add to statusbar layout
        self.statusbar_layout.addWidget(self.status_label)
        self.status_label.setFixedHeight(25)

        # Title Labels
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_tasks_label.setAlignment(Qt.AlignCenter)

        # Status Label
        # self.set_statusbar_over_all_widgets()
        self.status_label.setAlignment(Qt.AlignCenter)

        # PushButtons
        self.add_task_plus_button.setIconSize(QSize(30, 30))

        # Login
        self.user_login_button.setIconSize(QSize(50, 50))

        # PushButtons connections
        self.add_task_button.clicked.connect(self.on_click_controller.on_click_task_button)
        self.del_tasks_button.clicked.connect(self.on_click_controller.on_click_task_button)
        self.change_theme_button.clicked.connect(self.on_click_controller.on_click_change_theme_button)
        self.about_button.clicked.connect(self.on_click_controller.on_click_about_button)
        self.add_task_plus_button.clicked.connect(self.on_click_controller.on_click_task_button)

        self.user_login_button.clicked.connect(self.print_dicts) # test column (delete)

        # Add action widgets into menu
        for button in self.menu_buttons:
            action = QWidgetAction(self)
            action.setDefaultWidget(button)
            self.menu.addAction(action)

        # Tool Menu Button
        self.tool_button.setIconSize(QSize(50, 50))
        self.tool_button.setPopupMode(QToolButton.InstantPopup)
        self.tool_button.setMenu(self.menu)

        # Styling
        self.title_label.setObjectName("title_label")
        self.title_tasks_label.setObjectName("title_tasks_label")
        self.status_label.setObjectName("status_label")
        self.user_login_button.setObjectName("user_login_button")
        self.tool_button.setObjectName("tool_button")
        self.add_task_plus_button.setObjectName("add_task_plus_button")
        self.add_task_button.setObjectName("add_task_button")
        self.del_tasks_button.setObjectName("del_tasks_button")
        self.change_theme_button.setObjectName("change_theme_button")
        self.about_button.setObjectName("about_button")
        self.completed_task_open_button.setObjectName("completed_task_open_button")

        self.visual_changer.change_UI_theme()
        self.show()

    def print_dicts(self):
        print(f"Unchecked: {self.checkbox_dict}")
        print(f"Checked: {self.completed_checkbox_dict}")