from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
admin_ui_path = os.path.join(parent_dir, "User Interfaces", "admin_main.ui")

class AdminMain(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(admin_ui_path, self)
        self.button_mentor.clicked.connect(self.open_mentor)
        self.button_exit.clicked.connect(self.exit)
        self.button_app.clicked.connect(self.open_app)
        self.button_int.clicked.connect(self.open_interviews)
        self.button_admin.clicked.connect(self.open_admin_menu)
        self.button_main.clicked.connect(self.open_login)

    def open_login(self):
        from LoginWindow import LoginWindow
        self.login_window = LoginWindow() 
        self.login_window.show()        
        self.close()

    def open_app(self):
        from Applications import Applications
        self.app_window = Applications() 
        self.app_window.show()        
        self.close()

    def open_interviews(self):
        from Interviews import Interviews
        self.int_window = Interviews() 
        self.int_window.show()        
        self.close()
    
    def open_admin_menu(self):
        from AdminMenu import AdminMenu
        self.admin_menu_window = AdminMenu() 
        self.admin_menu_window.show()        
        self.close()

    def open_mentor(self):
        from Mentor import Mentor
        self.mentor_window = Mentor() 
        self.mentor_window.show()        
        self.close()

    def exit(self):
        self.close()