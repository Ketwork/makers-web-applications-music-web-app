# Single Table Design Recipe Template

_Copy this recipe template to design and create a database table from a specification._

    # Request:
    POST /albums

    # With body parameters:
    title=Voyage
    release_year=2022
    artist_id=2

    # Expected response (200 OK)
    (No content)

  Your test should assert that the new album is present in the list of records returned by GET /albums.


    # Request:
    GET /artists

    # Expected response (200 OK)
    Pixies, ABBA, Taylor Swift, Nina Simone

    # Request:
    POST /artists

    # With body parameters:
    name=Wild nothing
    genre=Indie

    # Expected response (200 OK)
    (No content)

    # Then subsequent request:
    GET /artists

    # Expected response (200 OK)
    Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing

## 1. Extract nouns from the user stories or specification



```
Nouns:

album, title, release year, artist, genre, id
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| album                 | id, title, release year, artist_id |
| artist                | id, name, genre

Name of the table (always plural): `albums`

Column names: `title`, `release_year`, `aritist_id`, `id`

Name of the table (always plural): `artists`

Column names: `name`, `genre`

## 3. Decide the column types


```

id: SERIAL
title: text
release_year: int
artist_id: int

id: SERIAL
name: text
genre: text
```

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    genre VARCHAR(255)
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Fsingle_table_design_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Fsingle_table_design_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Fsingle_table_design_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Fsingle_table_design_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Fsingle_table_design_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
