import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ODQ3MWFmZmQyNTExNTY3MDRlYmFiMDQ4ZDJjMjYzZSIsInN1YiI6IjYxZWMwODgzZTQ4ODYwMDAxZWZjYzkyZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.3YVUZhOArR8Hs3kyY9z-70j60oaepKWKkuVDPyQtkLg"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()
