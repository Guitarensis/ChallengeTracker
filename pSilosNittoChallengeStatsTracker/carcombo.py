from PyQt5 import QtWidgets, QtCore

global selected_car
CAR_NAMES = ['Challenger',
             'Charger',
             'Civic',
             'Ftype',
             'FunnyCar',
             'Lancer',
             'Mopar',
             'Mustang',
             'Ram',
             'RSX',
             'RX8',
             'Skyline',
             'SRT4',
             'Subaru',
             'Supra',
             'TFD',
             'Viper']


class CarsWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        global selected_car
        self.selected_car = None

        self.car_combo = QtWidgets.QComboBox(self)
        self.car_combo.setGeometry(QtCore.QRect(40, 150, 191, 22))
        self.car_combo.setMaxVisibleItems(20)
        self.car_combo.setObjectName("car_combo")
        self.car_combo.addItems(CAR_NAMES)
        self.car_combo.setCurrentIndex(0)
        self.car_combo.currentIndexChanged.connect(self.update_selected_car)
        self.selected_car = self.car_combo.currentText()

    def update_selected_car(self):
        self.selected_car = self.car_combo.currentText()
        global selected_car
        selected_car = self.selected_car
