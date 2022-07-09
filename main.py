import csv

flights = []
flights_fields = ["NUM_FLIGHT", "DEPART_PREVU", "DEPART", "ARRIVE_PREVU", "ARRIVE", "DATE" , "DATE_FORMATED", "AIRLINE", "AIRLINE_PHOTO", "ORIGIN_AIRPORT", "DESTINATION_AIRPORT" , "DISTANCE"]

def get_airline(code):
    with open("./data/airlines.csv", 'r') as file:
        csvreader = csv.DictReader(file)
        return [item for item in csvreader if item.get('IATA_CODE') == code][0]


def get_airport(airport):
    with open("./data/airports.csv", 'r') as file:
        csvreader = csv.DictReader(file)
        
        result = [item for item in csvreader if item.get('IATA_CODE') == airport]

        return result[0] if len(result) > 0 else None
        # return [item for item in csvreader if item.get('IATA_CODE') == airport][0]


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



with open("./data/flights.csv", 'r') as file:
    csvreader = csv.DictReader(file)

    for row in csvreader:

        origin_airport = get_airport(row['ORIGIN_AIRPORT'])
        destination_airport = get_airport(row['DESTINATION_AIRPORT'])

        flight = {
            "NUM_FLIGHT" : row['FLIGHT_NUMBER'],
            "DEPART_PREVU" : row['SCHEDULED_DEPARTURE'][:2] + ":" + row['SCHEDULED_DEPARTURE'][2:], 
            "DEPART" : row['DEPARTURE_TIME'][:2] + ":" + row['DEPARTURE_TIME'][2:],
            "ARRIVE_PREVU" : row['SCHEDULED_ARRIVAL'][:2] + ":" + row['SCHEDULED_ARRIVAL'][2:], 
            "ARRIVE" : row['ARRIVAL_TIME'][:2] + ":" + row['ARRIVAL_TIME'][2:], 
            "DATE" : "{}.{}.{}".format(row['DAY'], row['MONTH'], row['YEAR']), 
            "DATE_FORMATED" : "Le {} {}, {}".format(row['DAY'], get_month(row['MONTH']), row['YEAR']), 
            "AIRLINE" : get_airline(row['AIRLINE'])['AIRLINE'], 
            "AIRLINE_PHOTO" : get_airline(row['AIRLINE'])['IMAGE'], 
            "ORIGIN_AIRPORT" : origin_airport.get('CITY') if origin_airport != None else None,
            "DESTINATION_AIRPORT" : destination_airport.get('CITY') if destination_airport != None else None,
            "DISTANCE" : row['DISTANCE']
        }

        flights.append(flight)

        break



with open("flights_transformed.csv", "w", encoding="UTF8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames = flights_fields)
    writer.writeheader()
    writer.writerows(flights)

