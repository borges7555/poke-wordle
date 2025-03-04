import csv
import os
import sys

def get_file_path(filename):
    """Get the correct path for data files in PyInstaller."""
    if getattr(sys, 'frozen', False):  # Running as an executable
        base_path = sys._MEIPASS  # The temporary folder PyInstaller uses
    else:
        base_path = os.path.dirname(__file__)  # Normal execution, use current directory

    return os.path.join(base_path, filename)

def create_map_from_csv() -> list:
    path = get_file_path("pokemon_db.csv")
    with open(path, mode='r', encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        data_map = []
        for row in csv_reader:
            row[3] = int(row[3])  # Generation
            row[4] = int(row[4])  # HP
            row[5] = int(row[5])  # Att
            row[6] = int(row[6])  # Def
            row[7] = int(row[7])  # Spa
            row[8] = int(row[8])  # Spd
            row[9] = int(row[9])  # Spe
            data_map.append(row)
    return data_map
