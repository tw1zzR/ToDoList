import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("QMainWindow { background-color: rgb(36, 36, 35);}")
        self.initUI()

    def initUI(self):
        self.setWindowTitle("To Do List")
        self.setWindowIcon(QIcon("assets/todolist_icon.png"))
        self.setGeometry(900, 400, 800, 700)

        # TOP Label
        title_label = QLabel("To Do List", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.resize(800, 100)
        title_label.setFont(QFont("Helvetica", 40, QFont.Bold))
        title_label.setStyleSheet(""" 
            color: white;
            background-color: rgb(18, 18, 17);
        """)

        # PushButtons and their connections
        add_task_button = QPushButton("ADD TASK", self)
        del_task_button = QPushButton("DELETE TASK", self)
        change_theme_button = QPushButton("CHANGE THEME", self)
        about_button = QPushButton("ABOUT APP", self)

        add_task_button.clicked.connect(self.on_click_task_button)
        del_task_button.clicked.connect(self.on_click_task_button)
        change_theme_button.clicked.connect(self.on_click_change_theme_button)
        about_button.clicked.connect(self.on_click_about_button)

        self.setStyleSheet("""
            QPushButton {
                font-family: Helvetica;
                font-size: 16px;
                font: bold;
                color: white;
                background-color: rgb(18, 18, 17);
                padding: 15px;
            }
            QMainWindow {
                background-color: rgb(36, 36, 35)
                }
            QMenu {
                background-color: rgb(79, 79, 75)
            }
        """)

        # Create Menu and add action widgets
        menu = QMenu(self)
        menu_buttons = [add_task_button, del_task_button, change_theme_button, about_button]

        for button in menu_buttons:
            action = QWidgetAction(self)
            action.setDefaultWidget(button)
            menu.addAction(action)

        # Tool Menu Button
        tool_button = QToolButton(self)
        tool_button.resize(100, 100)
        tool_button.setIcon(QIcon("assets/white_menu_icon.png"))
        tool_button.setIconSize(QSize(50, 50))
        tool_button.setPopupMode(QToolButton.InstantPopup)
        tool_button.setMenu(menu)

        tool_button.setStyleSheet(""" 
                                    background-color: rgb(18, 18, 17);
                                    border-radius: 0px;
                                """)


        self.show()


    def on_click_task_button(self):
        sender = self.sender()
        if sender.text() == "ADD TASK":
            print("ADD TASK")
        elif sender.text() == "DELETE TASK":
            print("DELETE TASK")

    def on_click_change_theme_button(self):
        print("CHANGE THEME")
        pass

    def on_click_about_button(self):
        print("ABOUT APP")
        pass