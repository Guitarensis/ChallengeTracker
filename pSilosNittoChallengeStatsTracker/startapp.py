# this script is used to start the application
from carcombo import selected_car
from dictionary import load_dataframes, gear_ratio_set
import geardropdownframe as GearsWidget, selected_gear_ratio, gear_ratio_combo
from IPython.external.qt_for_kernel import QtCore
import configparser
import keyboard
import os
import psutil


# List of applications that need to be running
app_list = ['1320v200.exe', '1320v200Scalable.exe', '1320v200Scalable60.exe']

# Load dataframes
load_dataframes()

def check_app_running(app_list):
    for proc in psutil.process_iter(['name']):
        if app_list in proc.info['name']:
            return True
        else:
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
                raise ValueError(f'Error:', 'Serious issue out the door go to the code')
            print("Errno", f"{app_list} is not running. Please start it.")
    return False


# Function to start the application
def start():
    # Check for saved gear ratios
    check_app_running(app_list)
    config = configparser.ConfigParser()
    config_file = os.path.join('scripts', 'configs.ini')
    if os.path.exists(config_file):
        config.read(config_file)
        last_gear_ratio_name = config.get('last_gear_ratio', 'name', fallback=None)
        if last_gear_ratio_name is not None:
            # combo_box needs to be defined in this scope or passed as an argument
            gear_ratio_index = gear_ratio_combo.findText(last_gear_ratio_name)
            if gear_ratio_index != -1:
                gear_ratio_combo.setCurrentIndex(gear_ratio_index)

    # Save last geat ratio that is currently selected for next time
    def config_last_ratio(selected_car):
        config = configparser.ConfigParser()
        config_file = os.path.join('scripts', 'configs.ini')
        if os.path.exists(config_file):
            config.read(config_file)
        selected_car[gear_ratio_set[config['last_gear_ratio']['name']]] = gear_ratio_combo.currentData()

        if not os.path.exists('scripts'):
            os.makedirs('scripts')
        with open(config_file, 'w') as file:
            config['last_gear_ratio'] = {'name': gear_ratio_combo.currentText()}

    # save the current gear ratio set and car used to the configuration file
    def save_config():
        config_last_ratio(selected_car)
        config['DEFAULT']['last_gear_ratio_set'] = gear_ratio_combo.currentText()
        config['DEFAULT']['last_car_used'] = selected_car  # replace with the current car name
        with open(config_file, 'w') as file:
            config.write(file)

    # connect the save_config function to a signal that is emitted when the program exits
    QtCore.QCoreApplication.aboutToQuit.connect(save_config)
