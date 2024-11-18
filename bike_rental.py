import json, datetime, smtplib, os

#Function that calculates cost of rental
def calculate_cost(rental_duration:int)->int:
    match rental_duration:
        case 1:
            return 10
        case rental_duration if isinstance(rental_duration, int) == False:
            print("Rental duration must be an integer!\n")
        case rental_duration if rental_duration <= 0:
            print("Invalid rental duration!\n")
        case _:
            return 10 + (5 * (rental_duration - 1))

#Function that lets user rent a bike for a certain duration
def rent_bike(customer_name:str, rental_duration:int)->list:
    rental = []
    match rental_duration:
        case rental_duration if isinstance(rental_duration, int) == False:
            print("Rental duration must be an integer!\n")
        case rental_duration if rental_duration <= 0:
            print("Invalid rental duration!\n")
        case _: 
            print(f"The cost of renting a bike for {rental_duration} hours is equal to {calculate_cost(rental_duration)} PLN.")
            rental.append(customer_name)
            rental.append(rental_duration)
            rental.append(calculate_cost(rental_duration))
            save_rental(rental)
        
def save_rental(rental:list):
    file = open("./data/rentals.json", "w")
    json.dump(rental, file)
    file.close()