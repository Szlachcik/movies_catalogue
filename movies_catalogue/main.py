from flask import Flask, render_template
import tmdb_client
from flask import request

app = Flask(__name__)


@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', "1")
    movies = tmdb_client.get_popular_movies(list_type=selected_list)["results"][:8]
    return render_template("homepage.html", movies=movies, current_list=selected_list)



@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.context_processor
def processor():
    def tmdb_one_url(path, size="w780"):
        return tmdb_client.get_one_url(path, size)
    return {"tmdb_one_url": tmdb_one_url}

@app.context_processor
def processor_actor():
    def tmdb_actor_url(path, size="w185"):
        return tmdb_client.get_actor_url(path, size)
    return {"tmdb_one_url": tmdb_actor_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
   details = tmdb_client.get_single_movie(movie_id)
   cast = tmdb_client.get_single_movie_cast(movie_id)
   return render_template("movie_details.html", movie=details, cast=cast)

if __name__ == "__main__":
    app.run(debug=True)

