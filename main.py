print("Welcome to Day Trip Generator! If you would like assistance with your travels we can help!")

import random

destinations = ["Buffalo","New York City","Cleveland","Toronto","Syracuse"]

def random_item_picker(list):
    random_item = random.choice(list)
    return random_item 

def user_destination_confirmation():
    random_destination = random_item_picker(destinations)
    user_input = input(f'We have selected {random_destination} as your destination. Would you like to keep this choice? y/n ')
    if user_input == "y":
        print(f"Great! Let's move onto the next option.")
        return random_destination
    elif user_input == "n":
        print(f"If that is not your prefered choice lets try again!")
        return user_destination_confirmation()

confirmed_destination = user_destination_confirmation()

restaurants = ["Ricci's", "Rohrbachs", "Anchor Bar", "DaVinci's", "Pelicans Nest"]

def random_item_picker(list):
    random_item = random.choice(list)
    return random_item 

def user_restaurant_confirmation():
    random_restaurant = random_item_picker(restaurants)
    user_input = input(f'We have selected {random_restaurant} as your dining location for this evening. Would you like to keep this choice? y/n ')
    if user_input == "y":
        return random_restaurant
        print(f"Great! Let's move onto the next option.")
    elif user_input == "n":
        print(f"If that is not your prefered choice lets try again!")
        return user_restaurant_confirmation()   

confirmed_restaurant = user_restaurant_confirmation()

transportation = ["car", "subway", "horseback", "train", "limousine"]

def random_item_picker(list):
    random_item = random.choice(list)
    return random_item 

def user_transportation_confirmation():
    random_transportation = random_item_picker(transportation)
    user_input = input(f'The mode of travel will by {random_transportation} for your trip today. Would you like to keep this choice? y/n ')
    if user_input == "y":
        print(f"Great! Let's move onto the next option.")
        return random_transportation
    elif user_input == "n":
        print(f"If that is not your prefered choice lets try again!")
        return user_transportation_confirmation()   

confirmed_transportation = user_transportation_confirmation()

entertainment = ["movies", "amphitheater", "pool hall ", "dance hall", "karaoke bar"]

def random_item_picker(list):
    random_item = random.choice(list)
    return random_item 

def user_entertainment_confirmation():
    random_entertainment = random_item_picker(entertainment)
    user_input = input(f'The entertainment for this evening will be at the {random_entertainment}. Would you like to keep this choice? y/n ')
    if user_input == "y":
        print(f"Great! Let's move onto the next option.")
        return random_entertainment
    elif user_input == "n":
        print(f"If that is not your prefered choice lets try again!")
        return user_entertainment_confirmation()   

confirmed_entertainment = user_entertainment_confirmation()

print("This is the trip we have planned for you.")
print(f"Destination: " + confirmed_destination)
print(f"Transportation: " + confirmed_transportation)
print("Restaurant: " + confirmed_restaurant)
print("Entertainment: " + confirmed_entertainment)

booked = ["confirmed"]
user_decision = booked

def customer_confirmed():
    user_verify = (input(f"Would you like to finalize your day trip? y/n "))
    if user_verify == "y":
        print(f"I hope you are excited for todays journey! You will be traveling to {confirmed_destination} by {confirmed_transportation}, where you will enjoy a meal at {confirmed_restaurant}. Lastly, you will have some fun at the {confirmed_entertainment}!!")
        return (user_decision)
    elif user_verify == "n":
        print("Let review things.")
        return (user_decision)

closed_deal = customer_confirmed()

print(f"Congratulations you have booked a day trip!!")


