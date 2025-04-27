
class ChangeVisualUI:

    def __init__(self, task_info_dialog):
        self.task_info_dialog = task_info_dialog

    def change_UI_theme(self):
        pass

    def apply_light_theme(self):
        self.task_info_dialog.dark_theme = False

        self.task_info_dialog.setStyleSheet("""
            QDialog {
                background-color: rgb(255, 255, 255);
            }
            QLabel {            
                font-family: Helvetica; 
                color: rgb(255, 255, 255);       
            }
            QLabel#task_name_label, QLabel#task_deadline_label, QLabel#task_description_label {
                background-color: transparent;
                font-family: Helvetica;
                font-size: 18px;
                font: bold;
                color: rgb(44,44,44);
            }
            QLabel#user_input_task_name, QLabel#user_input_task_deadline, QTextEdit#user_input_task_description {
                background-color: rgb(60, 60, 60);
                border: 3px solid rgb(30, 30, 30);  
                font-family: Helvetica;
                font-size: 18px;
                color: rgb(235,235,235);
            }
            QTextEdit#user_input_task_description {
                padding-top: 5px;
                padding-left: 10px;
                padding-right: 10px;
            }
            QPushButton#OK_Button {
                background-color: rgb(93, 217, 110);
                font-family: Helvetica;
                font-size: 18px;
                border: 3px solid rgb(66, 135, 76);
                font: bold;
                color: rgb(44, 44, 44);
            }
        """)

    def apply_dark_theme(self):
        self.task_info_dialog.dark_theme = True

        self.task_info_dialog.setStyleSheet("""
            QDialog {
                background-color: rgb(44, 44, 44);
            }
            QLabel {            
                font-family: Helvetica; 
                color: rgb(0,0,0);       
            }
            QLabel#task_name_label, QLabel#task_deadline_label, QLabel#task_description_label {
                background-color: transparent;
                font-family: Helvetica;
                font-size: 18px;
                font: bold;
                color: rgb(235,235,235);
            }
            QLabel#user_input_task_name, QLabel#user_input_task_deadline, QTextEdit#user_input_task_description {
                background-color: rgb(246, 246, 246);
                font-family: Helvetica;
                font-size: 18px;
                border: 3px solid rgb(222, 222, 222);
                color: rgb(44, 44, 44);
            }
            QTextEdit#user_input_task_description {
                padding-top: 5px;
                padding-left: 10px;
                padding-right: 10px;
            }
            QPushButton#OK_Button {
                background-color: rgb(93, 217, 110);
                font-family: Helvetica;
                font-size: 18px;
                border: 3px solid;
                border-color: rgb(66, 135, 76);
                font: bold;
                color: rgb(44, 44, 44);
            }
        """)