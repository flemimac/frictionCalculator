import math

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

from widgets.addDataWindow import AddData

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('layouts\windowMain.ui', self)
        self.setWindowTitle("Калькулятор")
        self.groupReynolds.hide()
        
        self.addData = AddData()
        
        self.buttonStart.clicked.connect(self.countingReynolds)
        self.buttonCheckData.clicked.connect(self.open_addData)
        
        
    def countingReynolds(self):
        self.inputLiquidDensity =  float(self.lineLiquidDensity.text())
        self.inputLiquidSpeed = float(self.lineLiquidSpeed.text())
        self.inputPipeDiameter = float(self.linePipeDiameter.text()) * 10**3
        self.inputDynamicCoeffLiquid = float(self.lineDynamicCoeffLiquid.text()) * 10**(-6)
        
        self.valueReynolds = ((self.inputLiquidDensity * self.inputLiquidSpeed * self.inputPipeDiameter) / (10**9 *self.inputDynamicCoeffLiquid))

        self.labelValueReynolds.setText(str(f"{round(self.valueReynolds, 2)}"))
        print(0, self.valueReynolds)
        
        if self.valueReynolds < 2300:
            valueFriction = 64 / self.valueReynolds
            
            self.labelValueFriction.setText(str(f"{valueFriction:3f}"))
            print(1, valueFriction)
        else:
            self.groupReynolds.show()
            # self.groupLedges.hide()
            
            self.buttonRoughnessNo.clicked.connect(self.countingFrictionNo)
            self.buttonRoughnessYes.clicked.connect(self.countingFrictionYes)
    
    def countingFrictionNo(self):
        if self.valueReynolds < 10**5:
            valueFriction = 0.3164 / pow(self.valueReynolds, (1 / 4))
            
            self.labelValueFriction.setText(str(f"{valueFriction:3f}"))
            print(2, valueFriction)
        else:
            valueFriction = (1.8 * math.log10(self.valueReynolds) - 1.5)**(-2)
            
            self.labelValueFriction.setText(str(f"{valueFriction:3f}"))
            print(3, valueFriction)
            
    def countingFrictionYes(self):
        # self.groupLedges.show()
        
        self.ledges = float(self.lineLedges.text())
        self.valueReynoldsM = (self.ledges / self.inputPipeDiameter) * self.valueReynolds

        print(self.valueReynoldsM)
        
        if self.valueReynoldsM < 10:
            if self.valueReynoldsM < 10**5:
                valueFriction = 0.3164 / pow(self.valueReynoldsM, (1 / 4))
            
                self.labelValueFriction.setText(str(f"{valueFriction:3f}"))
                print(2, valueFriction)
            else:
                valueFriction = (1.8 * math.log10(self.valueReynoldsM) - 1.5)**(-2)
            
                self.labelValueFriction.setText(str(f"{valueFriction:3f}"))
        elif 10 <= self.valueReynoldsM < 500:
            valueFriction = (0.1 * (1.46 * self.valueReynoldsM + (100 / self.valueReynolds))**0.25)
            self.labelValueFriction.setText(str(f"{valueFriction:3f}"))
        else:
            valueFriction = (2 * math.log10(1 / self.valueReynoldsM) + 1.74) ** -2
            self.labelValueFriction.setText(str(f"{valueFriction:3f}"))
            
    def open_addData(self):
        self.addData.show()