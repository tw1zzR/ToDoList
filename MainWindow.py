import copy
from collections import OrderedDict
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from TaskDialogBox import TaskDialogBox
from TaskInfoMessageBox import CustomTaskInfoMessageBox


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.checkbox_dict = {}
        self.completed_checkbox_dict = {}

        self.current_task_info_window = None
        self.dark_theme = False

        ####
        self.completed_task_opened = False
        self.completed_task_layout = QVBoxLayout()
        ####

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

        ####
        self.completed_task_open_button = QPushButton("Completed Task")
        ####
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

        self.status_timer = QTimer(self)
        self.refresh_task_timer = QTimer(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("To Do List")
        self.setWindowIcon(QIcon("assets/MainWindow/todolist_icon.png"))
        self.setGeometry(900, 400, 800, 700)

        #test
        ####
        self.completed_task_open_button.setLayoutDirection(Qt.RightToLeft)
        self.completed_task_open_button.setIconSize(QSize(25,25))

        self.completed_task_open_button.clicked.connect(self.on_click_completed_tasks_button)

        self.completed_task_layout.setContentsMargins(0, 0, 0, 0)
        self.completed_task_layout.setSpacing(0)
        ####
        # ---

        self.change_theme_button.setLayoutDirection(Qt.RightToLeft)
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

        self.show_all_task_checkboxes()

        # add to statusbar layout
        self.statusbar_layout.addWidget(self.status_label)
        self.status_label.setFixedHeight(25)

        self.start_track_status_realtime()
        self.status_timer.timeout.connect(self.refresh_status_realtime)

        self.start_track_task_deadline()
        self.refresh_task_timer.timeout.connect(self.refresh_task_deadline)

        # Title Labels
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_tasks_label.setAlignment(Qt.AlignCenter)

        # Status Label
        self.set_statusbar_over_all_widgets()
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

        self.user_login_button.clicked.connect(self.print_buttons) # test column (delete)

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

        self.changeTheme()

        self.show()

    def print_buttons(self):
        print(self.checkbox_dict)
        print(self.current_task_info_window)

        print(self.completed_checkbox_dict)

    def set_statusbar_over_all_widgets(self):
        self.status_label.raise_()

    # checkbox methods
    def create_task_checkbox_with_buttons(self, user_task_name, user_task_deadline, user_task_description):
        task_checkbox = QCheckBox(user_task_name, self)
        task_checkbox.stateChanged.connect(self.on_click_task_checkbox)
        task_checkbox.setFixedHeight(50)

        checkbox_moveup_button = QPushButton(self)
        checkbox_movedown_button = QPushButton(self)

        checkbox_moveup_button.setFixedSize(50,25)
        checkbox_movedown_button.setFixedSize(50,25)

        checkbox_reorder_buttons = [checkbox_moveup_button, checkbox_movedown_button]

        task_info_button = QPushButton(self)
        edit_task_button = QPushButton(self)
        delete_task_button = QPushButton(self)

        task_info_button.setToolTip("View task details")
        edit_task_button.setToolTip("Edit task")
        delete_task_button.setToolTip("Delete task")

        checkbox_buttons = [task_info_button, edit_task_button, delete_task_button]

        for button in checkbox_buttons:
            button.setFixedSize(50, 50)
            button.setIconSize(QSize(30, 30))
            if self.dark_theme:
                button.setStyleSheet(
                    "background-color: rgb(246, 246, 246);"
                    "border-top: 3px solid rgb(222, 222, 222);"
                    "border-bottom: 3px solid rgb(222, 222, 222);"
                    "border-right: 3px solid rgb(222, 222, 222);")
            else:
                button.setStyleSheet(
                    "background-color: rgb(60, 60, 60);"
                    "border-top: 3px solid rgb(30, 30, 30);"
                    "border-bottom: 3px solid rgb(30, 30, 30);"
                    "border-right: 3px solid rgb(30, 30, 30);")

        for reorder_button in checkbox_reorder_buttons:
            reorder_button.setStyleSheet("background-color: transparent;")

        self.checkbox_dict[task_checkbox] = {
            "buttons": checkbox_buttons,
            "reorder_buttons": checkbox_reorder_buttons,
            "name": user_task_name,
            "deadline": user_task_deadline,
            "description": user_task_description
        }

        self.change_checkboxes_button_icons_theme()
        self.connect_checkbox_buttons()

    def find_checkbox_by_checkbox_button(self, clicked_button):
        for checkbox, data in self.checkbox_dict.items():
            if clicked_button in data["buttons"] or clicked_button in data["reorder_buttons"]:
                return checkbox

    def connect_checkbox_buttons(self):
        for checkbox, data in self.checkbox_dict.items():
            task_info_button  = data["buttons"][0]
            edit_task_button  = data["buttons"][1]
            delete_task_button = data["buttons"][2]

            if not hasattr(task_info_button, "_clicked_connected"):
                task_info_button.clicked.connect(self.on_click_task_info_checkbox_button)
                task_info_button._clicked_connected = True
            if not hasattr(edit_task_button, "_clicked_connected"):
                edit_task_button.clicked.connect(self.on_click_edit_task_checkbox_button)
                edit_task_button._clicked_connected = True
            if not hasattr(delete_task_button, "_clicked_connected"):
                delete_task_button.clicked.connect(self.on_click_delete_task_checkbox_button)
                delete_task_button._clicked_connected = True
            for reorder_button in data["reorder_buttons"]:
                if not hasattr(reorder_button, "_clicked_connected"):
                    reorder_button.clicked.connect(self.on_click_reorder_button)
                    reorder_button._clicked_connected = True

    def create_task_info_messagebox_checkbox_button(self, checkbox_sender):
        task_name = self.checkbox_dict[checkbox_sender]["name"]
        task_deadline = self.checkbox_dict[checkbox_sender]["deadline"]
        task_description = self.checkbox_dict[checkbox_sender]["description"]

        if self.current_task_info_window:
            self.current_task_info_window.close()
            self.current_task_info_window.set_task_info_msgbox_new_data(task_name, task_deadline, task_description)
        else:
            self.current_task_info_window = CustomTaskInfoMessageBox(task_name, task_deadline, task_description)

        self.current_task_info_window.compare_with_main_win_theme(self.dark_theme)

        self.current_task_info_window.show()

    def delete_task_checkbox_with_buttons(self, checkbox_sender):
        if checkbox_sender in self.checkbox_dict:
            checkbox_buttons = self.checkbox_dict[checkbox_sender]["buttons"]
            reorder_buttons = self.checkbox_dict[checkbox_sender]["reorder_buttons"]

            for button in checkbox_buttons[:]:
                button.setParent(None)
                button.deleteLater()
            for reorder_button in reorder_buttons[:]:
                reorder_button.setParent(None)
                reorder_button.deleteLater()

            checkbox_sender.setParent(None)
            checkbox_sender.deleteLater()

            del self.checkbox_dict[checkbox_sender]

        if checkbox_sender in self.completed_checkbox_dict:
            del self.completed_checkbox_dict[checkbox_sender]

    def create_and_open_edit_task_dialog(self, sender_checkbox, primary_task_name, primary_task_deadline, primary_task_description):
        edit_task_dialogbox = TaskDialogBox()

        edit_task_dialogbox.compare_with_main_win_theme(self.dark_theme)

        date_format = "dd.MM.yyyy HH:mm"
        primary_user_task_deadline = QDateTime.fromString(primary_task_deadline, date_format)

        # Set primary checkbox data
        edit_task_dialogbox.user_input_task_name.setText(primary_task_name)
        edit_task_dialogbox.user_input_task_deadline.setDateTime(primary_user_task_deadline)
        edit_task_dialogbox.user_input_task_description.setText(primary_task_description)

        if edit_task_dialogbox.exec_():
            # Change to edited checkbox data
            edited_task_name, edited_task_deadline, edited_task_description = edit_task_dialogbox.get_task_data()

            self.checkbox_dict[sender_checkbox]["name"] = edited_task_name
            self.checkbox_dict[sender_checkbox]["deadline"] = edited_task_deadline
            self.checkbox_dict[sender_checkbox]["description"] = edited_task_description

            sender_checkbox.setText(edited_task_name)
            self.show_all_task_checkboxes()

    def clear_layout(self, layout):
        reversed_layout = reversed(range(layout.count()))
        for i in reversed_layout:
            item = layout.itemAt(i).widget()
            layout.removeItem(item)

    def show_all_task_checkboxes(self):
        self.clear_layout(self.tasks_layout)

        ####
        #self.clear_layout(self.completed_task_layout)
        ####

        title_tasks_layout = QHBoxLayout()

        title_tasks_layout.addStretch()
        title_tasks_layout.addWidget(self.title_tasks_label, alignment=Qt.AlignCenter)
        title_tasks_layout.addStretch()

        self.tasks_layout.addLayout(title_tasks_layout)

        for checkbox, data in self.checkbox_dict.items():

            checkbox_layout = QHBoxLayout()
            checkbox_layout.setContentsMargins(0,0,0,0)
            checkbox_layout.setSpacing(0)

            moveup_btn = data["reorder_buttons"][0]
            movedown_btn = data["reorder_buttons"][1]

            reorder_layout = QVBoxLayout()

            for reorder_button in [moveup_btn, movedown_btn]:
                reorder_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                reorder_button.show()
                reorder_layout.addWidget(reorder_button)

            checkbox_layout.addLayout(reorder_layout)

            checkbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            checkbox_layout.addWidget(checkbox)

            for button in data["buttons"]:
                button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                button.show()
                checkbox_layout.addWidget(button)
            checkbox_layout.addSpacing(50)

            self.tasks_layout.addLayout(checkbox_layout)

        # (+) button layout
        plus_button_layout = QHBoxLayout()

        plus_button_layout.addSpacing(50)
        plus_button_layout.addWidget(self.add_task_plus_button, alignment=Qt.AlignLeft)
        plus_button_layout.addStretch()

        self.add_task_plus_button.setFixedSize(50, 50)
        self.tasks_layout.addLayout(plus_button_layout)

        ####
        # for checkbox in self.checkbox_dict:
        #     if checkbox.isChecked():
        #         self.show_completed_tasks()
        #         break
        ####

        self.set_statusbar_over_all_widgets()

    def task_checkbox_set_style_sheet(self, sender, checked):
        if checked:
            sender.setStyleSheet(
                "background-color: rgb(93, 217, 110);"
                "border-color: rgb(66, 135, 76);")
        else:
            if self.dark_theme:
                sender.setStyleSheet(
                    "background-color: rgb(246, 246, 246);"
                    "border: 3px solid rgb(222, 222, 222);")
            else:
                sender.setStyleSheet(
                    "background-color: rgb(60, 60, 60);"
                    "border: 3px solid rgb(30, 30, 30);")

    def create_and_setup_delete_confirmation_dialog(self):
        delete_confirmation_dialog = QMessageBox()

        delete_confirmation_dialog.setWindowTitle("Delete All Tasks")
        delete_confirmation_dialog.setWindowIcon(QIcon("assets/TaskDialogBox/addtask_dialogbox_icon.png"))
        delete_confirmation_dialog.setText("Are you sure you want to delete all tasks?")

        delete_confirmation_dialog.setIcon(QMessageBox.Warning)
        delete_confirmation_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        delete_confirmation_dialog.setStyleSheet("""
                        QMessageBox {
                            font-family: Helvetica;
                            color: rgb(0,0,0);
                            font-size: 16px;
                        }
                        QPushButton {
                            font-family: Helvetica;
                            font-size: 14px;
                        }
                        """)

        return delete_confirmation_dialog

    def create_and_setup_about_app_dialog(self):
        about_app_dialog = QMessageBox()

        about_app_dialog.setWindowTitle("About App")
        about_app_dialog.setWindowIcon(QIcon("assets/AboutAppMessageBox/information_icon.png"))
        about_app_dialog.setTextFormat(Qt.RichText)
        about_app_dialog.setText("My GitHub: <a href=\"https://github.com/tw1zzR\">tw1zzR</a>")
        about_app_dialog.setIcon(QMessageBox.Information)

        about_app_dialog.setStyleSheet("""
                                QMessageBox {
                                    font-family: Helvetica;
                                    color: rgb(0,0,0);
                                    font-size: 16px;
                                }
                                QPushButton {
                                    font-family: Helvetica;
                                    font-size: 14px;
                                }
                                """)

        return about_app_dialog

    # Refresh realtime statusbar every 1 sec
    def start_track_status_realtime(self):
        self.status_timer.start(1000)

    def refresh_status_realtime(self):
        current_time = QDateTime.currentDateTime()

        # Status bar realtime
        formatted_realtime = current_time.toString("MMMM dd, hh:mm")
        self.status_label.setText(formatted_realtime)

    # Refresh deadline every 5 min
    def start_track_task_deadline(self):
        self.refresh_task_timer.start(300000)

    def refresh_task_deadline(self):
        current_time = QDateTime.currentDateTime()

        formatted_deadline_realtime = current_time.toString("dd.MM.yyyy HH:mm")
        formatted_deadline_realtime = QDateTime.fromString(formatted_deadline_realtime, "dd.MM.yyyy HH:mm")

        for checkbox, task_data in self.checkbox_dict.items():
            task_deadline_str = task_data["deadline"]
            task_deadline = QDateTime.fromString(task_deadline_str, "dd.MM.yyyy HH:mm")

            if current_time > task_deadline and not checkbox.isChecked():
                checkbox.setStyleSheet(
                    "background-color: rgb(242, 155, 155);"
                    "border: 3px solid rgb(130, 57, 57);")
            elif not checkbox.isChecked():
                if self.dark_theme:
                    checkbox.setStyleSheet(
                        "background-color: rgb(246, 246, 246);"
                        "border: 3px solid rgb(222, 222, 222);")
                else:
                    checkbox.setStyleSheet(
                        "background-color: rgb(60, 60, 60);"
                        "border: 3px solid rgb(30, 30, 30);")

    def move_up_down_checkbox(self, target_checkbox, up_down):
        items = list(self.checkbox_dict.items())

        for i, (checkbox, _) in enumerate(items):
            if checkbox is target_checkbox:
                break

        if i == 0 and up_down == "up":
            return
        elif i == len(items) - 1 and up_down == "down":
            return

        match up_down:
            case "up":
                items[i-1], items[i] = items[i], items[i-1]
            case "down":
                items[i+1], items[i] = items[i], items[i+1]

        self.checkbox_dict = OrderedDict(items)
        self.show_all_task_checkboxes()

    ####
    # def create_completed_tasks_button(self):
    #     completed_title_tasks_layout = QHBoxLayout()
    #
    #     completed_title_tasks_layout.addStretch()
    #     completed_title_tasks_layout.addWidget(self.completed_task_open_button, alignment=Qt.AlignCenter)
    #     completed_title_tasks_layout.addStretch()
    #
    #     self.completed_task_layout.addLayout(completed_title_tasks_layout)
    #     self.tasks_layout.addLayout(self.completed_task_layout)
    #
    # def show_completed_tasks(self):
    #     self.clear_layout(self.completed_task_layout)
    #
    #     completed_title_tasks_layout = QHBoxLayout()
    #
    #     completed_title_tasks_layout.addStretch()
    #     completed_title_tasks_layout.addWidget(self.completed_task_open_button, alignment=Qt.AlignCenter)
    #     completed_title_tasks_layout.addStretch()
    #
    #     self.completed_task_layout.addLayout(completed_title_tasks_layout)
    #
    #     for checkbox, data in self.checkbox_dict.items():
    #         if checkbox.isChecked():
    #             checkbox_layout = QHBoxLayout()
    #             checkbox_layout.setContentsMargins(0, 0, 0, 0)
    #             checkbox_layout.setSpacing(0)
    #
    #             clone_checked_checkbox = QCheckBox(data["name"])
    #             clone_checked_checkbox.setChecked(True)
    #             clone_checked_checkbox.setStyleSheet(
    #                 "background-color: rgb(93, 217, 110);"
    #                 "border-color: rgb(66, 135, 76);")
    #
    #             checkbox_layout.addSpacing(50)
    #             checkbox_layout.addWidget(clone_checked_checkbox)
    #             checkbox_layout.addSpacing(50)
    #
    #             self.completed_task_layout.addSpacing(25)
    #             self.completed_task_layout.addLayout(checkbox_layout)
    #
    # def hide_completed_tasks(self):
    #     self.hide_layout_widgets(self.completed_task_layout)
    #
    # def hide_layout_widgets(self, layout):
    #     if layout is None:
    #         return
    #
    #     for i in range(layout.count()):
    #         item = layout.itemAt(i)
    #         if item.widget():
    #             item.widget().setVisible(False)
    #         elif item.layout():
    #             self.hide_layout_widgets(item.layout())

    # def hide_completed_tasks(self):
    #     # self.clear_completed_task_layout(self.completed_task_layout)
    #     layout = self.completed_task_layout
    #
    #     for i in range(layout.count()):
    #         item = layout.itemAt(i)
    #         if item.widget():
    #             item.widget().setVisible(False)
    #         elif item.layout():
    #             self.hide_completed_tasks(item.layout())
    #
    #     # completed_title_tasks_layout = QHBoxLayout()
    #     #
    #     # completed_title_tasks_layout.addStretch()
    #     # completed_title_tasks_layout.addWidget(self.completed_task_open_button, alignment=Qt.AlignCenter)
    #     # completed_title_tasks_layout.addStretch()
    #     #
    #     # self.completed_task_layout.addLayout(completed_title_tasks_layout)

        #
        #     completed_title_tasks_layout.addStretch()
        #     completed_title_tasks_layout.addWidget(self.completed_task_open_button, alignment=Qt.AlignCenter)
        #     completed_title_tasks_layout.addStretch()
        #
        #     self.completed_task_layout.addLayout(completed_title_tasks_layout)


    ####

    # def clear_completed_task_layout(self, layout):
    #     for i in range(layout.count()):  # Проходим по всем элементам макета
    #         item = layout.itemAt(i)
    #         widget = item.widget()  # Получаем виджет, если он есть
    #         if widget:  # Если элемент является виджетом
    #             layout.removeWidget(widget)  # Убираем виджет из макета
    #             widget.deleteLater()

    # Change Theme and SetStyleSheet methods
    def changeTheme(self):
        if self.dark_theme:
            self.apply_light_theme()
            self.change_theme_button.setIcon(QIcon("assets/MainWindow/ToolMenu/light_theme_icon.png"))
        else:
            self.apply_dark_theme()
            self.change_theme_button.setIcon(QIcon("assets/MainWindow/ToolMenu/dark_theme_icon.png"))

        self.change_theme_button.setIconSize(QSize(35, 20))

    def change_checkboxes_button_icons_theme(self):
        white_reorder_buttons_path = ["assets/MainWindow/white_moveup_arrow_icon.png",
                                      "assets/MainWindow/white_movedown_arrow_icon.png"]

        gray_reorder_buttons_path = ["assets/MainWindow/gray_moveup_arrow_icon.png",
                                     "assets/MainWindow/gray_movedown_arrow_icon.png"]

        white_checkbox_buttons_path = ["assets/MainWindow/CheckBox/white_task_info_button_V1_icon.png",
                              "assets/MainWindow/CheckBox/white_edit_task_button_icon.png",
                              "assets/MainWindow/CheckBox/white_delete_task_button_icon.png"]

        gray_checkbox_buttons_path = ["assets/MainWindow/CheckBox/gray_task_info_button_V1_icon.png",
                             "assets/MainWindow/CheckBox/gray_edit_task_button_icon.png",
                             "assets/MainWindow/CheckBox/gray_delete_task_button_icon.png"]

        if self.dark_theme:
            for task_data in self.checkbox_dict.values():
                i = 0
                for reorder_button in task_data["reorder_buttons"]:
                    reorder_button.setIcon(QIcon(white_reorder_buttons_path[i]))
                    i += 1
                i = 0
                for checkbox_button in task_data["buttons"]:
                    checkbox_button.setIcon(QIcon(gray_checkbox_buttons_path[i]))
                    i += 1
        else:
            for task_data in self.checkbox_dict.values():
                i = 0
                for reorder_button in task_data["reorder_buttons"]:
                    reorder_button.setIcon(QIcon(gray_reorder_buttons_path[i]))
                    i += 1
                i = 0
                for checkbox_button in task_data["buttons"]:
                    checkbox_button.setIcon(QIcon(white_checkbox_buttons_path[i]))
                    i += 1

    def change_completed_task_button_icon(self):
        if self.dark_theme:
            if self.completed_task_opened:
                self.completed_task_open_button.setIcon(
                    QIcon("assets/MainWindow/white_open_completed_task_section_icon.png"))
            else:
                self.completed_task_open_button.setIcon(
                    QIcon("assets/MainWindow/white_closed_completed_task_section_icon.png"))
        else:
            if self.completed_task_opened:
                self.completed_task_open_button.setIcon(QIcon("assets/MainWindow/gray_open_completed_task_section_icon.png"))
            else:
                self.completed_task_open_button.setIcon(QIcon("assets/MainWindow/gray_closed_completed_task_section_icon.png"))

    def apply_light_theme(self):
        self.dark_theme = False

        for checkbox, task_data in self.checkbox_dict.items():
            checkbox.setChecked(False)

        # to White
            # icons
        self.tool_button.setIcon(QIcon("assets/MainWindow/gray_menu_icon.png"))
        self.user_login_button.setIcon(QIcon("assets/MainWindow/gray_user_icon.png"))
        self.add_task_plus_button.setIcon(QIcon("assets/MainWindow/white_add_task_plus_button_v1_icon.png"))

        self.change_checkboxes_button_icons_theme()
        self.change_completed_task_button_icon()

        for checkbox, data in self.checkbox_dict.items():
            for button in data["buttons"]:
                button.setStyleSheet(
                    "background-color: rgb(60, 60, 60);"
                    "border-top: rgb(30, 30, 30);"
                    "border-bottom: 3px solid rgb(30, 30, 30);"
                    "border-right: 3px solid rgb(30, 30, 30);")

            # widgets
        self.setStyleSheet("""
            QLabel {
                font-family: Helvetica;
                color: rgb(44,44,44)
            }
            QLabel#title_label {                                                     
                font-size: 40px;
                font: bold;
                background-color: rgb(181, 181, 181);
                border-bottom: 2px solid rgb(41, 41, 39);
            }
            QLabel#title_tasks_label {
                font-size: 36px;
                font: bold;
            }
            QLabel#status_label {
                font-size: 14px;
                color: rgb(235,235,235);
                background-color: rgb(110, 110, 110); 
            }
            QToolButton#tool_button, QPushButton#user_login_button {
                background-color: rgb(181, 181, 181);
                border-radius: 0px;
                border-bottom: 2px solid rgb(41, 41, 39);
            }
            QPushButton {
                font-family: Helvetica;
                font-size: 18px;
                font: bold;
                color: rgb(44,44,44);
                background-color: rgb(235, 235, 235);
                padding: 15px;
            }
            QPushButton#add_task_button, QPushButton#del_tasks_button, 
            QPushButton#change_theme_button, QPushButton#about_button {
                color: rgb(225, 225, 220);
                background-color: rgb(79, 79, 75);
            }
            QPushButton#add_task_button:hover, QPushButton#del_tasks_button:hover, 
            QPushButton#change_theme_button:hover, QPushButton#about_button:hover {
                border: 2px solid rgb(140, 140, 140);
            }
            QPushButton#add_task_plus_button {
                background-color: rgb(60, 60, 60);
                border: 3px solid rgb(30, 30, 30);    
            }
            QPushButton#completed_task_open_button {
                background-color: transparent;
            }
            QWidget {
                background-color: rgb(235, 235, 235);
            }
            QScrollArea {
                background-color: rgb(235, 235, 235);
                border: none;
            }
            QScrollBar:vertical {
                background: rgb(181, 181, 181);
                width: 15px;
                margin: 15px 3px 15px 3px;
                border: none;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background: rgb(90, 90, 90);
                min-height: 5px;
                border-radius: 4px;
            }
            QScrollBar::add-line, QScrollBar::sub-line,
            QScrollBar::up-arrow, QScrollBar::down-arrow,
            QScrollBar::add-page, QScrollBar::sub-page {
                background: none;
                border: none;
                height: 0px;
            }
            QMainWindow {
                background-color: rgb(235, 235, 235);
            }
            QMenu {
                background-color: rgb(79, 79, 75);
            }
            QInputDialog {
                font-family: Helvetica;
                font-size: 16px;
                background-color: rgb(36, 36, 35);
            }
            QCheckBox {
                background-color: rgb(60, 60, 60);
                border: 3px solid rgb(30, 30, 30);   
                font-family: Helvetica;
                font-size: 18px;
                color: rgb(235, 235, 235);
                padding: 10px;       
            }
            QCheckBox::indicator {
                border-image: url(assets/MainWindow/CheckBox/full_white_checkbox_unchecked_icon.png);
                width: 30px;
                height: 30px;
                margin-right: 5px;
            }
            QCheckBox::indicator::checked {
                border-image: url(assets/MainWindow/CheckBox/full_white_checkbox_checked_icon.png);
            }
            QToolTip {
                font-family: Helvetica;
                background-color: rgb(60, 60, 60);
                color: rgb(235, 235, 235);
            }
        """)

    def apply_dark_theme(self):
        self.dark_theme = True

        for checkbox, task_data in self.checkbox_dict.items():
            checkbox.setChecked(False)

        # to Dark
            # icons
        self.tool_button.setIcon(QIcon("assets/MainWindow/white_menu_icon.png"))
        self.user_login_button.setIcon(QIcon("assets/MainWindow/white_user_icon.png"))
        self.add_task_plus_button.setIcon(QIcon("assets/MainWindow/gray_add_task_plus_button_v1_icon.png"))

        self.change_checkboxes_button_icons_theme()
        self.change_completed_task_button_icon()

        if self.completed_task_opened:
            self.completed_task_open_button.setIcon(QIcon("assets/MainWindow/white_open_completed_task_section_icon.png"))
        else:
            self.completed_task_open_button.setIcon(QIcon("assets/MainWindow/white_closed_completed_task_section_icon.png"))

        for checkbox, data in self.checkbox_dict.items():
            for button in data["buttons"]:
                button.setStyleSheet(
                    "background-color: rgb(246, 246, 246);"
                    "border-top: 3px solid rgb(222, 222, 222);"
                    "border-bottom: 3px solid rgb(222, 222, 222);"
                    "border-right: 3px solid rgb(222, 222, 222);")

            # widgets
        self.setStyleSheet("""
            QLabel {
                font-family: Helvetica;
                color: rgb(235,235,235);
            }
            QLabel#title_label {
                font-size: 40px;
                font: bold;
                background-color: rgb(18, 18, 18);
                border-bottom: 2px solid rgb(41, 41, 39);
            }
            QLabel#title_tasks_label {
                font-size: 36px;
                font: bold;
            }
            QLabel#status_label {
                font-size: 14px;
                color: rgb(235,235,235);
                background-color: rgb(110, 110, 110); 
            }
            QToolButton#tool_button, QPushButton#user_login_button {
                background-color: rgb(18, 18, 18);
                border-radius: 0px;
                border-bottom: 2px solid rgb(41, 41, 39);
            }
            QPushButton {
                font-family: Helvetica;
                font-size: 18px;
                font: bold;
                color: white;
                background-color: rgb(18, 18, 18) ;
                padding: 15px;
            }
            QPushButton#add_task_button, QPushButton#del_tasks_button, 
            QPushButton#change_theme_button, QPushButton#about_button {
                color: rgb(225, 225, 220);
                background-color: rgb(79, 79, 75);
            }
            QPushButton#add_task_button:hover, QPushButton#del_tasks_button:hover, 
            QPushButton#change_theme_button:hover, QPushButton#about_button:hover {
                border: 2px solid rgb(140, 140, 140);
            }
            QPushButton#add_task_plus_button {
                background-color: rgb(246, 246, 246);
                border: 3px solid rgb(222, 222, 222);      
            }
            QPushButton#completed_task_open_button {
                background-color: transparent;
            }
            QPushButton:pressed {
                padding-left: 13px;
                padding-top: 7px;
                padding-right: 11px;
                padding-bottom: 5px;
            }         
            QWidget {
                background-color: rgb(44, 44, 44);
            }
            QScrollArea {
                background-color: rgb(44, 44, 44);
                border: none;
            }
            QScrollBar:vertical {
                background: rgb(18, 18, 18);
                width: 15px;
                margin: 15px 3px 15px 3px;
                border: none;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background: rgb(90, 90, 90);
                min-height: 5px;
                border-radius: 4px;
            }
            QScrollBar::add-line, QScrollBar::sub-line,
            QScrollBar::up-arrow, QScrollBar::down-arrow,
            QScrollBar::add-page, QScrollBar::sub-page {
                background: none;
                border: none;
                height: 0px;
            }
            QMainWindow {
                background-color: rgb(44, 44, 44);
            }
            QMenu {
                background-color: rgb(79, 79, 75);
            }
            QInputDialog {
                font-family: Helvetica;
                font-size: 16px;
                background-color: rgb(36, 36, 35);
            }
            QCheckBox {
                background-color: rgb(246, 246, 246);
                border: 3px solid rgb(222, 222, 222);
                font-family: Helvetica;
                font-size: 18px;
                color: rgb(44, 44, 44);
                padding: 10px;       
            }
            QCheckBox::indicator {
                border-image: url(assets/MainWindow/CheckBox/full_gray_checkbox_unchecked_icon.png);
                width: 30px;
                height: 30px;
                margin-right: 5px;
            }
            QCheckBox::indicator::checked {
                border-image: url(assets/MainWindow/CheckBox/full_gray_checkbox_checked_icon.png);
            }
            QToolTip {
                font-family: Helvetica;
                background-color: rgb(246, 246, 246);
                color: rgb(44, 44, 44);
            }
        """)

    def is_completed_checkbox_dict_empty(self):
        if not self.completed_checkbox_dict:
            return True
        else:
            return False

    def is_button_in_layout(self, layout, button):
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if isinstance(item.widget(), QPushButton) and item.widget() == button:
                return True
        return False

    def add_completed_tasks_button_into_layout(self):
        self.tasks_layout.addWidget(self.completed_task_open_button, alignment=Qt.AlignCenter)
        self.update()

    def delete_completed_tasks_button(self):
        self.tasks_layout.removeWidget(self.completed_task_open_button)
        self.completed_task_open_button.setParent(None)
        self.update()

    def show_completed_tasks_checkboxes(self):
        self.clear_layout(self.completed_task_layout)

        for checkbox, data in self.completed_checkbox_dict.items():
            checkbox_layout = QHBoxLayout()
            checkbox_layout.setContentsMargins(0, 0, 0, 0)
            checkbox_layout.setSpacing(0)

            checked_checkbox_copy = QCheckBox(data["name"])
            checked_checkbox_copy.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

            checkbox_layout.addSpacing(50)
            checkbox_layout.addWidget(checked_checkbox_copy)
            checkbox_layout.addSpacing(50)

            self.completed_task_layout.addLayout(checkbox_layout)
            self.completed_task_layout.addSpacing(30)

            self.tasks_layout.addLayout(self.completed_task_layout)
            self.update()

    # Methods written by AI for delete (hide) completed checkboxes
    def delete_completed_tasks_checkboxes(self):
        """Удаляет все элементы из макета completed_task_layout, отключая их от родительского виджета."""
        while self.completed_task_layout.count():
            item = self.completed_task_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                # Отключаем виджет от родителя, чтобы он исчез из UI
                widget.setParent(None)
            elif item.layout() is not None:
                # Рекурсивно очищаем вложенные макеты
                self._delete_layout_recursively(item.layout())

    def _delete_layout_recursively(self, layout):
        """Рекурсивно удаляет все элементы из вложенного макета, устанавливая родителя виджетов в None."""
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            elif item.layout() is not None:
                self._delete_layout_recursively(item.layout())
    # ------------------------------------------------------------------

    # onclick methods
        # Tool menu button methods
    def on_click_task_button(self):
        sender = self.sender()

        match sender.objectName():
            case "add_task_button" | "add_task_plus_button":
                add_task_dialog_box = TaskDialogBox()
                add_task_dialog_box.compare_with_main_win_theme(self.dark_theme)

                if add_task_dialog_box.exec_():
                    user_task_name, user_task_deadline, user_task_description = add_task_dialog_box.get_task_data()

                    self.create_task_checkbox_with_buttons(user_task_name, user_task_deadline, user_task_description)
                    self.show_all_task_checkboxes()
            case "del_tasks_button":
                if self.checkbox_dict:
                    delete_confirmation_dialog = self.create_and_setup_delete_confirmation_dialog()

                    user_reply = delete_confirmation_dialog.exec_()

                    if user_reply == QMessageBox.Yes:
                        for checkbox in list(self.checkbox_dict.keys()):
                            self.delete_task_checkbox_with_buttons(checkbox)
                        self.current_task_info_window = None

                    self.show_all_task_checkboxes()

    def on_click_change_theme_button(self):
        self.changeTheme()

    def on_click_about_button(self):
        about_app_dialog = self.create_and_setup_about_app_dialog()
        about_app_dialog.exec_()

        # Set checkbox checked method

    ####
    def on_click_task_checkbox(self):
        sender = self.sender()

        match sender.isChecked():
            case True:
                self.task_checkbox_set_style_sheet(sender, True)

                for checkbox, data in self.checkbox_dict.items():
                    if checkbox == sender:
                        self.completed_checkbox_dict[checkbox] = data

                is_completed_checkbox_button_in_layout = self.is_button_in_layout(self.tasks_layout, self.completed_task_open_button)
                if not is_completed_checkbox_button_in_layout:
                    self.add_completed_tasks_button_into_layout()

            case False:
                self.task_checkbox_set_style_sheet(sender, False)

                for checkbox in list(self.completed_checkbox_dict.keys()):
                    if checkbox == sender:
                        del self.completed_checkbox_dict[checkbox]
                self.show_completed_tasks_checkboxes()

                is_empty = self.is_completed_checkbox_dict_empty()
                if is_empty:
                    self.delete_completed_tasks_button()
                    self.delete_completed_tasks_checkboxes()
                    self.completed_task_opened = False
                    self.change_completed_task_button_icon()

        # Set checkbox buttons methods
    def on_click_task_info_checkbox_button(self):
        sender = self.sender()
        sender_checkbox = self.find_checkbox_by_checkbox_button(sender)

        self.create_task_info_messagebox_checkbox_button(sender_checkbox)

    def on_click_edit_task_checkbox_button(self):
        sender = self.sender()
        sender_checkbox = self.find_checkbox_by_checkbox_button(sender)

        # Get primary checkbox data
        sender_checkbox_task_name = self.checkbox_dict[sender_checkbox]["name"]
        sender_checkbox_task_deadline = self.checkbox_dict[sender_checkbox]["deadline"]
        sender_checkbox_task_description = self.checkbox_dict[sender_checkbox]["description"]

        self.create_and_open_edit_task_dialog(sender_checkbox, sender_checkbox_task_name,
                                              sender_checkbox_task_deadline, sender_checkbox_task_description)

    def on_click_delete_task_checkbox_button(self):
        sender = self.sender()
        sender_checkbox = self.find_checkbox_by_checkbox_button(sender)

        self.delete_task_checkbox_with_buttons(sender_checkbox)
        self.show_all_task_checkboxes()

    def on_click_reorder_button(self):
        sender = self.sender()
        sender_checkbox = self.find_checkbox_by_checkbox_button(sender)

        for data in self.checkbox_dict.values():
            if data["reorder_buttons"][0] is sender:
                self.move_up_down_checkbox(sender_checkbox, "up")
            elif data["reorder_buttons"][1] is sender:
                self.move_up_down_checkbox(sender_checkbox, "down")

    def on_click_completed_tasks_button(self):

        if self.completed_task_opened:
            self.completed_task_opened = False
            self.delete_completed_tasks_checkboxes()
        else:
            self.completed_task_opened = True
            self.show_completed_tasks_checkboxes()

        self.change_completed_task_button_icon()