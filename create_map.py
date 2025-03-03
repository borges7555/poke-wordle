import csv

def create_map_from_csv() -> list:
    with open("pokemon_db.csv", mode='r') as file:
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