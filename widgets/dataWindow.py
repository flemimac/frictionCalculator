from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QInputDialog
from PyQt6.QtGui import QStandardItemModel, QStandardItem

from database.DataDensities.requests import fetchData, deleteData, updateData, createData
from widgets.addDensityWindow import AddDensity

class Data(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('layouts\windowData.ui', self)
        self.setWindowTitle("Данные")
        self.AddDensity = AddDensity()
        
        self.buttonAddDensity.clicked.connect(self.addDensity)
        self.buttonEditDensity.clicked.connect(self.editDensity)
        self.buttonDeleteDensity.clicked.connect(self.deleteDensity)
        self.buttonRestartDensity.clicked.connect(self.loadData)
        createData()
        self.loadData()
    
    def loadData(self):
        data = fetchData()
        
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Плотность', 'Значение'])

        for row in data:
            items = [QStandardItem(str(item)) for item in row]
            model.appendRow(items)

        self.tableData.setModel(model)
        
    def addDensity(self):
        self.AddDensity.show()
        self.loadData()
        
    
    def deleteDensity(self):
        selected_indexes = self.tableData.selectedIndexes()
        
        if not selected_indexes:
            print("Ошибка Выберите строку для удаления.")
            return
        
        selected_row = selected_indexes[0].row()
        model = self.tableData.model()
        
        density = model.item(selected_row, 0).text()
        value = model.item(selected_row, 1).text()

        deleteData(density, value)

        self.loadData()
        
    def editDensity(self):
        selected_index = self.tableData.currentIndex()
        
        if not selected_index.isValid():
            print("Пожалуйста, выберите строку для редактирования.")
            return

        selected_row = selected_index.row()
        density_item = self.tableData.model().item(selected_row, 0).text()
        value_item = self.tableData.model().item(selected_row, 1).text()
        
        new_density, ok1 = QInputDialog.getText(self, "Редактирование", "Введите новую плотность:", text=density_item)
        new_value, ok2 = QInputDialog.getText(self, "Редактирование", "Введите новое значение:", text=value_item)

        if ok1 and ok2:
            updateData(density_item, new_density, new_value)
            self.loadData()