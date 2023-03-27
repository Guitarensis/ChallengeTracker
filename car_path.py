import os
from data_path import data_folder

cars = [f for f in os.listdir(data_folder) if f.endswith('.json')]