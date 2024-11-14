from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QStandardItemModel, QStandardItem

from database.requests import fetch_data

class AddData(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('layouts\windowAddData.ui', self)
        self.setWindowTitle("Добавление данных")
        self.load_data()
    
    def load_data(self):
        data = fetch_data()
        
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Density', 'Value'])

        for row in data:
            items = [QStandardItem(str(item)) for item in row]
            model.appendRow(items)

        self.tableData.setModel(model)