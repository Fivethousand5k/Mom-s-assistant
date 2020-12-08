from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem


class TreeWidgetTable(QTreeWidgetItem):
    def __init__(self,parent=None):
        super(TreeWidgetTable,self).__init__(parent)
        QTreeWidgetItem.__init__(parent)
        self.btn_start = QtWidgets.QToolButton()
