from lib.album import Album

"""
Constructs with an id, title, release date, and artist id
"""
def test_album_constructs():
    album = Album(1, "Test Title", 2000, 2)
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 2000
    assert album.artist_id == 2

"""
Albums with equal contents are equal
"""
def test_books_are_equal():
    album_1 = Album(1, "Test Title", 2000, 2)
    album_2 = Album(1, "Test Title", 2000, 2)
    assert album_1 == album_2

"""
We can format albumss to strings
"""
def test_albums_format_nicely():
    album = Album(1, "Test Title", 2000, 2)
    assert str(album) == "Album(1, Test Title, 2000, 2)"

