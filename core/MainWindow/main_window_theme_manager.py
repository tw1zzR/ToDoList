from PyQt5.QtGui import *

class MainWindowThemeManager:

    def __init__(self, main_window):
        self.main_window = main_window
        self.task_items = self.main_window.tasks_data.task_items
        self.uncompleted_task_items = self.main_window.tasks_data.uncompleted_task_items

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
        reorder_icons = {
            True: ["assets/MainWindow/white_moveup_arrow_icon.png",
                   "assets/MainWindow/white_movedown_arrow_icon.png"],
            False: ["assets/MainWindow/gray_moveup_arrow_icon.png",
                    "assets/MainWindow/gray_movedown_arrow_icon.png"]
        }

        checkbox_icons = {
            True: ["assets/MainWindow/CheckBox/gray_task_info_button_V1_icon.png",
                   "assets/MainWindow/CheckBox/gray_edit_task_button_icon.png",
                   "assets/MainWindow/CheckBox/gray_delete_task_button_icon.png"],
            False: ["assets/MainWindow/CheckBox/white_task_info_button_V1_icon.png",
                    "assets/MainWindow/CheckBox/white_edit_task_button_icon.png",
                    "assets/MainWindow/CheckBox/white_delete_task_button_icon.png"]
        }

        theme = self.main_window.dark_theme

        for task_item in self.task_items:
            for btn, icon_path in zip(task_item.checkbox_buttons, checkbox_icons[theme]):
                self.set_widget_icon(btn, icon_path)
            for btn, icon_path in zip(task_item.reorder_buttons, reorder_icons[theme]):
                self.set_widget_icon(btn, icon_path)

    def change_completed_task_button_icon(self):
        theme_color = "white" if self.main_window.dark_theme else "gray"
        state = "open" if self.main_window.completed_task_opened else "closed"

        icon_path = f"assets/MainWindow/{theme_color}_{state}_completed_task_section_icon.png"
        self.set_widget_icon(self.main_window.completed_task_open_button, icon_path)

    def set_widget_icon(self, widget, icon_path):
        widget.setIcon(QIcon(icon_path))

    def apply_light_theme(self):
        self.main_window.dark_theme = False

        # to White
        self.set_widget_icon(self.main_window.change_theme_button, "assets/MainWindow/ToolMenu/light_theme_icon.png")
        self.set_widget_icon(self.main_window.tool_button, "assets/MainWindow/gray_menu_icon.png")
        self.set_widget_icon(self.main_window.user_login_button, "assets/MainWindow/gray_user_icon.png")
        self.set_widget_icon(self.main_window.add_task_plus_button, "assets/MainWindow/white_add_task_plus_button_v1_icon.png")

        self.change_checkboxes_button_icons_theme()
        self.change_completed_task_button_icon()

        for task_item in self.task_items:
            for button in task_item.checkbox_buttons:
                button.setStyleSheet(
                    "background-color: rgb(60, 60, 60);"
                    "border-top: rgb(30, 30, 30);"
                    "border-bottom: 3px solid rgb(30, 30, 30);"
                    "border-right: 3px solid rgb(30, 30, 30);")

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

        for task_item in self.uncompleted_task_items:
            self.task_checkbox_set_style_sheet(task_item.checkbox, False)

    def apply_dark_theme(self):
        self.main_window.dark_theme = True

        # to Dark
        self.set_widget_icon(self.main_window.change_theme_button, "assets/MainWindow/ToolMenu/dark_theme_icon.png")
        self.set_widget_icon(self.main_window.tool_button, "assets/MainWindow/white_menu_icon.png")
        self.set_widget_icon(self.main_window.user_login_button, "assets/MainWindow/white_user_icon.png")
        self.set_widget_icon(self.main_window.add_task_plus_button, "assets/MainWindow/gray_add_task_plus_button_v1_icon.png")

        self.change_checkboxes_button_icons_theme()
        self.change_completed_task_button_icon()

        for task_item in self.task_items:
            for button in task_item.checkbox_buttons:
                    button.setStyleSheet(
                        "background-color: rgb(246, 246, 246);"
                        "border-top: 3px solid rgb(222, 222, 222);"
                        "border-bottom: 3px solid rgb(222, 222, 222);"
                        "border-right: 3px solid rgb(222, 222, 222);")

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

        for task_item in self.uncompleted_task_items:
            self.task_checkbox_set_style_sheet(task_item.checkbox, False)