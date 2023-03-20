from PyQt5 import QtWidgets
from Ventana_principal import Ui_ventana_principal
from Ventana_Datos_Materia import Ui_ventana_materia
import sys

class ventana(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ventana_principal()
        self.ui.setupUi(self)
        
        self.ui.btn_carre_conda.clicked.connect(self.ventana_materias)
    
    def ventana_materias(self):
        super().__init__()
        self.Ui = Ui_ventana_materia()
        self.Ui.setupUi(self)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    otra_ventana = ventana()
    otra_ventana.show()
    sys.exit(app.exec_())