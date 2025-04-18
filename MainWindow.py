from ComponentBuilderUI import ComponentBuilderUI
from ChangeVisualUI import ChangeVisualUI
from TaskDialogBox import TaskDialogBox
from collections import OrderedDict
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.visual_changer = ChangeVisualUI(self)
        self.component_builder = ComponentBuilderUI(self)

        self.checkbox_dict = {}
        self.completed_checkbox_dict = {}
        self.dicts = [self.checkbox_dict, self.completed_checkbox_dict]

        self.current_task_info_window = None
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

        self.status_timer = QTimer(self)
        self.refresh_task_timer = QTimer(self)

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

        self.visual_changer.change_UI_theme()
        self.show()


    def print_buttons(self):
        print(self.checkbox_dict)
        print(self.completed_checkbox_dict)


    def set_statusbar_over_all_widgets(self):
        self.status_label.raise_()


    def find_checkbox_by_checkbox_button(self, clicked_button):
        for dictionary in self.dicts:
            for checkbox, data in dictionary.items():
                if clicked_button in data["buttons"] or clicked_button in data["reorder_buttons"]:
                    return checkbox


    def connect_checkbox_buttons(self):
        for dictionary in self.dicts:
            for checkbox, data in dictionary.items():
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


    def delete_task_checkbox_with_buttons(self, checkbox_sender, *dicts):
        for dictionary in dicts:
            if checkbox_sender in dictionary:
                checkbox_data = dictionary[checkbox_sender]

                checkbox_buttons = checkbox_data["buttons"]
                reorder_buttons = checkbox_data["reorder_buttons"]

                for button in checkbox_buttons[:]:
                    button.setParent(None)
                    button.deleteLater()
                for reorder_button in reorder_buttons[:]:
                    reorder_button.setParent(None)
                    reorder_button.deleteLater()

                checkbox_sender.setParent(None)
                checkbox_sender.deleteLater()

                del dictionary[checkbox_sender]
                break


    def clear_layout(self, layout):
        reversed_layout = reversed(range(layout.count()))
        for i in reversed_layout:
            item = layout.itemAt(i).widget()
            layout.removeItem(item)


    def show_all_task_checkboxes(self):
        self.clear_layout(self.tasks_layout)

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

            data["checkbox_layout"] = checkbox_layout

            self.tasks_layout.addLayout(checkbox_layout)

        # (+) button layout
        plus_button_layout = QHBoxLayout()

        plus_button_layout.addSpacing(50)
        plus_button_layout.addWidget(self.add_task_plus_button, alignment=Qt.AlignLeft)
        plus_button_layout.addStretch()

        self.add_task_plus_button.setFixedSize(50, 50)
        self.tasks_layout.addLayout(plus_button_layout)

        # test
        completed_tasks_button_layout = QHBoxLayout()

        completed_tasks_button_layout.addSpacing(50)
        completed_tasks_button_layout.addWidget(self.completed_task_open_button, alignment=Qt.AlignCenter)
        completed_tasks_button_layout.addSpacing(50)

        self.completed_task_open_button.hide()

        if self.completed_checkbox_dict:
            self.completed_task_open_button.show()

        self.tasks_layout.addLayout(completed_tasks_button_layout)
        # ---

        self.set_statusbar_over_all_widgets()


    # Refresh realtime statusbar every sec
    def start_track_status_realtime(self):
        self.status_timer.start(1000)


    def refresh_status_realtime(self):
        current_time = QDateTime.currentDateTime()

        # Status bar realtime
        formatted_realtime = current_time.toString("MMMM dd, hh:mm")
        self.status_label.setText(formatted_realtime)


    # Refresh deadline every min
    def start_track_task_deadline(self):
        self.refresh_task_timer.start(60000)


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
                self.visual_changer.set_default_widget_style(checkbox)


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


    def delete_completed_tasks_button(self):
        self.tasks_layout.removeWidget(self.completed_task_open_button)
        self.completed_task_open_button.setParent(None)
        self.update()


    def move_task_to_another_dict(self, completed_task_checkbox, from_dict, to_dict):
        completed_task_checkbox_data = from_dict.pop(completed_task_checkbox)
        to_dict[completed_task_checkbox] = completed_task_checkbox_data


    def show_completed_tasks(self):
        for checkbox, data in self.completed_checkbox_dict.items():

            if "checkbox_layout" in data:
                continue

            checkbox_layout = QHBoxLayout()
            checkbox_layout.setContentsMargins(0, 0, 0, 0)
            checkbox_layout.setSpacing(0)

            checkbox_layout.addSpacing(50)

            checkbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            checkbox.show()
            checkbox_layout.addWidget(checkbox)

            for reorder_button in data["reorder_buttons"]:
                reorder_button.hide()

            for button in data["buttons"]:
                button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                button.show()
                checkbox_layout.addWidget(button)

            checkbox_layout.addSpacing(50)

            data["checkbox_layout"] = checkbox_layout

            self.tasks_layout.addLayout(checkbox_layout)


    def delete_completed_tasks_from_ui(self):
        for checkbox, data in self.completed_checkbox_dict.items():
            layout = data.get("checkbox_layout")
            if layout:
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.hide()

                self.tasks_layout.removeItem(layout)
                del  data["checkbox_layout"]


    def remove_completed_task_from_ui(self, sender_checkbox):
        for checkbox, data in self.completed_checkbox_dict.items():
            if checkbox is sender_checkbox:
                checkbox_layout = data.get("checkbox_layout")
                if checkbox_layout:
                    while checkbox_layout.count():
                        item = checkbox_layout.takeAt(0)
                        widget = item.widget()
                        if widget:
                            widget.hide()

                for reorder_button in data["reorder_buttons"]:
                    reorder_button.hide()

                self.tasks_layout.removeItem(checkbox_layout)
                del data["checkbox_layout"]

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
                    self.show_all_task_checkboxes()

                    if self.completed_task_opened:
                        self.delete_completed_tasks_from_ui()
                        self.show_completed_tasks()

            case "del_tasks_button":
                if self.checkbox_dict or self.completed_checkbox_dict:
                    delete_confirmation_dialog = self.component_builder.create_and_setup_delete_confirmation_dialog()

                    user_reply = delete_confirmation_dialog.exec_()

                    if user_reply == QMessageBox.Yes:
                        for dictionary in self.dicts:
                            if dictionary:
                                list_of_checkboxes = list(dictionary.keys())
                                for checkbox in list_of_checkboxes:
                                    self.delete_task_checkbox_with_buttons(checkbox,*self.dicts)
                        self.current_task_info_window = None

                    self.show_all_task_checkboxes()

                    if self.completed_task_opened:
                        self.delete_completed_tasks_from_ui()
                        self.show_completed_tasks()


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

                self.move_task_to_another_dict(sender_checkbox, self.checkbox_dict, self.completed_checkbox_dict)

                self.remove_completed_task_from_ui(sender_checkbox)

                if self.completed_task_opened:
                    self.show_all_task_checkboxes()

                    self.delete_completed_tasks_from_ui()
                    self.show_completed_tasks()

            case False:
                self.visual_changer.task_checkbox_set_style_sheet(sender_checkbox, False)

                self.move_task_to_another_dict(sender_checkbox, self.completed_checkbox_dict, self.checkbox_dict)

                if self.completed_task_opened:
                    self.show_all_task_checkboxes()
                    self.visual_changer.task_checkbox_set_style_sheet(sender_checkbox, False)

                    self.delete_completed_tasks_from_ui()
                    self.show_completed_tasks()


        # Set checkbox buttons methods
    def on_click_task_info_checkbox_button(self):
        sender = self.sender()
        sender_checkbox = self.find_checkbox_by_checkbox_button(sender)

        self.component_builder.create_task_info_messagebox_checkbox_button(sender_checkbox)


    def on_click_edit_task_checkbox_button(self):
        sender = self.sender()
        sender_checkbox = self.find_checkbox_by_checkbox_button(sender)

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
        sender_checkbox = self.find_checkbox_by_checkbox_button(sender)

        self.delete_task_checkbox_with_buttons(sender_checkbox, self.checkbox_dict, self.completed_checkbox_dict)

        self.show_all_task_checkboxes()

        if self.completed_task_opened:
            self.delete_completed_tasks_from_ui()
            self.show_completed_tasks()


    def on_click_reorder_button(self):
        sender = self.sender()
        sender_checkbox = self.find_checkbox_by_checkbox_button(sender)

        for data in self.checkbox_dict.values():
            if data["reorder_buttons"][0] is sender:
                self.move_up_down_checkbox(sender_checkbox, "up")
            elif data["reorder_buttons"][1] is sender:
                self.move_up_down_checkbox(sender_checkbox, "down")
            else:
                continue
            break


    def on_click_completed_tasks_button(self):
        self.show_all_task_checkboxes()

        if self.completed_task_opened:
            self.completed_task_opened = False
            self.delete_completed_tasks_from_ui()
        else:
            self.completed_task_opened = True
            self.show_completed_tasks()

        self.visual_changer.change_completed_task_button_icon()