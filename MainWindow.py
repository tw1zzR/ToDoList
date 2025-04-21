from core.ComponentBuilderUI import ComponentBuilderUI
from core.ChangeVisualUI import ChangeVisualUI
from core.TaskButtonManager import TaskButtonManager
from core.TaskCheckboxManager import TaskCheckboxManager
from windows.TaskDialogBox import TaskDialogBox
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

        self.completed_task_open_button.clicked.connect(self.on_click_completed_tasks_button)
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
        self.add_task_button.clicked.connect(self.on_click_task_button)
        self.del_tasks_button.clicked.connect(self.on_click_task_button)
        self.change_theme_button.clicked.connect(self.on_click_change_theme_button)
        self.about_button.clicked.connect(self.on_click_about_button)
        self.add_task_plus_button.clicked.connect(self.on_click_task_button)

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


    # onclick methods

    def on_click_task_button(self):
        sender = self.sender()

        match sender.objectName():
            case "add_task_button" | "add_task_plus_button":
                add_task_dialog_box = TaskDialogBox()
                add_task_dialog_box.compare_with_main_win_theme(self.dark_theme)

                if add_task_dialog_box.exec_():
                    user_task_name, user_task_deadline, user_task_description = add_task_dialog_box.get_task_data()

                    self.component_builder.create_task_checkbox_with_buttons(user_task_name,
                                                                             user_task_deadline,
                                                                             user_task_description)
                    self.task_checkbox_manager.show_all_task_checkboxes()

                    if self.completed_task_opened:
                        self.task_checkbox_manager.delete_completed_tasks_from_ui()
                        self.task_checkbox_manager.show_completed_tasks()

            case "del_tasks_button":
                if self.checkbox_dict or self.completed_checkbox_dict:
                    delete_confirmation_dialog = self.component_builder.create_and_setup_delete_confirmation_dialog()

                    user_reply = delete_confirmation_dialog.exec_()

                    if user_reply == QMessageBox.Yes:
                        for dictionary in self.dicts:
                            if dictionary:
                                list_of_checkboxes = list(dictionary.keys())
                                for checkbox in list_of_checkboxes:
                                    self.task_checkbox_manager.delete_task_checkbox_with_buttons(checkbox,*self.dicts)
                        self.component_builder.current_task_info_window = None

                    self.task_checkbox_manager.show_all_task_checkboxes()

                    if self.completed_task_opened:
                        self.task_checkbox_manager.delete_completed_tasks_from_ui()
                        self.task_checkbox_manager.show_completed_tasks()
                else:
                    delete_tasks_error = self.component_builder.create_warning_messagebox("Delete all tasks","Task list is empty.")
                    delete_tasks_error.exec_()


    def on_click_change_theme_button(self):
        self.visual_changer.change_UI_theme()


    def on_click_about_button(self):
        about_app_dialog = self.component_builder.create_and_setup_about_app_dialog()
        about_app_dialog.exec_()


        # Set checkbox checked method
    def on_click_task_checkbox(self):
        sender_checkbox = self.sender()

        if self.completed_checkbox_dict:
            self.completed_task_open_button.hide()
        else:
            self.completed_task_open_button.show()

        match sender_checkbox.isChecked():
            case True:
                self.visual_changer.task_checkbox_set_style_sheet(sender_checkbox, True)

                self.task_checkbox_manager.move_task_to_another_dict(sender_checkbox, self.checkbox_dict, self.completed_checkbox_dict)

                self.task_checkbox_manager.remove_completed_task_from_ui(sender_checkbox)

                if self.completed_task_opened:
                    self.task_checkbox_manager.show_all_task_checkboxes()

                    self.task_checkbox_manager.delete_completed_tasks_from_ui()
                    self.task_checkbox_manager.show_completed_tasks()

            case False:
                self.visual_changer.task_checkbox_set_style_sheet(sender_checkbox, False)

                self.task_checkbox_manager.move_task_to_another_dict(sender_checkbox, self.completed_checkbox_dict, self.checkbox_dict)

                if self.completed_task_opened:
                    self.task_checkbox_manager.show_all_task_checkboxes()
                    self.visual_changer.task_checkbox_set_style_sheet(sender_checkbox, False)

                    self.task_checkbox_manager.delete_completed_tasks_from_ui()
                    self.task_checkbox_manager.show_completed_tasks()


        # Set checkbox buttons methods
    def on_click_task_info_checkbox_button(self):
        sender = self.sender()
        sender_checkbox = self.task_button_manager.find_checkbox_by_checkbox_button(sender)

        self.component_builder.create_task_info_messagebox_checkbox_button(sender_checkbox)


    def on_click_edit_task_checkbox_button(self):
        sender = self.sender()
        sender_checkbox = self.task_button_manager.find_checkbox_by_checkbox_button(sender)

        # Get primary checkbox data
        for dictionary in self.dicts:
            if sender_checkbox in dictionary:
                sender_checkbox_task_name = dictionary[sender_checkbox]["name"]
                sender_checkbox_task_deadline = dictionary[sender_checkbox]["deadline"]
                sender_checkbox_task_description = dictionary[sender_checkbox]["description"]
                break

        self.component_builder.create_and_open_edit_task_dialog(sender_checkbox,
                                                                sender_checkbox_task_name,
                                                                sender_checkbox_task_deadline,
                                                                sender_checkbox_task_description)


    def on_click_delete_task_checkbox_button(self):
        sender = self.sender()
        sender_checkbox = self.task_button_manager.find_checkbox_by_checkbox_button(sender)

        self.task_checkbox_manager.delete_task_checkbox_with_buttons(sender_checkbox, self.checkbox_dict, self.completed_checkbox_dict)

        self.task_checkbox_manager.show_all_task_checkboxes()

        if self.completed_task_opened:
            self.task_checkbox_manager.delete_completed_tasks_from_ui()
            self.task_checkbox_manager.show_completed_tasks()


    def on_click_reorder_button(self):
        sender = self.sender()
        sender_checkbox = self.task_button_manager.find_checkbox_by_checkbox_button(sender)

        for data in self.checkbox_dict.values():
            if data["reorder_buttons"][0] is sender:
                self.task_checkbox_manager.move_up_down_checkbox(sender_checkbox, "up")
            elif data["reorder_buttons"][1] is sender:
                self.task_checkbox_manager.move_up_down_checkbox(sender_checkbox, "down")
            else:
                continue
            break


    def on_click_completed_tasks_button(self):
        self.task_checkbox_manager.show_all_task_checkboxes()

        if self.completed_task_opened:
            self.completed_task_opened = False
            self.task_checkbox_manager.delete_completed_tasks_from_ui()
        else:
            self.completed_task_opened = True
            self.task_checkbox_manager.show_completed_tasks()

        self.visual_changer.change_completed_task_button_icon()