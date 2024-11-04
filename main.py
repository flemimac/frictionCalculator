import sys
import math

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QGroupBox


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calculator.ui', self)
        self.setWindowTitle("Калькулятор")
        self.groupReynolds.hide()
        self.buttonStart.clicked.connect(self.countingReynolds)
        
    def countingReynolds(self):
        lineLiquindDensity =  float(self.lineLiquidDensity.text())
        lineLiquidSpeed = float(self.lineLiquidSpeed.text())
        linePipeDiameter = float(self.linePipeDiameter.text())
        lineDynamicCoeffLiquid = float(self.lineDynamicCoeffLiquid.text())
        
        self.valueReynolds = (lineLiquindDensity * lineLiquidSpeed * linePipeDiameter) / lineDynamicCoeffLiquid
        self.labelValueReynolds.setText(str(f"{self.valueReynolds:3f}"))
        print(self.valueReynolds)
        
        if self.valueReynolds < 2300:
            valueFriction = 64 / self.valueReynolds
            self.labelValueFriction.setText(str(f"{valueFriction:3f}"))
            print(valueFriction)
        else:
            self.groupReynolds.show()
            self.buttonRoughnessNo.clicked.connect(self.countingFrictionNo)
    
    def countingFrictionNo(self):
        if self.valueReynolds < 10**5:
            valueFriction = 0.3164 / pow(self.valueReynolds, (1 / 4))
            self.labelValueFriction.setText(str(f"{valueFriction:3f}"))
            print(valueFriction)
        else:
            valueFriction = (1.8 * math.log10(self.valueReynolds) - 1.5)**(-2)
            self.labelValueFriction.setText(str(f"{valueFriction:3f}"))
            print(valueFriction)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())