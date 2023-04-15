import tkinter as ttk


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


selected_car = None


class CarsWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        global selected_car
        self.selected_car = None

        self.car_combo = ttk.ttk.Combobox(self, values=CAR_NAMES)
        self.car_combo.place(x=40, y=150)
        self.car_combo.bind('<<ComboboxSelected>>', self.update_selected_car)
        self.selected_car = self.car_combo.get()

    def update_selected_car(self):
        global selected_car
        self.selected_car = self.car_combo.get()
