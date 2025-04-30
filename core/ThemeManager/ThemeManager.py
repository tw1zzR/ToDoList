from core.ThemeManager.icons_path import reorder_icons, checkbox_icons
from PyQt5.QtGui import *

class ThemeManager:

    def __init__(self, main_window, task_windows):
        self.dark_theme = True

        self.main_window = main_window
        self.task_windows = task_windows

    def change_UI_theme(self):
        if self.dark_theme:
            self.apply_light_theme()
        else:
            self.apply_dark_theme()

    def apply_qss_config(self, window, filepath):
        with open(filepath, 'r') as file:
            window.setStyleSheet(file.read())

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

    # Set MW icons methods
    def change_checkboxes_button_icons_theme(self):
        for task_item in self.main_window.tasks_data.task_items:
            for btn, icon_path in zip(task_item.checkbox_buttons, checkbox_icons[self.dark_theme]):
                self.set_widget_icon(btn, icon_path)
            for btn, icon_path in zip(task_item.reorder_buttons, reorder_icons[self.dark_theme]):
                self.set_widget_icon(btn, icon_path)

    def change_completed_task_button_icon(self):
        theme_color = "white" if self.dark_theme else "gray"
        state = "open" if self.main_window.completed_task_opened else "closed"

        icon_path = f"assets/MainWindow/{theme_color}_{state}_completed_task_section_icon.png"
        self.set_widget_icon(self.main_window.completed_task_open_button, icon_path)

    def set_widget_icon(self, widget, icon_path):
        widget.setIcon(QIcon(icon_path))

    def change_checkbox_buttons_theme(self):
        for task_item in self.main_window.tasks_data.task_items:
            for button in task_item.checkbox_buttons:
                if self.dark_theme:
                    button.setStyleSheet(
                        "background-color: rgb(246, 246, 246);"
                        "border-top: 3px solid rgb(222, 222, 222);"
                        "border-bottom: 3px solid rgb(222, 222, 222);"
                        "border-right: 3px solid rgb(222, 222, 222);")
                else:
                    button.setStyleSheet(
                        "background-color: rgb(60, 60, 60);"
                        "border-top: rgb(30, 30, 30);"
                        "border-bottom: 3px solid rgb(30, 30, 30);"
                        "border-right: 3px solid rgb(30, 30, 30);")

    # Apply App Theme
    def apply_light_theme(self):
        self.dark_theme = False

        # to White
        self.set_widget_icon(self.main_window.change_theme_button, "assets/MainWindow/ToolMenu/light_theme_icon.png")
        self.set_widget_icon(self.main_window.tool_button, "assets/MainWindow/gray_menu_icon.png")
        self.set_widget_icon(self.main_window.user_login_button, "assets/MainWindow/gray_user_icon.png")
        self.set_widget_icon(self.main_window.add_task_plus_button, "assets/MainWindow/white_add_task_plus_button_v1_icon.png")

        self.change_checkboxes_button_icons_theme()
        self.change_completed_task_button_icon()

        self.change_checkbox_buttons_theme()

        self.apply_qss_config(self.main_window,
        "core/ThemeManager/theme_presets/mw_light.qss")

        for window in self.task_windows:
            self.apply_qss_config(window, "core/ThemeManager/theme_presets/tw_light.qss")

        for task_item in self.main_window.tasks_data.uncompleted_task_items:
            self.task_checkbox_set_style_sheet(task_item.checkbox, False)

    def apply_dark_theme(self):
        self.dark_theme = True

        # to Dark
        self.set_widget_icon(self.main_window.change_theme_button, "assets/MainWindow/ToolMenu/dark_theme_icon.png")
        self.set_widget_icon(self.main_window.tool_button, "assets/MainWindow/white_menu_icon.png")
        self.set_widget_icon(self.main_window.user_login_button, "assets/MainWindow/white_user_icon.png")
        self.set_widget_icon(self.main_window.add_task_plus_button,
                             "assets/MainWindow/gray_add_task_plus_button_v1_icon.png")

        self.change_checkboxes_button_icons_theme()
        self.change_completed_task_button_icon()

        self.change_checkbox_buttons_theme()

        self.apply_qss_config(self.main_window,
        "core/ThemeManager/theme_presets/mw_dark.qss")

        for window in self.task_windows:
            self.apply_qss_config(window, "core/ThemeManager/theme_presets/tw_dark.qss")

        for task_item in self.main_window.tasks_data.uncompleted_task_items:
            self.task_checkbox_set_style_sheet(task_item.checkbox, False)