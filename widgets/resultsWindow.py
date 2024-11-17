from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QStandardItemModel, QStandardItem

from database.DataResults.requests import *

class Results(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('layouts\windowResults.ui', self)
        self.setWindowTitle("Данные")
        
        self.buttonDeleteResults.clicked.connect(self.deleteResults)
        self.buttonClearResults.clicked.connect(self.clearResults)
        self.buttonRestartResults.clicked.connect(self.loadData)
        
        createData()
        self.loadData()
    
    def loadData(self):
        data = fetchData()
        
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Номер', 'Значение'])

        for row in data:
            items = [QStandardItem(str(item)) for item in row]
            model.appendRow(items)

        self.tableAnswer.setModel(model)
        
    
    def deleteResults(self):
        selected_indexes = self.tableAnswer.selectedIndexes()
        
        if not selected_indexes:
            print("Ошибка Выберите строку для удаления.")
            return
        
        selected_row = selected_indexes[0].row()
        model = self.tableAnswer.model()
        
        number = model.item(selected_row, 0).text()
        value = model.item(selected_row, 1).text()

        deleteData(number)

        self.loadData()
        
    def clearResults(self):
        clearData()
        self.loadData()