from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import os
import pandas as pd
from AdminMain import AdminMain
from Prefs import Prefs
from session import Session

current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
mentor_ui_path = os.path.join(parent_dir, "User Interfaces", "mentor.ui")


class Mentor(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(mentor_ui_path, self)
        self.button_back.clicked.connect(self.back)
        self.button_exit.clicked.connect(self.exit)
        self.lineEdit.textChanged.connect(self.search_in_table)
        self.comboBox.currentIndexChanged.connect(self.filter_by_combobox)
        self.button_all_app.clicked.connect(self.load_excel_to_table)

    def filter_by_combobox(self):
        selected_value = self.comboBox.currentText().strip().lower()

        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 4)
            if not item:
                continue

            cell_text = item.text().strip().lower()

            if selected_value in ("all", ""):
                self.tableWidget.setRowHidden(row, False)
            else:
                self.tableWidget.setRowHidden(row, selected_value not in cell_text)

    def search_in_table(self):
        query = self.lineEdit.text().strip().lower()

        for row in range(self.tableWidget.rowCount()):
            match_found = False
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item and query in item.text().strip().lower():
                    match_found = True
                    break
            self.tableWidget.setRowHidden(row, not match_found)

    def load_excel_to_table(self):
        try:
            df = pd.read_excel("Mentor.xlsx")
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
