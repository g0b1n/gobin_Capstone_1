import requests
from secrets_1 import apiKey

# My API key
api_key = apiKey

## Trending Movies
def trendingMvi(query):
    """Return multiple media types (movies, TV shows, and people) in a single call to get the most trending data on the entirety of TMDB."""

    api_url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={api_key}&query={query}&include_adult=false&language=en-US"

    headers = {
        "accept": "application/json",
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

## Trending Shows
# def trendingTv(query):
#     """Return multiple media types (movies, TV shows, and people) in a single call to get the most trending data on the entirety of TMDB."""

#     api_url = f"https://api.themoviedb.org/3/trending/tv/day?api_key={api_key}&query={query}&include_adult=false&language=en-US"

#     headers = {
#         "accept": "application/json",
#     }

#     try:
#         response = requests.get(api_url, headers=headers)
#         response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
#         return response.json()
#     except requests.RequestException as e:
#         print(f"An error occurred: {e}")
#         return None


## Search
def fetch_movie_data(query, api_key):
    """
    Fetch movie data from TMDb API based on the query.
    :param query: Search term for the movie.
    :param api_key: API key for TMDb.
    :return: JSON response with movie data or None in case of an error.
    """
    api_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}&include_adult=false&language=en-US&page=1"
    headers = {
        "accept": "application/json",
        # "Authorization": f"Bearer {api_key}"
    }
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code.
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


## MOVIE DETAILS
def get_movie_details(movie_id, api_key):
    """Get details about a paticular movie"""
    api_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    headers = {
        "accept": "application/json",
    }
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code.
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def get_movie_cast(movie_id, api_key):
    api_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}&language=en-US"

    headers = {
        "accept": "application/json",
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code.
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None



## Trending Shows
def trendingPerson(query):
    """Return multiple media types (movies, TV shows, and people) in a single call to get the most trending data on the entirety of TMDB."""

    api_url = f"https://api.themoviedb.org/3/trending/person/day?api_key={api_key}&query={query}&include_adult=false&language=en-US"

    headers = {
        "accept": "application/json",
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def person_details(person_id, api_key):
    """fetch details about celebs"""

    api_url = f"https://api.themoviedb.org/3/person/{person_id}?api_key={api_key}&language=en-US"

    headers = {
        "accept": "application/json"
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        json_response = response.json()
        print(json_response)
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

## Movies done by actors
def get_known_for(person_id, api_key):
    api_url = f"https://api.themoviedb.org/3/person/{person_id}/movie_credits?api_key={api_key}&language=en-US"

    headers = {
        "accept": "application/json",
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None




# def add_to_fav(user_id, movie_id, api_key):
#     """API call to add movies to favorite"""
#     api_url = f"https://api.themoviedb.org/3/account/{user_id}/favorite"

#     headers = {
#         "accept": "application/json",
#         "content-type": "application/json",
#     }

#     payload = {
#         "media_type": "movie",
#         "media_id": movie_id,
#         "favorite": True  # Correct the typo in "favorite"
#     }

#     try:
#         response = requests.post(api_url, headers=headers, params={"api_key": api_key}, json=payload)
#         response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
#         return response.json()
#     except requests.RequestException as e:
#         print(f"An error occurred: {e}")
#         return None


# # Search peoples
# def search_people(query, api_key):
#     """Search for people"""
#     api_url = f"https://api.themoviedb.org/3/search/person?query={query}&api_key={api_key}include_adult=false&language=en-US&page=1"

#     headers = {
#         "accept": "application/json",
#     }

#     try:
#         response = requests.get(api_url, headers=headers)
#         response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
#         return response.json()
#     except requests.RequestException as e:
#         print(f"An error occurred: {e}")
#         return None

def get_movie_reviews(movie_id, api_key):
    """Get the user reviews for a movie."""
    
    api_url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews?api_key={api_key}&language=en-US&page=1"

    headers = {
        "accept": "application/json",
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None
