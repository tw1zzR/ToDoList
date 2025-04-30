from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def clear_layout(layout):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()

        if widget is not None:
            widget.setParent(None)

def get_task_from_dialog(task_input_dialog):
    user_task_name = task_input_dialog.user_input_task_name.text()
    user_task_deadline = task_input_dialog.user_input_task_deadline.text()
    user_task_description = task_input_dialog.user_input_task_description.toPlainText()

    if user_task_name.strip():
        task_input_dialog.accept()

        return user_task_name, user_task_deadline, user_task_description
    else:
        empty_task_name_msgbox = create_messagebox("Task Error","Task name cannot be blank.",
                                                    QMessageBox.Warning,"assets/warning_icon_1.png")
        empty_task_name_msgbox.exec_()


def create_messagebox(title, message=None, icon=None, win_icon=None):
    warning_msgbox = QMessageBox()

    warning_msgbox.setWindowTitle(title)
    warning_msgbox.setWindowIcon(QIcon(win_icon))
    warning_msgbox.setTextFormat(Qt.RichText)
    warning_msgbox.setText(message)
    warning_msgbox.setIcon(icon)

    set_default_widget_style(warning_msgbox)

    return warning_msgbox

def set_default_widget_style(widget, window=None):
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