import time
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from add_task_dialog import AddTaskDialog


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.tasks = []

        self.title_label = QLabel("To Do List", self)
        self.title_tasks_label = QLabel("Tasks", self)
        self.status_label = QLabel(time.strftime("%B %d, %Y"), self)

        self.user_login_button = QPushButton(self)
        self.add_task_button = QPushButton("ADD TASK", self)
        self.del_task_button = QPushButton("DELETE TASK", self)
        self.change_theme_button = QPushButton("CHANGE THEME", self)
        self.about_button = QPushButton("ABOUT APP", self)

        self.menu = QMenu(self)
        self.menu_buttons = [self.add_task_button, self.del_task_button, self.change_theme_button, self.about_button]

        self.tool_button = QToolButton(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("To Do List")
        self.setWindowIcon(QIcon("assets/todolist_icon.png"))
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
        self.user_login_button.setIcon(QIcon("assets/white_user_icon.png"))
        self.user_login_button.setIconSize(QSize(50, 50))
        self.user_login_button.resize(100,100)
        self.user_login_button.move(700,0)

        # PushButtons connections
        self.add_task_button.clicked.connect(self.on_click_task_button)
        self.del_task_button.clicked.connect(self.on_click_task_button)
        self.change_theme_button.clicked.connect(self.on_click_change_theme_button)
        self.about_button.clicked.connect(self.on_click_about_button)

        # Add action widgets into menu
        for button in self.menu_buttons:
            action = QWidgetAction(self)
            action.setDefaultWidget(button)
            self.menu.addAction(action)

        # Tool Menu Button
        self.tool_button.setIcon(QIcon("assets/white_menu_icon.png"))
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
            QCheckBox {
                background-color: rgb(246, 246, 246);
                font-family: Helvetica;
                font-size: 18px;
                border: 3px solid rgb(222, 222, 222);
                color: rgb(0, 0, 0);
                padding: 0 10px;       
            }
            QInputDialog {
                font-family: Helvetica;
                font-size: 16px;
                background-color: rgb(36, 36, 35);
            }
        """)

        self.show()

    # checkbox methods
    def create_and_setup_checkbox(self, task_dialog_box):
        user_task_name, user_task_deadline, user_task_description = task_dialog_box.get_task_data()
        task_checkbox = QCheckBox(f"{user_task_name} | {user_task_description} ||| {user_task_deadline}", self)
        task_checkbox.stateChanged.connect(self.on_click_task_checkbox)
        self.tasks.append(task_checkbox)

        task_checkbox.setFixedWidth(700)
        task_checkbox.setFixedHeight(50)

    def show_checkboxes(self):
        x, y = 50, 200
        for task_checkbox in self.tasks:
            task_checkbox.move(x, y)
            y += 80
            task_checkbox.show()

    def checkbox_set_style_sheet(self, sender, checked):
        if checked:
            sender.setStyleSheet(
                "background-color: rgb(93, 217, 110);"
                "font-family: Helvetica;"
                "font-size: 18px;"
                "border: 3px solid;"
                "border-color: rgb(66, 135, 76);"
                "color: rgb(0,0,0);")
        else:
            sender.setStyleSheet(
                "background-color: rgb(246, 246, 246);"
                "font-family: Helvetica;"
                "font-size: 18px;"
                "border: 3px solid rgb(222, 222, 222);"
                "color: rgb(0, 0, 0);"
                "padding: 0 10px;  "
            )


    # onclick methods
    def on_click_task_button(self):
        sender = self.sender()

        match sender.text():
            case "ADD TASK":
                add_task_dialog_box = AddTaskDialog()

                if add_task_dialog_box.exec_():
                    self.create_and_setup_checkbox(add_task_dialog_box)
                    self.show_checkboxes()
            case "DELETE TASK":
                print("DELETE TASK")

    def on_click_change_theme_button(self):
        print("CHANGE THEME")
        pass

    def on_click_about_button(self):
        print("ABOUT APP")
        pass

    def on_click_task_checkbox(self):
        sender = self.sender()

        match sender.isChecked():
            case True:
                print("123")
                self.checkbox_set_style_sheet(sender, True)
            case False:
                print("456")
                self.checkbox_set_style_sheet(sender, False)
        print("TASK CHECKBOX")
        pass

    # other methods
    def setup_dialog_box(self, dialog_title, dialog_text):
        text, ok = QInputDialog.getText(self, dialog_title, dialog_text)
        return text, ok