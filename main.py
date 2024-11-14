import sys
from PyQt6.QtWidgets import QApplication

from widgets.mainWindow import Calculator
from widgets.addDataWindow import AddData

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Calculator()
    mainWindow.show()

    sys.exit(app.exec())