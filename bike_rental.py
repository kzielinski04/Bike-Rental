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