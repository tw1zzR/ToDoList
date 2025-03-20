from PyQt5.QtWidgets import QDialog


class AddDelDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
