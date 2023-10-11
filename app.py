import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/albums', methods=['POST'])
def post_album():
    if has_invalid_album_parameters(request.form):
        return "You need to summit a title, release_year, and artist_id", 400
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(
        None,
        request.form['title'],
        request.form['release_year'],
        request.form['artist_id'])
    repository.create(album)
    return '', 200

def has_invalid_album_parameters(form):
    return 'title' not in form or \
        'release_year' not in form \
        or 'artist_id' not in form

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    respository = AlbumRepository(connection)
    return "\n".join(
        f"{album}" for album in respository.all()
    )





# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
# @app.route('/emoji', methods=['GET'])
# def get_emoji():
#     return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

