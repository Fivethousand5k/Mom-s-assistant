#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author Fivethousand
    @Date 2020/12/12 14:16
    @Describe 
    @Version 1.0
"""

import os
import sys
import xlwt

from PyQt5 import QtWidgets, QtCore, Qt, QtGui
from PyQt5.QtWidgets import QApplication, QTreeWidgetItem, QFileDialog
from TreewidgetTable import TreeWidgetTable
from GUI import Ui_Form
from Button import Button
from read_excel import Excel_Parser
class Mom_Assistant(QtWidgets.QMainWindow,Ui_Form):
    def __init__(self,parent=None):
        super(Mom_Assistant, self).__init__(parent)
        self.setupUi(self)
        self.init_ui()
        self.init_thread()
        self.init_connection()

    def init_ui(self):
        self.setWindowTitle("老妈助手")
        #self.setWindowFlags(Qt.Qt.FramelessWindowHint)      #无边框窗口
        self.setFixedSize(self.width(), self.height())   #固定长宽

        self.treeWidget.setColumnCount(10)  # 设置部件的列数
        self.treeWidget.setHeaderLabels(['卡号', '姓名','交易类型','交易份额','交易单价','交易总额','交易日期','签约机构','推荐人工号','合作行名'])  # 设置头部信息对应列的标识符
       # the following 3 lines guarantee that the
        self.treeWidget.header().setSectionResizeMode(3)
        self.treeWidget.StretchLastSection=False
        self.treeWidget.setAutoScroll(False)
        self.root=TreeWidgetTable(self.treeWidget)
        self.treeWidget.addTopLevelItem(self.root)

        self.root.setText(0, '筛查结果')
        # for i in range(100):
        #     child = QTreeWidgetItem()
        #     child.setText(0,'123')
        #     self.root.addChild(child)

        self.file_drop_btn=Button('',self.widget,self.label_address)



        # self.setCentralWidget(self.treeWidget)  # 将tree部件设置为该窗口的核心框架

    def init_thread(self):
        self.Excel_parser=Excel_Parser()
        self.Excel_parser.start()



    def init_connection(self):
        self.btn_search.clicked.connect(self.parse_excel)
        self.btn_export.clicked.connect(self.export)
        self.Excel_parser.trigger.connect(self.display_result)
        self.Excel_parser.text_signal.connect(self.set_title_text)
        self.file_drop_btn.text_signal.connect(self.set_address_text)

    def display_result(self,result):        # display the result from Excel_parser
        if result != None:
            for card_id, name in result:
                personal_result = result[(card_id, name)]
                child = QTreeWidgetItem()
                child.setText(1, name)
                child.setText(0, str(card_id))
                # child.setBackground(1, QtGui.QColor('green'))
                self.root.addChild(child)
                for buy_tuple in personal_result:
                    personal_result2 = personal_result[buy_tuple]
                    name, transaction_type, num, u_price, total, time, contractor, refers_num, co_bank = buy_tuple
                    subchild = QTreeWidgetItem()
                    # subchild.setForeground(0, Qt.green)
                    subchild.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)  # 设为可编辑
                    subchild.setText(1, name)
                    subchild.setText(0, str(card_id))
                    subchild.setText(2, transaction_type)
                    subchild.setText(3, str(num))
                    subchild.setText(4, str(u_price))
                    subchild.setText(5, str(total))
                    subchild.setText(6, time)
                    subchild.setText(7, str(contractor))
                    subchild.setText(8, str(refers_num))
                    subchild.setText(9, str(co_bank))
                    child.addChild(subchild)
                    if transaction_type == "客户买入":
                        subchild.setForeground(2, QtGui.QColor('red'))
                    for msg in personal_result2:
                        name, transaction_type, num, u_price, total, time, contractor, refers_num, co_bank = msg
                        subchild = QTreeWidgetItem()
                        subchild.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)  # 设为可编辑
                        subchild.setText(1, name)
                        subchild.setText(0, str(card_id))
                        subchild.setText(2, transaction_type)
                        subchild.setText(3, str(num))
                        subchild.setText(4, str(u_price))
                        subchild.setText(5, str(total))
                        subchild.setText(6, time)
                        subchild.setText(7, str(contractor))
                        subchild.setText(8, str(refers_num))
                        subchild.setText(9, str(co_bank))
                        child.addChild(subchild)
        self.root.setExpanded(True)

    def set_title_text(self,text):            # connected with the Excel_parser, it receives the signal from Excel_parser and display it on the title.
        self.setWindowTitle("老妈助手"+text)

    def set_address_text(self,text):
        text=text.split('/')[-1]
        self.label_address.setText("当前选择: "+text)
    def parse_excel(self):
        self.root.takeChildren()        # clear all the children under the root
        time_range=self.spinBox_timerange.value()
        self.Excel_parser.begin(time_range=time_range,filename=self.file_drop_btn.text)

    def export(self):       #导出
        row_count,col_count=0,0
        save_path=QFileDialog.getExistingDirectory()
        workbook = xlwt.Workbook(encoding='utf-8')
        booksheet=workbook.add_sheet('Sheet1', cell_overwrite_ok = True)
        title=['卡号','姓名','交易类型','交易份额','交易单价','交易总额','交易日期','签约机构','推荐人工号','合作行名']
        for i,tt in enumerate(title):
            booksheet.write(0, i, tt)
        row_count+=1
        child_count=self.root.childCount()      # count the number of children
        for i in range(child_count):
            child=self.root.child(i)
            subchild_count=child.childCount()
            for j in range(subchild_count):
                subchild=child.child(j)
                card, name, transaction_type, num, u_price, total, time, contractor, refers_num, co_bank=subchild.text(0),subchild.text(1),subchild.text(2),subchild.text(3),subchild.text(4),subchild.text(5),subchild.text(6),subchild.text(7),subchild.text(8),subchild.text(9)
                booksheet.write(row_count, 0, card)
                booksheet.write(row_count, 1, name)
                booksheet.write(row_count, 2, transaction_type)
                booksheet.write(row_count, 3, num)
                booksheet.write(row_count, 4, u_price)
                booksheet.write(row_count, 5, total)
                booksheet.write(row_count, 6, time)
                booksheet.write(row_count, 7, contractor)
                booksheet.write(row_count, 8, refers_num)
                booksheet.write(row_count, 9, co_bank)

                row_count+=1
        workbook.save(os.path.join(save_path,'结果.xls'))



if __name__ == '__main__':
        app = QApplication(sys.argv)
        myWin = Mom_Assistant()
        myWin.show()

        sys.exit(app.exec_())

