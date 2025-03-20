import time
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from add_task_dialog import AddTaskDialog


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.tasks = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle("To Do List")
        self.setWindowIcon(QIcon("assets/todolist_icon.png"))
        self.setGeometry(900, 400, 800, 700)

        # TOP Label
        title_label = QLabel("To Do List", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.resize(800, 100)
        title_label.move(0,0)

        # Status bar (label)
        status_label = QLabel(time.strftime("%B %d, %Y"), self)
        status_label.setAlignment(Qt.AlignCenter)
        status_label.resize(800,25)
        status_label.move(0, 675)

        # User Log In PushButton
        user_login_button = QPushButton(self)
        user_login_button.setIcon(QIcon("assets/white_user_icon.png"))
        user_login_button.setIconSize(QSize(50, 50))
        user_login_button.resize(100,100)
        user_login_button.move(700,0)

        # PushButtons and their connections
        add_task_button = QPushButton("ADD TASK", self)
        del_task_button = QPushButton("DELETE TASK", self)
        change_theme_button = QPushButton("CHANGE THEME", self)
        about_button = QPushButton("ABOUT APP", self)

        add_task_button.clicked.connect(self.on_click_task_button)
        del_task_button.clicked.connect(self.on_click_task_button)
        change_theme_button.clicked.connect(self.on_click_change_theme_button)
        about_button.clicked.connect(self.on_click_about_button)


        # Create Menu and add action widgets
        menu = QMenu(self)
        menu_buttons = [add_task_button, del_task_button, change_theme_button, about_button]

        for button in menu_buttons:
            action = QWidgetAction(self)
            action.setDefaultWidget(button)
            menu.addAction(action)

        # Tool Menu Button
        tool_button = QToolButton(self)
        tool_button.setIcon(QIcon("assets/white_menu_icon.png"))
        tool_button.setIconSize(QSize(50, 50))
        tool_button.setPopupMode(QToolButton.InstantPopup)
        tool_button.setMenu(menu)
        tool_button.resize(100, 100)
        tool_button.move(0,0)



        # Create object name before styling
        title_label.setObjectName("title_label")
        status_label.setObjectName("status_label")
        user_login_button.setObjectName("user_login_button")

        tool_button.setObjectName("tool_button")



        self.setStyleSheet("""
                    QLabel#title_label {
                        font-family: Helvetica;
                        font-size: 40px;
                        font: bold;
                        color: white;
                        background-color: rgb(18, 18, 17);
                    }
                    QLabel#status_label {
                        font-family: Helvetica;
                        font-size: 14px;
                        color: white;
                        background-color: rgb(110, 110, 109); 
                    }
                    QLabel#user_login_button {
                        background-color: transparent;
                        border-radius: 0px;
                    }
                    QPushButton {
                        font-family: Helvetica;
                        font-size: 16px;
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
                    QToolButton#tool_button {
                        background-color: transparent;
                        border-radius: 0px;
                    }
                    QCheckBox {
                        font-family: Helvetica;
                        font-size: 16px;
                        color: black;
                        background-color: rgb(0, 0, 0);                      
                    }
                    QInputDialog {
                        font-family: Helvetica;
                        font-size: 16px;
                        background-color: rgb(36, 36, 35);
                    }
                """)


        self.show()




    def on_click_task_button(self):
        sender = self.sender()

        if sender.text() == "ADD TASK":
            print("ADD TASK")

            add_task_dialog = AddTaskDialog()

            if add_task_dialog.exec_():
                user_task_name, user_task_deadline, user_task_description = add_task_dialog.get_task_data()

                task_checkbox = QCheckBox(f"{user_task_name} | {user_task_description} ||| {user_task_deadline}",self)
                self.tasks.append(task_checkbox)
                task_checkbox.move(50, 200)
                task_checkbox.show()

        elif sender.text() == "DELETE TASK":
            print("DELETE TASK")
            text, ok = self.setup_dialog_box("Delete Task", "Enter the task:")
            if ok:
                pass

    def setup_dialog_box(self, dialog_title, dialog_text):
        text, ok = QInputDialog.getText(self, dialog_title, dialog_text)
        return text, ok




    def on_click_change_theme_button(self):
        print("CHANGE THEME")
        pass

    def on_click_about_button(self):
        print("ABOUT APP")
        pass