from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ChangeVisualUI:

    def __init__(self, main_window):
        self.main_window = main_window


    def change_UI_theme(self):
        if self.main_window.dark_theme:
            self.apply_light_theme()
        else:
            self.apply_dark_theme()


    def task_checkbox_set_style_sheet(self, sender, checked):
        if checked:
            sender.setStyleSheet(
                "background-color: rgb(93, 217, 110);"
                "border-color: rgb(66, 135, 76);")
        else:
            if self.main_window.dark_theme:
                sender.setStyleSheet(
                    "background-color: rgb(246, 246, 246);"
                    "border: 3px solid rgb(222, 222, 222);")
            else:
                sender.setStyleSheet(
                    "background-color: rgb(60, 60, 60);"
                    "border: 3px solid rgb(30, 30, 30);")


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

        for dictionary in self.main_window.dicts:
            if self.main_window.dark_theme:
                for task_data in dictionary.values():
                    i = 0
                    for reorder_button in task_data["reorder_buttons"]:
                        reorder_button.setIcon(QIcon(white_reorder_buttons_path[i]))
                        i += 1
                    i = 0
                    for checkbox_button in task_data["buttons"]:
                        checkbox_button.setIcon(QIcon(gray_checkbox_buttons_path[i]))
                        i += 1
            else:
                for task_data in dictionary.values():
                    i = 0
                    for reorder_button in task_data["reorder_buttons"]:
                        reorder_button.setIcon(QIcon(gray_reorder_buttons_path[i]))
                        i += 1
                    i = 0
                    for checkbox_button in task_data["buttons"]:
                        checkbox_button.setIcon(QIcon(white_checkbox_buttons_path[i]))
                        i += 1


    def change_completed_task_button_icon(self):
        if self.main_window.dark_theme:
            if self.main_window.completed_task_opened:
                self.main_window.completed_task_open_button.setIcon(
                    QIcon("assets/MainWindow/white_open_completed_task_section_icon.png"))
            else:
                self.main_window.completed_task_open_button.setIcon(
                    QIcon("assets/MainWindow/white_closed_completed_task_section_icon.png"))
        else:
            if self.main_window.completed_task_opened:
                self.main_window.completed_task_open_button.setIcon(QIcon("assets/MainWindow/gray_open_completed_task_section_icon.png"))
            else:
                self.main_window.completed_task_open_button.setIcon(QIcon("assets/MainWindow/gray_closed_completed_task_section_icon.png"))


    def apply_light_theme(self):
        self.main_window.dark_theme = False
        self.main_window.change_theme_button.setIcon(QIcon("assets/MainWindow/ToolMenu/light_theme_icon.png"))

        for checkbox, task_data in self.main_window.checkbox_dict.items():
            checkbox.setChecked(False)

        # to White
            # icons
        self.main_window.tool_button.setIcon(QIcon("assets/MainWindow/gray_menu_icon.png"))
        self.main_window.user_login_button.setIcon(QIcon("assets/MainWindow/gray_user_icon.png"))
        self.main_window.add_task_plus_button.setIcon(QIcon("assets/MainWindow/white_add_task_plus_button_v1_icon.png"))

        self.change_checkboxes_button_icons_theme()
        self.change_completed_task_button_icon()

        for dictionary in self.main_window.dicts:
            for data in dictionary.values():
                for button in data["buttons"]:
                    button.setStyleSheet(
                        "background-color: rgb(60, 60, 60);"
                        "border-top: rgb(30, 30, 30);"
                        "border-bottom: 3px solid rgb(30, 30, 30);"
                        "border-right: 3px solid rgb(30, 30, 30);")

            # widgets
        self.main_window.setStyleSheet("""
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
        self.main_window.dark_theme = True
        self.main_window.change_theme_button.setIcon(QIcon("assets/MainWindow/ToolMenu/dark_theme_icon.png"))

        for checkbox, task_data in self.main_window.checkbox_dict.items():
            checkbox.setChecked(False)

        # to Dark
            # icons
        self.main_window.tool_button.setIcon(QIcon("assets/MainWindow/white_menu_icon.png"))
        self.main_window.user_login_button.setIcon(QIcon("assets/MainWindow/white_user_icon.png"))
        self.main_window.add_task_plus_button.setIcon(QIcon("assets/MainWindow/gray_add_task_plus_button_v1_icon.png"))

        self.change_checkboxes_button_icons_theme()
        self.change_completed_task_button_icon()

        if self.main_window.completed_task_opened:
            self.main_window.completed_task_open_button.setIcon(QIcon("assets/MainWindow/white_open_completed_task_section_icon.png"))
        else:
            self.main_window.completed_task_open_button.setIcon(QIcon("assets/MainWindow/white_closed_completed_task_section_icon.png"))

        for dictionary in self.main_window.dicts:
            for data in dictionary.values():
                for button in data["buttons"]:
                    button.setStyleSheet(
                        "background-color: rgb(246, 246, 246);"
                        "border-top: 3px solid rgb(222, 222, 222);"
                        "border-bottom: 3px solid rgb(222, 222, 222);"
                        "border-right: 3px solid rgb(222, 222, 222);")

            # widgets
        self.main_window.setStyleSheet("""
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


    def set_default_widget_style(self, widget):
        if isinstance(widget, QCheckBox):
            if self.main_window.dark_theme:
                widget.setStyleSheet(
                    "background-color: rgb(246, 246, 246);"
                    "border: 3px solid rgb(222, 222, 222);")
            else:
                widget.setStyleSheet(
                    "background-color: rgb(60, 60, 60);"
                    "border: 3px solid rgb(30, 30, 30);")
        elif isinstance(widget, QPushButton):
            if self.main_window.dark_theme:
                widget.setStyleSheet(
                    "background-color: rgb(246, 246, 246);"
                    "border-top: 3px solid rgb(222, 222, 222);"
                    "border-bottom: 3px solid rgb(222, 222, 222);"
                    "border-right: 3px solid rgb(222, 222, 222);")
            else:
                widget.setStyleSheet(
                    "background-color: rgb(60, 60, 60);"
                    "border-top: 3px solid rgb(30, 30, 30);"
                    "border-bottom: 3px solid rgb(30, 30, 30);"
                    "border-right: 3px solid rgb(30, 30, 30);")
        elif isinstance(widget, QMessageBox):
            widget.setStyleSheet("""
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