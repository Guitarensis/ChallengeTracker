from PyQt5 import QtWidgets, QtCore, QtGui


class GearsWidget(QtWidgets.QWidget):
    gears_entered = QtCore.pyqtSignal(float, float, float, float, float, float, float, float)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.gear_1_entry = QtWidgets.QLineEdit(self)
        self.gear_1_entry.setGeometry(QtCore.QRect(500, 60, 91, 20))
        self.gear_1_entry.setText("")
        self.gear_1_entry.setObjectName("gear_1_entry")
        self.gear_2_entry = QtWidgets.QLineEdit(self)
        self.gear_2_entry.setGeometry(QtCore.QRect(500, 110, 91, 20))
        self.gear_2_entry.setObjectName("gear_2_entry")
        self.gear_3_entry = QtWidgets.QLineEdit(self)
        self.gear_3_entry.setGeometry(QtCore.QRect(500, 160, 91, 20))
        self.gear_3_entry.setObjectName("gear_3_entry")
        self.gear_4_entry = QtWidgets.QLineEdit(self)
        self.gear_4_entry.setGeometry(QtCore.QRect(600, 60, 81, 20))
        self.gear_4_entry.setObjectName("gear_4_entry")
        self.gear_5_entry = QtWidgets.QLineEdit(self)
        self.gear_5_entry.setGeometry(QtCore.QRect(600, 110, 81, 20))
        self.gear_5_entry.setObjectName("gear_5_entry")
        self.gear_6_entry = QtWidgets.QLineEdit(self)
        self.gear_6_entry.setGeometry(QtCore.QRect(600, 160, 81, 20))
        self.gear_6_entry.setObjectName("gear_6_entry")
        self.final_entry = QtWidgets.QLineEdit(self)
        self.final_entry.setGeometry(QtCore.QRect(690, 60, 91, 20))
        self.final_entry.setObjectName("final_entry")
        self.expected_et_entry = QtWidgets.QLineEdit(self)
        self.expected_et_entry.setGeometry(QtCore.QRect(690, 110, 91, 20))
        self.expected_et_entry.setObjectName("expected_et_entry")
        self.gear_1_label = QtWidgets.QLabel(self)
        self.gear_1_label.setGeometry(QtCore.QRect(530, 40, 41, 20))
        self.gear_1_label.setObjectName("gear_1_label")
        self.gear_2_label = QtWidgets.QLabel(self)
        self.gear_2_label.setGeometry(QtCore.QRect(530, 90, 41, 20))
        self.gear_2_label.setObjectName("gear_2_label")
        self.gear_3_label = QtWidgets.QLabel(self)
        self.gear_3_label.setGeometry(QtCore.QRect(530, 140, 47, 13))
        self.gear_3_label.setObjectName("gear_3_label")
        self.gear_4_label = QtWidgets.QLabel(self)
        self.gear_4_label.setGeometry(QtCore.QRect(620, 40, 47, 13))
        self.gear_4_label.setObjectName("gear_4_label")
        self.gear_5_label = QtWidgets.QLabel(self)
        self.gear_5_label.setGeometry(QtCore.QRect(620, 90, 47, 13))
        self.gear_5_label.setObjectName("gear_5_label")
        self.gear_6_label = QtWidgets.QLabel(self)
        self.gear_6_label.setGeometry(QtCore.QRect(620, 140, 47, 13))
        self.final_label = QtWidgets.QLabel(self)
        self.final_label.setGeometry(QtCore.QRect(710, 40, 71, 16))
        self.final_label.setObjectName("final_label")
        self.expected_et_label = QtWidgets.QLabel(self)
        self.expected_et_label.setGeometry(QtCore.QRect(700, 90, 71, 16))
        self.expected_et_label.setObjectName("expected_et_label")
        self.gear_ratio_combo.setCurrentIndex(0)
        self.selected_gear_ratio = self.gear_ratio_combo.currentText()


class GearsEntries:
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        GearsWidget.gear_1_entry = self.gear_1_entry
        GearsWidget.gear_2_entry = self.gear_2_entry
        GearsWidget.gear_3_entry = self.gear_3_entry
        GearsWidget.gear_4_entry = self.gear_4_entry
        GearsWidget.gear_5_entry = self.gear_5_entry
        GearsWidget.gear_6_entry = self.gear_6_entry
        GearsWidget.gear_1_label = self.gear_1_label
        GearsWidget.gear_2_label = self.gear_2_label
        GearsWidget.gear_3_label = self.gear_3_label
        GearsWidget.gear_4_label = self.gear_4_label
        GearsWidget.gear_5_label = self.gear_5_label
        GearsWidget.gear_6_label = self.gear_6_label
        GearsWidget.final_entry = self.final_entry
        GearsWidget.final_label = self.final_label
        GearsWidget.expected_et_entry = self.expected_et_entry
        self.gear_1_entry = None
        self.gear_2_entry = None
        self.gear_3_entry = None
        self.gear_4_entry = None
        self.gear_5_entry = None
        self.gear_6_entry = None
        self. final_entry = None
        self.expected_et_entry = None
class GearRatioCombo(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.gear_ratio_combo = None
        self.gear_ratio_combo = QtWidgets.QComboBox(self)
        self.gear_ratio_combo.setGeometry(QtCore.QRect(220, 10, 571, 22))
        self.gear_ratio_combo.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.gear_ratio_combo.setMaxVisibleItems(5)
        self.gear_ratio_combo.setObjectName("gear_ratio_combo")

        # Populate the dropdown widget with the first 5 gear ratio sets
        gear_ratios = gear_ratios_df.index.tolist()[:5]
        for gear_ratio in gear_ratios:
            self.gear_ratio_combo.addItem(selected_car(gear_ratio))
        return gear_ratios[selected_car][gear_ratio_key]
