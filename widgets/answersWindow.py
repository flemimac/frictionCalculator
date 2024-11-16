from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QStandardItemModel, QStandardItem

from database.DataAnswers.requests import fetchData, deleteData, createData

class Results(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('layouts\windowAnswer.ui', self)
        self.setWindowTitle("Данные")
        
        self.buttonDeleteAnswer.clicked.connect(self.deleteAnswer)
        self.buttonRestartAnswer.clicked.connect(self.loadData)
        createData()
        self.loadData()
    
    def loadData(self):
        data = fetchData()
        
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Значение'])

        for row in data:
            items = [QStandardItem(str(item)) for item in row]
            model.appendRow(items)

        self.tableAnswer.setModel(model)
        
    
    def deleteAnswer(self):
        selected_indexes = self.tableAnswer.selectedIndexes()
        
        if not selected_indexes:
            print("Ошибка Выберите строку для удаления.")
            return
        
        selected_row = selected_indexes[0].row()
        model = self.tableAnswer.model()
        
        value = model.item(selected_row, 0).text()

        deleteData(value)

        self.loadData()
        