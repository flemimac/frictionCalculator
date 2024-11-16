from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

from database.DataDensities.requests import addData 

class AddDensity(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('layouts\windowAddDensity.ui', self)
        self.setWindowTitle("Добавление плотности")
        
        self.buttonAddDensity.clicked.connect(self.addDensity)
    
    def addDensity(self):
        self.density = str(self.lineDensity.text())
        self.value = int(self.lineValue.text())
        
        addData(self.density, self.value)
        
        self.lineDensity.clear()
        self.lineValue.clear()
