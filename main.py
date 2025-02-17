import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,QApplication

class ejemplo_GUI(QMainWindow):
    def __init__(self): # constructor
        super().__init__()
        uic.loadUi("ui/restaurante.ui",self)

        #Llamada de los metodos por eventos
        self.btnProcesar.clicked.connect(self.Procesar)
        self.btnNuevo.clicked.connect(self.Limpiar)


    #Variables de nuestra ui
    def Lectura_Datos(self):
        self.Plato = self.txtPlatillo.text()
        self.Precio = float(self.txtPrecio.text())
        self.Cantidad = float(self.txtCantidad.text())
    

    #Accion del boton procesar
    def Procesar(self):
        #trae las variables
        self.Lectura_Datos()
        #Realiza calculos
        self.Importe = self.Precio*self.Cantidad
        self.Impuesto = self.Importe*0.18
        self.Total = self.Importe+self.Impuesto
        
        self.txtSalida.setText("")
        self.txtSalida.append("==================")
        self.txtSalida.append("   Comprobante de pago    ")
        self.txtSalida.append("==================")
        self.txtSalida.append("Platillo\t: "+str(self.Plato))
        self.txtSalida.append("Precio\t: "+str(self.Precio))
        self.txtSalida.append("Cantidad\t: "+str(self.Cantidad))
        self.txtSalida.append("==================")
        self.txtSalida.append("Importe\t: "+str(self.Importe))
        self.txtSalida.append("IGV(18%)\t: "+str(round(self.Impuesto,2)))
        self.txtSalida.append("Total\t: "+str(self.Total))

    #Accion del boton nuevo
    def Limpiar(self):
        #Borra la data de la caja 
        self.txtPlatillo.setText("")
        self.txtPrecio.setText("")
        self.txtCantidad.setText("")
        self.txtSalida.setText("")
        self.txtPlatillo.setFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ejemplo_GUI()
    GUI.show()
    sys.exit(app.exec_())