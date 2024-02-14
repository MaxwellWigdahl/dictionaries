movie_ratings = { "movies":[
      { "Movie Title": "Inception",
        "Movie Rating": 8.5,
      },
      { "Movie Title": "Interstellar",
        "Movie Rating": 7.5,
      },
      { "Movie Title": "The Dark Knight",
        "Movie Rating": 9,
      },
      { "Movie Title": "The Shawshank Redemption",
        "Movie Rating": 9.5,
      },
      { "Movie Title": "Dunkirk",
        "Movie Rating": 8,
      }

      ]
}

user_movie = input("Enter a movie title: ")

def recommend_movie(movie_ratings, user_movie):
    found = False
    for movie in movie_ratings["movies"]:
        if user_movie == movie["Movie Title"]:
            found = True
            if movie["Movie Rating"] >= 8:
                print("You should watch this movie!")
            else:
                print("This movie is low rated. You might prefer these higher rated movies: ")
                for movie in movie_ratings["movies"]:
                    if movie["Movie Rating"] >= 8:
                        print(f"{movie['Movie Title']}")
            break

    if not found:
        print("This movie could not be found. But check out these other high rated movies: ")
        for movie in movie_ratings["movies"]:
            if movie["Movie Rating"] >= 8:
                print(f"{movie['Movie Title']}")

recommend_movie(movie_ratings, user_movie)
                      
