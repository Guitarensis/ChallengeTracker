from carcombo import selected_car
from dictionary import load_dataframes
from geardropdown import GearsWidget, gear_rat
from PyQt5 import QtWidgets
from IPython.external.qt_for_kernel import QtCore
import configparser
import keyboard
import os
import psutil



# List of applications that need to be running
app_list = ['1320v200.exe', '1320v200Scalable.exe', '1320v200Scalable60.exe']

# Load dataframes
load_dataframes()

# Press Ctrl+Shift+Z to print "Hotkey Detected"
keyboard.add_hotkey('alt+shift+z', print, args=('Hotkey', 'Detected'))

# Wait for Esc key to be pressed
keyboard.wait('esc')

def start():
    # Check for saved gear ratios
    config = configparser.ConfigParser()
    config_file = os.path.join('scripts', 'configs.ini')
    if os.path.exists(config_file):
        config.read(config_file)
        last_gear_ratio_name = config.get('last_gear_ratio', 'name', fallback=None)
        if last_gear_ratio_name is not None:
            # combo_box needs to be defined in this scope or passed as an argument
            gear_ratio_index = combo_box.findText(last_gear_ratio_name)
            if gear_ratio_index != -1:
                combo_box.setCurrentIndex(gear_ratio_index)

    # Define gear_ratios dictionary
    gear_ratios = {
        "gear_ratio_set_1": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
        "gear_ratio_set_2": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
        "gear_ratio_set_3": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
        "gear_ratio_set_4": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
        "gear_ratio_set_5": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0]
    }


    # Check if required applications are running
    def check_app_running(app_list):
        for proc in psutil.process_iter(['name']):
            if app_list in proc.info['name']:
                return True
        return False


    def check_required_apps():
        for app in app_list:
            if not check_app_running(app_list):
                QtWidgets.QMessageBox.critical(None, "Errno", f"{app_list} is not running. Please start it."
                )
                return False
        return True


    # Enumerate through gear widgets to highlight them
    try:
        for i in GearsWidget.gear_entry:
            for j, entry in enumerate(getattr(GearsWidget, 'gear_{}_entry'.format(i))):
                GearsWidget.highlight(entry)
    except Exception:
        raise ValueError('Error: Serious error in code - no highlighting of widgets')

    try:
        with open(f'cars/{selected_car}.json', 'r') as f:
            (selected_car[selected_gear_ratio][gear_ratio_set]) = f.read().split(',')
            # load gear ratios
            gear_ratio_combo(selected_car)

        print('Nitto running lets get a going')
    except Exception:
        raise ValueError(f'Erro:', 'Serious issue out the door go to the code')


    def config_last_ratio(gear_ratio_combo, selected_car):
        config = configparser.ConfigParser()
        config_file = os.path.join('scripts', 'configs.ini')
        if os.path.exists(config_file):
            config.read(config_file)
        gear_ratios = {"gear_ratio_set_1": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                       "gear_ratio_set_2": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                       "gear_ratio_set_3": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                       "gear_ratio_set_4": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                       "gear_ratio_set_5": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0]},
        selected_car[gear_ratios[config['last_gear_ratio']['name']]] = gear_ratio_combo.currentData()

        if not os.path.exists('scripts'):
            os.makedirs('scripts')
        with open(config_file, 'w') as f:
            config['last_gear_ratio'] = {'name': gear_ratio_combo.currentText()}
        gear_ratios = {"gear_ratio_set_1": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                       "gear_ratio_set_2": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                       "gear_ratio_set_3": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                       "gear_ratio_set_4": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                       "gear_ratio_set_5": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0]}

    # save the current gear ratio set and car used to the configuration file
    def save_config():
        config['DEFAULT']['last_gear_ratio_set'] = self.gear_ratio_combo.currentText()
        config['DEFAULT']['last_car_used'] = {selected_car} # replace with the current car name
        with open(config_file, 'w') as f:
            config.write(f)

    # connect the save_config function to a signal that is emitted when the program exits
    QtCore.QCoreApplication.aboutToQuit.connect(save_config)