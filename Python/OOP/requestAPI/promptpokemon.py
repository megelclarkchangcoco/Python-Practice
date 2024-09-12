# How to connect to an API using Python
from http.client import responses
from operator import truediv

# Importing the requests library to make HTTP requests
import requests

# Base URL for the PokeAPI
base_url = "https://pokeapi.co/api/v2/"

# Function to get Pokemon information by name
def get_pokemon_info(name):
    # Construct the URL for the specific Pokemon
    url = f"{base_url}/pokemon/{name}"
    # Make a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        pokemon_data = response.json()
        return pokemon_data
    else:
        # Print an error message if the request failed
        print(f"Failed to retrieve data {response.status_code}")

# Function to start the program
def start():
    # Infinite loop to keep asking for Pokemon info
    while True:
        # Prompt the user to enter a Pokemon name
        pokemon_name = input("Enter the Pokemon name you want info about: ")
        # Get the Pokemon information
        pokemon_info = get_pokemon_info(pokemon_name)

        # Check if the Pokemon information was retrieved successfully
        if pokemon_info:
            # Print the Pokemon's name, ID, height, and weight
            print(f"Name  : {pokemon_info['name'].capitalize()}")
            print(f"ID    : {pokemon_info['id']}")
            print(f"Height: {pokemon_info['height']}")
            print(f"Weight: {pokemon_info['weight']}")
            print()
        else:
            # Print an error message if the Pokemon name is invalid
            print(f"{pokemon_name} is Invalid")

        # Ask the user if they want to try again
        choice = input("Do you want to try again? (Yes (y) or No (n)): ").lower()

        # Check the user's choice
        if choice == "n" or choice == "no":
            # Exit the loop if the user chooses 'No'
            break

# Call the start function to run the program
start()


