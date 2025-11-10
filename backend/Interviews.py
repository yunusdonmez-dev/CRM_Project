from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import os
import pandas as pd
from AdminMain import AdminMain
from Prefs import Prefs
from session import Session

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
int_ui_path = os.path.join(parent_dir, "User Interfaces", "interviews.ui")

class Interviews(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(int_ui_path, self)
        self.button_back.clicked.connect(self.back)
        self.button_exit.clicked.connect(self.exit)
        self.load_excel_to_table() 

    def load_excel_to_table(self):
        try:
            df = pd.read_excel("backend\\Interviews.xlsx")
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(len(df.columns))
            self.tableWidget.setHorizontalHeaderLabels(df.columns)

            for row_idx, row_data in enumerate(df.values):
                self.tableWidget.insertRow(row_idx)
                for col_idx, value in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    self.tableWidget.setItem(row_idx, col_idx, item)

        except Exception as e:
            print(f" Unexpected error: {e}")

    def back(self):
        if Session.role == "admin":
            self.back_window = AdminMain()
        elif Session.role == "user":
            self.back_window = Prefs()
        self.back_window.show()        
        self.close()

    def exit(self):
        self.close()