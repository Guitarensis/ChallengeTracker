import tkinter as tk

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


class CarsWidget:
    def __init__(self, parent):
        self.parent = parent
        global selected_car
        self.selected_car = None

        self.car_combo = tk.StringVar(self.parent)
        self.car_combo.set(CAR_NAMES[0])
        self.car_combo.trace("w", self.update_selected_car)

        tk.Label(self.parent, text="Select a car:").pack(pady=5)
        tk.OptionMenu(self.parent, self.car_combo, *CAR_NAMES).pack(pady=5)

        self.selected_car = self.car_combo.get()

    def update_selected_car(self):
        global selected_car
        self.selected_car = self.car_combo.get()
        selected_car = self.selected_car
