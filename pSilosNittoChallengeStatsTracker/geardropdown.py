from PyQt5 import QtWidgets, QtCore, QtGui
from carcombo import selected_car
from dictionary import gear_ratios_df, final_ratio_df, gear_ratio_set


class GearRatioCombo(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        gear_ratio_combo = QtWidgets.QComboBox()
        gear_ratio_combo.setGeometry(QtCore.QRect(220, 10, 571, 22))
        gear_ratio_combo.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        gear_ratio_combo.setMaxVisibleItems(10)
        gear_ratio_combo.setObjectName("gear_ratio_combo")
        gear_ratio_combo.setCurrentIndex(0)
        selected_gear_ratio = gear_ratio_combo.currentText()
        gear_ratio_combo.gear_ratio_combo.currentIndexChanged.connect(selected_gear_ratio)
        # Populate the dropdown widget with the first 10 gear ratio sets
        gear_ratios = gear_ratios_df.index.tolist()[:10]
        for gear_ratio_set in gear_ratios:
            final = final_ratio_df.loc[gear_ratio_set, 'Final ET']
            expected_et = final_ratio_df.loc[gear_ratio_set, 'Expected ET']
            item_text = selected_car(gear_ratio_set)
            tooltip_text = f'Final ET: {final}, Expected ET: {expected_et}'
            gear_ratio_combo.addItem(item_text)
            gear_ratio_combo.setItemData(
                gear_ratio_combo.count() - 1,
                tooltip_text,
                QtCore.Qt.ToolTipRole
            )


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
        self.gear_ratio_set = gear_ratios_df.loc[self.selected_gear_ratio].values
        self.final_entry.setText(str(final_ratio_df.loc[self.selected_gear_ratio, 'Final ET']))
        self.expected_et_entry.setText(str(final_ratio_df.loc[self.selected_gear_ratio, 'Expected ET']))

    class GearEntries(QtWidgets.QWidget):
        def __init__(self, parent=None):
            super().__init__(parent)

            # Create a list of gear entry attribute names
            gear_entry_names = ["gear_1_entry", "gear_2_entry", "gear_3_entry", "gear_4_entry", "gear_5_entry",
                                "gear_6_entry"]

            # Loop over the list and create the attributes using setattr()
            for name in gear_entry_names:
                setattr(self, name, QtWidgets.QLineEdit(self))
                getattr(self, name).setGeometry(
                    QtCore.QRect(500, 60 + 50 * gear_entry_names.index(name), 91, 20))
                getattr(self, name).setObjectName(name)

            self.final_entry = QtWidgets.QLineEdit(self)
            self.final_entry.setGeometry(QtCore.QRect(690, 60, 91, 20))
            self.final_entry.setObjectName("final_entry")

            self.expected_et_entry = QtWidgets.QLineEdit(self)
            self.expected_et_entry.setGeometry(QtCore.QRect(690, 110, 91, 20))
            self.expected_et_entry.setObjectName("expected_et_entry")

            self.final_label = QtWidgets.QLabel(self)
            self.final_label.setGeometry(QtCore.QRect(710, 40, 71, 16))
            self.final_label.setObjectName("final_label")

            self.expected_et_label = QtWidgets.QLabel(self)
            self.expected_et_label.setGeometry(QtCore.QRect(700, 90, 71, 16))
            self.expected_et_label.setObjectName("expected_et_label")
            GearsWidget.selected_gear_ratio = self.gear_ratio_combo.currentText()

            self.gear_1_entry = None
            self.gear_2_entry = None
            self.gear_3_entry = None
            self.gear_4_entry = None
            self.gear_5_entry = None
            self.gear_6_entry = None
            self. final_entry = None
            self.expected_et_entry = None
            self.selected_gear_ratio = None
