from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time

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
        status_label = QLabel(f"{time.strftime("%B %d, %Y")}", self)
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

        # DIALOG BOX | ADD DEL TASKS
        task_checkbox = QCheckBox("", self)

        qhbox = QHBoxLayout()
        qhbox.setGeometry(QtCore.QRect(70, 470, 280, 60))
        qhbox.setContentsMargins(0, 0, 0, 0)

            # Labels
        task_label = QLabel("Enter the task",self)
        task_label.setGeometry(70, 245, 160, 40)

        deadline_label = QLabel("Deadline", self)
        deadline_label.setGeometry(70, 140, 160, 40)

        task_name_label = QLabel("Task name", self)
        task_name_label.setGeometry(70, 35, 160, 40)

            # User Input
        user_input_task_name = QLineEdit(self)
        user_input_task_name.setGeometry(70, 70, 280, 50)

        user_input_task = QLineEdit(self)
        user_input_task.setGeometry(QtCore.QRect(70, 280, 280, 150))

        user_input_datetime = QDateTimeEdit(self)
        user_input_datetime.setGeometry(QtCore.QRect(70, 175, 280, 50))

            # Push Buttons
        OK_push_button = QPushButton("OK", self)
        qhbox.addWidget(OK_push_button)

        CANCEL_push_button = QPushButton("CANCEL", self)
        qhbox.addWidget(CANCEL_push_button)

        # Create object name before styling
        title_label.setObjectName("title_label")
        status_label.setObjectName("status_label")
        user_login_button.setObjectName("user_login_button")

        tool_button.setObjectName("tool_button")

        #dialog box
        task_label.setObjectName("task_label")
        deadline_label.setObjectName("deadline_label")
        task_name_label.setObjectName("task_name_label")

        user_input_task_name.setObjectName("user_input_task_name")
        user_input_task.setObjectName("user_input_task")
        user_input_datetime.setObjectName("user_input_datetime")

        qhbox.setObjectName("hbox_layout")

        OK_push_button.setObjectName("OK_push_button")
        CANCEL_push_button.setObjectName("CANCEL_push_button")

        

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
                    QLabel#task_name_label {
                        background-color: transparent;
                        font-family: Helvetica;
                        font-size: 20px;
                        font: bold;
                        color: rgb(0,0,0);
                    }
                    QLabel#deadline_label {
                        background-color: transparent;
                        font-family: Helvetica;
                        font-size: 20px;
                        font: bold;
                        color: rgb(0,0,0);
                    }
                    QLabel#task_label {
                        background-color: transparent;
                        font-family: Helvetica;
                        font-size: 20px;
                        font: bold;
                        color: rgb(0,0,0);
                    }
                    QLineEdit#user_input_task_name {
                        background-color: rgb(246, 246, 246);
                        font-family: Helvetica;
                        font-size: 18px;
                        border: 3px solid;
                        border-color: rgb(222, 222, 222);
                        font: bold;
                        color: rgb(0,0,0);
                        padding-left: 10px;
                    }
                    QLinedEdit#user_input_task {
                        background-color: rgb(246, 246, 246);
                        font-family: Helvetica;
                        font-size: 18px;
                        border: 3px solid;
                        border-color: rgb(222, 222, 222);
                        color: rgb(0,0,0);
                        padding-left: 10px;
                    }
                    QDateTimeEdit#user_input_datetime {
                        background-color: rgb(246, 246, 246);
                        font-family: Helvetica;
                        font-size: 18px;
                        border: 3px solid;
                        border-color: rgb(222, 222, 222);
                        color: rgb(0,0,0);
                        padding-left: 10px;
                    }
                    QPushButton {
                        font-family: Helvetica;
                        font-size: 16px;
                        font: bold;
                        color: white;
                        background-color: rgb(18, 18, 17);
                        padding: 15px;
                    }
                    QPushButton#OK_push_button {
                        background-color: rgb(93, 217, 110);
                        font-family: Helvetica;
                        font-size: 18px;
                        border: 3px solid;
                        border-color: rgb(66, 135, 76);
                        font: bold;
                        color: rgb(0,0,0);
                        width: 80px;
                        height: 50px;
                    }
                    QPushButton#CANCEL_push_button {
                        background-color: rgb(242, 155, 155);
                        font-family: Helvetica;
                        font-size: 18px;
                        border: 3px solid;
                        border-color: rgb(130, 57, 57);
                        font: bold;
                        color: rgb(0,0,0);
                        width: 80px;
                        height: 50px;
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
            text, ok = self.setup_dialog_box("Add Task", "Enter the task:")
            if ok:
                print("DIALOG BOX")
                # task_checkbox = QCheckBox(f"{text}", self)
                # self.tasks.append(task_checkbox)
                # task_checkbox.move(50, 200)
                # task_checkbox.show()
        elif sender.text() == "DELETE TASK":
            print("DELETE TASK")
            text, ok = self.setup_dialog_box("Delete Task", "Enter the task:")
            if ok:
                pass

    def on_click_change_theme_button(self):
        print("CHANGE THEME")
        pass

    def on_click_about_button(self):
        print("ABOUT APP")
        pass

    def setup_dialog_box(self, dialog_title, dialog_text):
        text, ok = QInputDialog.getText(self, dialog_title, dialog_text)
        return text, ok