
import requests

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ODQ3MWFmZmQyNTExNTY3MDRlYmFiMDQ4ZDJjMjYzZSIsInN1YiI6IjYxZWMwODgzZTQ4ODYwMDAxZWZjYzkyZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.3YVUZhOArR8Hs3kyY9z-70j60oaepKWKkuVDPyQtkLg"

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_popular_movies(list_type):
    endpoint = f"https://api.themoviedb.org/4/list/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_poster_url(poster_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}{poster_path}"


#https://image.tmdb.org/t/p/w342/1Rr5SrvHxMXHu5RjKpaMba8VTzi.jpg


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_one_url(backdrop_path, size="w780"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}{backdrop_path}"

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_actor_url(profile_path, size="w780"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}{profile_path}"



