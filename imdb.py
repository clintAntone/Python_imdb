import requests

# API Key for The Movie Database (TMDb)
api_key = '978c4b53e738933e48df999ba45deca6'

# Base URL for TMDb API
base_url = 'https://api.themoviedb.org/3/movie/'

# Endpoints
now_playing_endpoint = 'now_playing'
top_rated_endpoint = 'top_rated'

# Function to retrieve latest movie
def get_latest_movies():
    # Full URL for the request
    url = f'{base_url}{now_playing_endpoint}?api_key={api_key}&language=en-US&page=1'

    # Make a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Load the JSON response data into a dictionary
        data = response.json()

        # Get the top 10 latest movies
        latest_movies = data['results'][:10]

        # Print the title and background information of each movie
        for i, movie in enumerate(latest_movies):
            print(f'{i + 1}. Title: {movie["title"]}')
            print(f'Background: {movie["overview"]}')
            print()
    else:
        # Print an error message if the request was unsuccessful
        print(f'An error occurred: {response.status_code}')

# Function to retrieve the top 10 most recommended movies
def get_top_rated_movies():
    # Full URL for the request
    url = f'{base_url}{top_rated_endpoint}?api_key={api_key}&language=en-US&page=1'

    # Make a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Load the JSON response data into a dictionary
        data = response.json()

        # Get the top 10 most recommended movies
        top_movies = data['results'][:10]

        # Print the title and background information of each movie
        for i, movie in enumerate(top_movies):
            print(f'{i + 1}. Title: {movie["title"]}')
            print(f'Background: {movie["overview"]}')
            print()
    else:
        # Print an error message if the request was unsuccessful
        print(f'An error occurred: {response.status_code}')

# Main function
def main():
    while True:
        print('===================================================')
        print('[1] Top 10 Latest Movies')
        print('[2] Top 10 Recommended Movies')
        print('[3] End the program')
        choice = int(input('Enter your choice: '))
        print('===================================================')
        if choice == 1:
            get_latest_movies()
        elif choice == 2:
            get_top_rated_movies()
        elif choice == 3:
            print('Ending program...')
            break       
        else:
            print('Invalid choice')

# Call the main function
if __name__ == '__main__':
    main()







