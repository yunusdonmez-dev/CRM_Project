import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import os
import pandas as pd
from session import Session

current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
excel_path = os.path.join(current_dir, "Kullanicilar .xls")
df = pd.read_excel(excel_path)
users = df.to_dict(orient="records")
login_ui_path = os.path.join(parent_dir, "User Interfaces", "login.ui")

class LoginWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(login_ui_path, self)
        self.button_login.clicked.connect(self.login)
        self.button_exit.clicked.connect(self.exit)
        
    def exit(self):
        self.close()

    def login(self):
        from AdminMain import AdminMain
        from Prefs import Prefs
        username = self.Username.text()
        password = self.Password.text()
        found = False
        for u in users:
            if u["kullanici"] == username and u["parola"] == password:
                found = True
                if u["yetki"]== "admin":
                    Session.role = "admin"
                    self.admin_window = AdminMain() 
                    self.admin_window.show()        
                    self.close()
                    
                else:
                    Session.role = "user"
                    self.admin_menu_window = Prefs() 
                    self.admin_menu_window.show()        
                    self.close()
                break

        if not found:
            Session.role = None
            self.error.setText(" Incorrect Username or Password!")