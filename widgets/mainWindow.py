import math

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QIcon

from widgets.dataWindow import Data
from widgets.resultsWindow import Results
from widgets.graphWindow import Graph

from database.DataDensities.requests import fetchMaterials, loadMaterials
from database.DataResults.requests import addData, allData

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('layouts\windowMain.ui', self)
        self.setWindowTitle("Калькулятор")
        self.setWindowIcon(QIcon('images/logo.png')) 
        self.groupReynolds.hide()
        
        self.Data = Data()
        self.Results = Results()
        self.Graph = Graph()
        
        # загрузка материалов в комбобокс
        loadMaterials(self.lineLiquidDensityComboBox)
        
        self.buttonStart.clicked.connect(self.countingReynolds)
        self.buttonCheckData.clicked.connect(self.openAddData)
        self.buttonCheckResults.clicked.connect(self.openResults)
        self.buttonCheckGraph.clicked.connect(self.openGraph)
        

        
    def countingReynolds(self):
        try:
            self.inputLiquidDensity = fetchMaterials(self.lineLiquidDensityComboBox.currentText())
            if self.inputLiquidDensity is None or self.inputLiquidDensity <= 0:
                raise ValueError("Пожалуйста, выберите корректную плотность жидкости.")
            
            self.inputLiquidSpeed = float(self.lineLiquidSpeed.text())
            if self.inputLiquidSpeed <= 0:
                raise ValueError("Пожалуйста, введите положительное значение скорости жидкости.")
            
            self.inputPipeDiameter = float(self.linePipeDiameter.text()) * 10**3
            if self.inputPipeDiameter <= 0:
                raise ValueError("Пожалуйста, введите положительное значение диаметра трубы.")
            
            self.inputDynamicCoeffLiquid = float(self.lineDynamicCoeffLiquid.text()) * 10**(-6)
            if self.inputDynamicCoeffLiquid <= 0:
                raise ValueError("Пожалуйста, введите положительное значение динамического коэффициента жидкости.")

            self.valueReynolds = ((self.inputLiquidDensity * self.inputLiquidSpeed * self.inputPipeDiameter) / (10**9 * self.inputDynamicCoeffLiquid))

            self.labelValueReynolds.setText(str(f"{round(self.valueReynolds, 2)}"))
            print(0, self.valueReynolds)
            
            if self.valueReynolds < 2300:
                valueFriction = 64 / self.valueReynolds
                
                self.labelValueFriction.setText(str(f"{valueFriction:.3f}"))
                addData(valueFriction)
                print(1, valueFriction)
            else:
                self.groupReynolds.show()
                self.buttonRoughnessNo.clicked.connect(self.countingFrictionNo)
                self.buttonRoughnessYes.clicked.connect(self.countingFrictionYes)

        except ValueError as e:
            QMessageBox.warning(self, "Ошибка ввода", str(e))
    
    def countingFrictionNo(self):
        if self.valueReynolds < 10**5:
            valueFriction = 0.3164 / pow(self.valueReynolds, (1 / 4))
            
            self.labelValueFriction.setText(str(f"{valueFriction:.3f}"))
            addData(f"{valueFriction:.3f}")
            print(2, valueFriction)
        else:
            valueFriction = (1.8 * math.log10(self.valueReynolds) - 1.5)**(-2)
            
            self.labelValueFriction.setText(str(f"{valueFriction:.3f}"))
            addData(f"{valueFriction:.3f}")
            print(3, valueFriction)
            
    def countingFrictionYes(self):
        try:
            self.ledges = float(self.lineLedges.text())
            
            if self.ledges <= 0:
                raise ValueError("Значение должно быть положительным.")
        
            self.valueReynoldsM = (self.ledges / self.inputPipeDiameter) * self.valueReynolds

            print(self.valueReynoldsM)
            
            if self.valueReynoldsM < 10:
                if self.valueReynoldsM < 10**5:
                    valueFriction = 0.3164 / pow(self.valueReynoldsM, (1 / 4))
                
                    self.labelValueFriction.setText(str(f"{valueFriction:.3f}"))
                    addData(f"{valueFriction:.3f}")
                    print(2, valueFriction)
                else:
                    valueFriction = (1.8 * math.log10(self.valueReynoldsM) - 1.5)**(-2)
                
                    self.labelValueFriction.setText(str(f"{valueFriction:.3f}"))
                    addData(f"{valueFriction:.3f}")
            elif 10 <= self.valueReynoldsM < 500:
                valueFriction = (0.1 * (1.46 * self.valueReynoldsM + (100 / self.valueReynolds))**0.25)
                self.labelValueFriction.setText(str(f"{valueFriction:.3f}"))
                addData(f"{valueFriction:.3f}")
            else:
                valueFriction = (2 * math.log10(1 / self.valueReynoldsM) + 1.74) ** -2
                self.labelValueFriction.setText(str(f"{valueFriction:.3f}"))
                addData(f"{valueFriction:.3f}")
                
        except ValueError:
            QMessageBox.warning(self, "Ошибка ввода", "Пожалуйста, введите корректное значение.")

    def openAddData(self):
        self.Data.show()
        
    def openResults(self):
        self.Results.show()
        
    def openGraph(self):
        data = allData()
        self.Graph.plot_graph(data) 