import sys
from PyQt5.QtWidgets import QApplication
from add_task_dialog import AddTaskDialog

def main():
    app = QApplication(sys.argv)
    task_dialog_box = AddTaskDialog()
    task_dialog_box.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()