import time
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from AddTaskDialogBox import AddTaskDialog
from TaskInfoMessageBox import CustomTaskInfoMessageBox


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.checkbox_dict = {}

        self.title_label = QLabel("To Do List", self)
        self.title_tasks_label = QLabel("Tasks", self)
        self.status_label = QLabel(time.strftime("%B %d, %Y"), self)

        self.user_login_button = QPushButton(self)

        # ToolMenu PushButtons
        self.add_task_button = QPushButton("ADD TASK", self)
        self.del_task_button = QPushButton("DELETE TASK", self)
        self.change_theme_button = QPushButton("CHANGE THEME", self)
        self.about_button = QPushButton("ABOUT APP", self)

        # Menu
        self.menu = QMenu(self)
        self.menu_buttons = [self.add_task_button, self.del_task_button, self.change_theme_button, self.about_button]

        self.tool_button = QToolButton(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("To Do List")
        self.setWindowIcon(QIcon("assets/MainWindow/todolist_icon.png"))
        self.setGeometry(900, 400, 800, 700)

        # Title Labels
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.resize(800, 100)
        self.title_label.move(0,0)

        self.title_tasks_label.setAlignment(Qt.AlignCenter)
        self.title_tasks_label.resize(200, 100)
        self.title_tasks_label.move(300,100)

        # Status Label
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.resize(800,25)
        self.status_label.move(0, 675)

        # Login
        self.user_login_button.setIcon(QIcon("assets/MainWindow/white_user_icon.png"))
        self.user_login_button.setIconSize(QSize(50, 50))
        self.user_login_button.resize(100,100)
        self.user_login_button.move(700,0)

        # PushButtons connections
        self.add_task_button.clicked.connect(self.on_click_task_button)
        self.del_task_button.clicked.connect(self.on_click_task_button)
        self.change_theme_button.clicked.connect(self.on_click_change_theme_button)
        self.about_button.clicked.connect(self.on_click_about_button)

        self.user_login_button.clicked.connect(self.print_buttons)

        # Add action widgets into menu
        for button in self.menu_buttons:
            action = QWidgetAction(self)
            action.setDefaultWidget(button)
            self.menu.addAction(action)

        # Tool Menu Button
        self.tool_button.setIcon(QIcon("assets/MainWindow/white_menu_icon.png"))
        self.tool_button.setIconSize(QSize(50, 50))
        self.tool_button.setPopupMode(QToolButton.InstantPopup)
        self.tool_button.setMenu(self.menu)
        self.tool_button.resize(100, 100)
        self.tool_button.move(0,0)

        # Create object name before styling
        self.title_label.setObjectName("title_label")
        self.title_tasks_label.setObjectName("title_tasks_label")
        self.status_label.setObjectName("status_label")
        self.user_login_button.setObjectName("user_login_button")
        self.tool_button.setObjectName("tool_button")
        self.user_login_button.setObjectName("user_login_button")

        self.setStyleSheet("""
            QLabel {
                font-family: Helvetica;
                color: white;
            }
            QLabel#title_label {
                font-size: 40px;
                font: bold;
                background-color: rgb(18, 18, 17);
                border-bottom: 2px solid rgb(41, 41, 39);
            }
            QLabel#title_tasks_label {
                font-size: 36px;
                font: bold;
            }
            QLabel#status_label {
                font-size: 14px;
                background-color: rgb(110, 110, 109); 
            }
            QLabel#user_login_button, QToolButton#tool_button, QPushButton#user_login_button {
                background-color: transparent;
                border-radius: 0px;
            }
            QPushButton {
                font-family: Helvetica;
                font-size: 18px;
                font: bold;
                color: white;
                background-color: rgb(18, 18, 17);
                padding: 15px;
            }
            QMainWindow {
                background-color: rgb(36, 36, 35);
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
                font-family: Helvetica;
                font-size: 18px;
                border: 3px solid rgb(222, 222, 222);
                color: rgb(0, 0, 0);
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
        """)

        self.show()

    def print_buttons(self):
        print(self.checkbox_dict)

    # checkbox methods
    def create_task_checkbox_with_buttons(self, task_dialog_box):
        user_task_name, user_task_deadline, user_task_description = task_dialog_box.get_task_data()

        task_checkbox = QCheckBox(user_task_name, self)
        task_checkbox.stateChanged.connect(self.on_click_task_checkbox)
        task_checkbox.setFixedSize(650, 50)

        task_info_button = QPushButton(self)
        edit_task_button = QPushButton(self)
        delete_task_button = QPushButton(self)

        task_info_button.setIcon(QIcon("assets/MainWindow/CheckBox/gray_task_info_button_V1_icon.png"))
        edit_task_button.setIcon(QIcon("assets/MainWindow/CheckBox/gray_edit_task_button_icon.png"))
        delete_task_button.setIcon(QIcon("assets/MainWindow/CheckBox/gray_delete_task_button_icon.png"))

        buttons = [task_info_button, edit_task_button, delete_task_button]

        for button in buttons:
            button.resize(50, 50)
            button.setIconSize(QSize(30, 30))
            button.setStyleSheet(
                "background-color: transparent;"
                "border-radius: 0px;")

        # Add to data lists
        self.checkbox_dict[task_checkbox] = {
            "buttons": buttons,
            "name": user_task_name,
            "deadline": user_task_deadline,
            "description": user_task_description
        }

        self.connect_checkbox_buttons()

    def find_checkbox_by_button(self, clicked_button):
        for checkbox, data in self.checkbox_dict.items():
            if clicked_button in data["buttons"]:
                return checkbox
        return None

    def connect_checkbox_buttons(self):
        for checkbox, data in self.checkbox_dict.items():
            task_info_button  = data["buttons"][0]
            edit_task_button  = data["buttons"][1]
            delete_task_button = data["buttons"][2]

            task_info_button.clicked.connect(self.on_click_task_info_checkbox)

            edit_task_button.clicked.connect(lambda: print("456"))
            delete_task_button.clicked.connect(lambda: print("789"))

    def create_task_info_messagebox(self, checkbox_sender):
        self.task_info_messagebox = CustomTaskInfoMessageBox(self.checkbox_dict[checkbox_sender]["name"],
                                                        self.checkbox_dict[checkbox_sender]["deadline"],
                                                        self.checkbox_dict[checkbox_sender]["description"])
        self.task_info_messagebox.show()

    def show_task_checkbox(self):
        checkbox_x, button_x = 75, 560
        y = 200

        for checkbox, data in self.checkbox_dict.items():
            checkbox.move(checkbox_x, y)
            checkbox.show()

            for button in data["buttons"]:
                button.move(button_x, y)
                button_x += 50
                button.show()

            y += 80
            button_x = 560

    def task_checkbox_set_style_sheet(self, sender, checked):
        if checked:
            sender.setStyleSheet(
                "background-color: rgb(93, 217, 110);"
                "border-color: rgb(66, 135, 76);")
        else:
            sender.setStyleSheet(
                "background-color: rgb(246, 246, 246);"
                "border-color: rgb(222, 222, 222);")

    # onclick methods

        # Tool menu button methods
    def on_click_task_button(self):
        sender = self.sender()

        match sender.text():
            case "ADD TASK":
                add_task_dialog_box = AddTaskDialog()
                if add_task_dialog_box.exec_():
                    self.create_task_checkbox_with_buttons(add_task_dialog_box)
                    self.show_task_checkbox()
            case "DELETE TASK":
                print("DELETE TASK")

    def on_click_change_theme_button(self):
        print("CHANGE THEME")
        pass

    def on_click_about_button(self):
        print("ABOUT APP")
        pass

        # Set checkbox checked method
    def on_click_task_checkbox(self):
        sender = self.sender()

        match sender.isChecked():
            case True:
                self.task_checkbox_set_style_sheet(sender, True)
            case False:
                self.task_checkbox_set_style_sheet(sender, False)

    def on_click_task_info_checkbox(self):
        sender = self.sender()

        sender_checkbox = self.find_checkbox_by_button(sender)
        self.create_task_info_messagebox(sender_checkbox)