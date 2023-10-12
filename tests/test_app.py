
"""
When I call GET /albums
I get a list of albums back
"""
def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/record_Store.sql")
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Album(1, Doolittle, 1989, 1)"


"""
When I call POST /albums with album info
That album is now in the list in GET /albums
"""
def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/record_Store.sql")
    post_response = web_client.post("/albums", data={
        'title': 'In Ear Park',
        'release_year': '2008',
        'artist_id': '2'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, Doolittle, 1989, 1)\n" \
        "Album(2, In Ear Park, 2008, 2)"

def test_post_albums_with_no_data(db_connection, web_client):
    db_connection.seed("seeds/record_Store.sql")
    post_response = web_client.post("/albums")
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == "" \
        "You need to summit a title, release_year, and artist_id"
    
    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, Doolittle, 1989, 1)"


def test_list_all_artists(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone'

def test_create_artist(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/artists", data={
        'name': 'Wild nothing',
        'genre': 'Indie'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing'

