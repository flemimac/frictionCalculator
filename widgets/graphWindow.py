from PyQt6.QtWidgets import QMainWindow

import matplotlib.pyplot as plt

class Graph(QMainWindow):
    def __init__(self):
        super().__init__()
        
    def plot_graph(self, data):
        plt.figure()
        plt.plot(data)
        plt.title("График")
        plt.xlabel("Индекс результата")
        plt.ylabel("Значение результата")
        plt.grid()
        
        plt.show()
        
        plt.savefig('graph.png')
