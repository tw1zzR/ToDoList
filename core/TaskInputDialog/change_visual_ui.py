
class ChangeVisualUI:

    def __init__(self, task_input_dialog):
        self.task_input_dialog = task_input_dialog

    def change_UI_theme(self):
        if self.task_input_dialog.dark_theme:
            self.apply_light_theme()
        else:
            self.apply_dark_theme()

    def apply_light_theme(self):
        self.task_input_dialog.setStyleSheet("""
            QDialog {
                background-color: rgb(255, 255, 255);
            }
            QLabel {            
                font-family: Helvetica; 
                color: rgb(44,44,44);       
            }
            QLabel#task_name_label, QLabel#task_deadline_label, QLabel#task_description_label {
                background-color: transparent;
                font-family: Helvetica;
                font-size: 18px;
                font: bold;
            }
            QLineEdit#user_input_task_name, QDateTimeEdit#user_input_task_deadline, QTextEdit#user_input_task_description {
                background-color: rgb(60,60,60);
                font-family: Helvetica;
                font-size: 18px;
                border: 3px solid rgb(30,30,30);
                color: rgb(235,235,235);
            }
            QTextEdit#user_input_task_description, QLineEdit#user_input_task_name, QDateTimeEdit#user_input_task_deadline {
                padding-top: 5px;
                padding-left: 10px;
                padding-right: 10px;
            }
            QPushButton {
                font-family: Helvetica;
                font-size: 18px;
                border: 3px solid;
                font: bold;
                color: rgb(44, 44, 44);
                width: 80px;
                height: 50px;
            }
            QPushButton#send_button {
                background-color: rgb(93, 217, 110);
                border-color: rgb(66, 135, 76);
            }
            QPushButton#cancel_button {
                background-color: rgb(242, 155, 155);
                border-color: rgb(130, 57, 57);
            }
        """)

    def apply_dark_theme(self):
        self.task_input_dialog.setStyleSheet("""
            QDialog {
                background-color: rgb(44, 44, 44);
            }
            QLabel {            
                font-family: Helvetica; 
                color: rgb(235,235,235);       
            }
            QLabel#task_name_label, QLabel#task_deadline_label, QLabel#task_description_label {
                background-color: transparent;
                font-family: Helvetica;
                font-size: 18px;
                font: bold;
            }
            QLineEdit#user_input_task_name, QDateTimeEdit#user_input_task_deadline, QTextEdit#user_input_task_description {
                background-color: rgb(246, 246, 246);
                border: 3px solid rgb(222, 222, 222);
                font-family: Helvetica;
                font-size: 18px;
                color: rgb(44, 44, 44);          
            }
            QTextEdit#user_input_task_description, QLineEdit#user_input_task_name, QDateTimeEdit#user_input_task_deadline {
                padding-top: 5px;
                padding-left: 10px;
                padding-right: 10px;
            }
            QPushButton {
                font-family: Helvetica;
                font-size: 18px;
                border: 3px solid;
                font: bold;
                color: rgb(44, 44, 44);
                width: 80px;
                height: 50px;
            }
            QPushButton#send_button {
                background-color: rgb(93, 217, 110);
                border-color: rgb(66, 135, 76);
            }
            QPushButton#cancel_button {
                background-color: rgb(242, 155, 155);
                border-color: rgb(130, 57, 57);
            }
        """)