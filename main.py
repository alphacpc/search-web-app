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

        # print("-------HEURE DE DEPART---------")
        # time_dep_prevu = row['SCHEDULED_DEPARTURE'][:2] + ":" + row['SCHEDULED_DEPARTURE'][2:]
        # time_dep = row['DEPARTURE_TIME'][:2] + ":" + row['DEPARTURE_TIME'][2:]
       
        # print("-------HEURE D'ARRIVEE---------")
        # time_arr_prevu = row['SCHEDULED_ARRIVAL'][:2] + ":" + row['SCHEDULED_ARRIVAL'][2:]
        # time_arr = row['ARRIVAL_TIME'][:2] + ":" + row['ARRIVAL_TIME'][2:]

        # print("-------VOL INFOS---------")
        # name_airline = get_airline(row['AIRLINE'])['AIRLINE']
        # image_airline = get_airline(row['AIRLINE'])['IMAGE']
        # origin_airport = get_airport(row['ORIGIN_AIRPORT'])['CITY']
        # destination_airport = get_airport(row['DESTINATION_AIRPORT'])['CITY']


        # flight_date_formated = "Le {} {}, {}".format(row['DAY'], get_month(row['MONTH']), row['YEAR'])
        # flight_date = "{}.{}.{}".format(row['DAY'], row['MONTH'], row['YEAR'])

        flight = {
            "NUM_FLIGHT" : row['FLIGHT_NUMBER'],
            "DEPART_PREVU" : time_dep_prevu, 
            "DEPART" : time_dep,
            "ARRIVE_PREVU" : time_arr_prevu, 
            "ARRIVE" : time_arr, 
            "DATE" : flight_date, 
            "DATE_FORMATED" : flight_date_formated, 
            "AIRLINE" : name_airline, 
            "AIRLINE_PHOTO" : image_airline, 
            "ORIGIN_AIRPORT" : origin_airport, 
            "DESTINATION_AIRPORT" : destination_airport,
            "DISTANCE" : row['DISTANCE']
        }

        

        break