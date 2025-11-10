from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import os
import get_events 

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
admin_menu_ui_path = os.path.join(parent_dir, "User Interfaces", "admin_menu.ui")


class AdminMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(admin_menu_ui_path, self)
        self.load_events()
        self.button_back.clicked.connect(self.back)
        self.button_exit.clicked.connect(self.exit)
        self.button_activity.clicked.connect(self.load_events)
        self.button_send.clicked.connect(self.open_send_mail)
        self.load_events()

    def open_send_mail(self):
        pass
        # from SendMail import SendMail
        # self.send_mail_window = SendMail()
        # self.send_mail_window.show()

    def back(self):
        from AdminMain import AdminMain
        self.back_window = AdminMain()
        self.back_window.show()        
        self.close()
    
    def load_events(self):
        try:
            events = get_events.main()
            if not events:
                QtWidgets.QMessageBox.information(
                    self, "INFO", "There are no events in the calendar."
                )
                return

            self.tableWidget.setRowCount(len(events))
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(
                ["Activity Name", "Start", "Participant Mail", "Organizer Mail"]
            )

            for i, e in enumerate(events):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(e["title"]))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(e["start"]))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(", ".join(e.get("attendees") or [])))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(e.get("organizer") or ""))

            self.tableWidget.resizeColumnsToContents()
        except Exception as ex:
            QtWidgets.QMessageBox.critical(self, "Error", str(ex))

    def exit(self):
        self.close()