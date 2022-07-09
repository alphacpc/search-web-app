import csv

def get_airline(code):
    with open("airlines.csv", 'r') as file:
        csvreader = csv.DictReader(file)
        return [item for item in csvreader if item.get('IATA_CODE') == code][0]


def get_airport(airport):
    with open("airports.csv", 'r') as file:
        csvreader = csv.DictReader(file)
        return [item for item in csvreader if item.get('IATA_CODE') == airport][0]

def get_month(num):
    months = [
        {"id": 1, "month": "Janvier"}, {"id": 2, "month": "Février"},
        {"id": 3, "month": "Mars"}, {"id": 4, "month": "Avril"},
        {"id": 5, "month": "Mais"}, {"id": 6, "month": "Juin"},
        {"id": 7, "month": "Juillet"}, {"id": 8, "month": "Aout"},
        {"id": 9, "month": "Septembre"}, {"id": 10, "month": "Octobre"},
        {"id": 11, "month": "Novembre"}, {"id": 12, "month": "Décembre"},
    ]
    return [month for month in months if month.get('id') == int(num)][0]['month']



with open("flights.csv", 'r') as file:
    csvreader = csv.DictReader(file)
    for row in csvreader:

        print("-------HEURE DE DEPART---------")
        heures_dep_prevu = row['SCHEDULED_DEPARTURE'][:2]
        minutes_dep_prevu = row['SCHEDULED_DEPARTURE'][2:]
        heures_dep = row['DEPARTURE_TIME'][:2]
        minutes_dep = row['DEPARTURE_TIME'][2:]
       
        print("-------HEURE D'ARRIVEE---------")
        heures_arr_prevu = row['SCHEDULED_ARRIVAL'][:2]
        minutes_arr_prevu = row['SCHEDULED_ARRIVAL'][2:]
        time_arr_prevu = row['SCHEDULED_ARRIVAL'][:2] + ":" + row['SCHEDULED_ARRIVAL'][2:]
        print(time_arr_prevu)

        heures_arr = row['ARRIVAL_TIME'][:2]
        minutes_arr = row['ARRIVAL_TIME'][2:]
        time_arr = row['ARRIVAL_TIME'][:2] + ":" + row['ARRIVAL_TIME'][2:]

        print(time_arr)

        print("-------VOL INFOS---------")
        name_airline = get_airline(row['AIRLINE'])['AIRLINE']
        image_airline = get_airline(row['AIRLINE'])['IMAGE']
        origin_airport = get_airport(row['ORIGIN_AIRPORT'])['CITY']
        destination_airport = get_airport(row['DESTINATION_AIRPORT'])['CITY']

        month = get_month(row['MONTH'])
        distance = row['DISTANCE']
        year = row['YEAR']
        day = row['DAY']
        filght_number = row['FLIGHT_NUMBER']



        break