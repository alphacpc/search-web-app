import csv
rows = []
with open("flights.csv", 'r') as file:
    csvreader = csv.DictReader(file)
    for row in csvreader:

        print("-------HEURE DE DEPART---------")

        heures_dep_prevu = row['SCHEDULED_DEPARTURE'][:2]
        minutes_dep_prevu = row['SCHEDULED_DEPARTURE'][2:]
        heures_dep = row['DEPARTURE_TIME'][:2]
        minutes_dep = row['DEPARTURE_TIME'][2:]

        print("Heure de départ prévu", heures_dep_prevu, ":", minutes_dep_prevu)
        print("Heure de départ", heures_dep_prevu, ":", minutes_dep_prevu)

        
        print("-------HEURE D'ARRIVE---------")


        heures_arr_prevu = row['SCHEDULED_ARRIVAL'][:2]
        minutes_arr_prevu = row['SCHEDULED_ARRIVAL'][2:]
        heures_arr = row['ARRIVAL_TIME'][:2]
        minutes_arr = row['ARRIVAL_TIME'][2:]

        print("Heure d'arrivé prévu", heures_arr_prevu, ":", minutes_arr_prevu)
        print("Heure d'arrivé", heures_arr, ":", minutes_arr)

        print("\n")
        break


def get_aita_code_compagny(code):
    
    compagnies = [
        {"code": "UA", "airline": "United Air Lines Inc" , "image": "./images/united.png" },
        {"code": "AA", "airline": "American Airlines Inc"  , "image": "./images/american-airlines.png" },
        {"code": "US", "airline": "US Airways Inc"  , "image": "./images/us.png" },
        {"code": "F9", "airline": "Frontier Airlines Inc" , "image": "./images/frontier.png" },
        {"code": "B6", "airline": "JetBlue Airways" , "image": "./images/jetblue.png" },
        {"code": "OO", "airline": "Skywest Airlines Inc" , "image": "./images/sktywest.png" },
        {"code": "AS", "airline": "Alaska Airlines Inc" , "image": "./images/alaska.png" },
        {"code": "NK", "airline": "Spirit Air Lines" , "image": "./images/spirit.png" },
        {"code": "WN", "airline": "Southwest Airlines Co" , "image": "./images/southwest.png" },
        {"code": "DL", "airline": "Delta Air Lines Inc" , "image": "./images/delta.png" },
        {"code": "EV", "airline": "Atlantic Southeast Airlines" , "image": "./images/southwest.png" },
        {"code": "HA", "airline": "Hawaiian Airlines Inc" , "image": "./images/hawa.png" },
        {"code": "MQ", "airline": "American Eagle Airlines Inc" , "image": "./images/american-airlines.png" },
        {"code": "VX", "airline": "Virgin America" , "image": "./images/virgini.png" }
    ]