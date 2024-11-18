import json, datetime, smtplib, os

#Function that calculates cost of rental
def calculate_cost(rental_duration:int)->int:
    match rental_duration:
        case 1:
            return 10
        case _:
            return 10 + (5 * (rental_duration - 1))