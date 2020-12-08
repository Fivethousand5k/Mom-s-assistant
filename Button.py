from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QFileDialog
from read_excel import handler_excel

class Button(QPushButton):

    def __init__(self, title, parent,label_address=None):
        super().__init__(title, parent)
        icon_btn_close = QIcon('resources/icons8-file-100.png')  # 在线检测的icon
        self.setIcon(icon_btn_close)
        self.setIconSize(QSize(120, 120))
        self.setAcceptDrops(True)
        self.text=None
        self.resize(parent.size())
        self.clicked.connect(self.select_file)
        self.label_address=label_address


    def select_file(self):
        self.text,_ =  QFileDialog.getOpenFileName(self, '选择文件', '.')

        self.label_address.setText(self.text)
    def dragEnterEvent(self, e):

        # if e.mimeData().hasFormat('text/plain'):
        #     e.accept()
        # else:
        #     e.ignore()
      e.accept()

    def dropEvent(self, e):
        print(e.mimeData().text())
        self.text=e.mimeData().text()
    def parse_excel1(self,time_range=3):
        if self.text != None and self.text!='':
            self.text=self.text.replace("file:///","")
            return handler_excel(self.text,time_range)
        else:
            return None
             #return handler_excel(self.text)