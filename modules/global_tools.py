from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


def is_valid_task_dialog_type(current_task_window, task_dialog_class, clicked_checkbox_name, task_window_checkbox_name):
    if (current_task_window is not None
            and current_task_window.isVisible()
            and isinstance(current_task_window, task_dialog_class)
            and clicked_checkbox_name == task_window_checkbox_name):
        return True
    else:
        return False

def open_task_dialog(current_task_dialog, new_task_dialog):
    if current_task_dialog is None or not current_task_dialog.isVisible():
        current_task_dialog = new_task_dialog
        current_task_dialog.show()
        return current_task_dialog
    else:
        current_task_dialog.raise_()
        current_task_dialog.activateWindow()


def set_app_theme(main_window_dark_theme):
    for window in QApplication.topLevelWidgets():
        if isinstance(window, (QMainWindow, QDialog)):
            compare_with_main_window_theme(window, main_window_dark_theme)
            window.update()

def compare_with_main_window_theme(window, main_window_dark_theme):
    if main_window_dark_theme:
        window.visual_changer.apply_dark_theme()
    else:
        window.visual_changer.apply_light_theme()

def create_warning_messagebox(window, title, message):
    warning_msgbox = QMessageBox()

    warning_msgbox.setWindowTitle(title)
    warning_msgbox.setWindowIcon(QIcon("assets/warning_icon_1.png"))
    warning_msgbox.setTextFormat(Qt.RichText)
    warning_msgbox.setText(message)
    warning_msgbox.setIcon(QMessageBox.Warning)

    set_default_widget_style(window, warning_msgbox)

    return warning_msgbox

def set_default_widget_style(window, widget):
    if isinstance(widget, QCheckBox):
        if window.dark_theme:
            widget.setStyleSheet(
                "background-color: rgb(246, 246, 246);"
                "border: 3px solid rgb(222, 222, 222);")
        else:
            widget.setStyleSheet(
                "background-color: rgb(60, 60, 60);"
                "border: 3px solid rgb(30, 30, 30);")
    elif isinstance(widget, QPushButton):
        if window.dark_theme:
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