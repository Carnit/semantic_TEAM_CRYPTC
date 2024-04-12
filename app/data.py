import requests

# Define your API token
TOKEN = "1cXcZZ1r5ir9fHWX_KGUaVazygGUl0xiZIZbFyW8_Ag"

# Define the base URL for the Trefle API
BASE_URL = "https://trefle.io/api/v1/"

# Define the endpoint to fetch plants data
PLANTS_ENDPOINT = "plants"


def fetch_plants_data():
    # Construct the request URL with the endpoint and token
    url = BASE_URL + PLANTS_ENDPOINT + "?token=" + TOKEN

    try:
        # Send a GET request to the Trefle API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the plant data
            return data
        else:
            # If the request was not successful, print the error message
            print("Error:", response.status_code)
            return None
    except Exception as e:
        # If an error occurs during the request, print the error message
        print("An error occurred:", str(e))
        return None


# Fetch plants data from the Trefle API
plants_data = fetch_plants_data()

# Print the fetched data (you can modify this according to your needs)
print(plants_data)
