import tkinter as tk
from tkinter import ttk
from dictionary import gear_ratios_df, final_ratio_df
from carcombo import selected_car


class GearEntries:
    def __init__(self, parent):
        self.parent = parent

        # Create a list of gear entry attribute names
        gear_entry_names = ["gear_1_entry", "gear_2_entry", "gear_3_entry", "gear_4_entry", "gear_5_entry",
                            "gear_6_entry"]

        # Loop over the list and create the attributes using setattr()
        for name in gear_entry_names:
            setattr(self, name, tk.Entry(self.parent, width=10))
            getattr(self, name).pack(pady=5)

        self.final_entry = tk.Entry(self.parent, width=10, state='readonly')
        self.final_entry.pack(pady=10)

        self.expected_et_entry = tk.Entry(self.parent, width=10, state='readonly')
        self.expected_et_entry.pack(pady=10)

        self.final_label = tk.Label(self.parent, text='Final ET')
        self.final_label.pack()

        self.expected_et_label = tk.Label(self.parent, text='Expected ET')
        self.expected_et_label.pack()

        self.gear_ratio_combo = None  # Add this line

        self.selected_gear_ratio = tk.StringVar()

    def update_gear_ratio_values(self):
        # Get the currently selected gear ratio set
        self.selected_gear_ratio.set(self.gear_ratio_combo.get())

        # Update the final ET and expected ET values based on the selected gear ratio set
        self.final_entry.delete(0, 'end')
        self.final_entry.insert(0, final_ratio_df.loc[self.selected_gear_ratio.get(), 'Final ET'])

        self.expected_et_entry.delete(0, 'end')
        self.expected_et_entry.insert(0, final_ratio_df.loc[self.selected_gear_ratio.get(), 'Expected ET'])


class GearsWidget:
    def __init__(self, parent):
        self.parent = parent

        self.gear_entries = GearEntries(self.parent)

        self.gear_entries.gear_ratio_combo = ttk.Combobox(
            self.parent,
            values=[selected_car(gear_ratio_set) for gear_ratio_set in gear_ratios_df.index.tolist()[:10]],
            state='readonly'
        )
        self.gear_entries.gear_ratio_combo.set(gear_ratios_df.index.tolist()[0])
        self.gear_entries.gear_ratio_combo.pack(pady=10)

        self.gear_entries.gear_ratio_combo.bind('<<ComboboxSelected>>', self.gear_entries.update_gear_ratio_values)

        self.gear_ratio_label = tk.Label(self.parent, text='Gear Ratio Set')
        self.gear_ratio_label.pack()
