from movie_rental.genre import Genre
from movie_rental.movie import Movie


class MovieLibrary:
    """
    Represents a DVD Rental store, and all the operations that the
    owner of the store can do.
    """

    def __init__(self):
        # if we are adding a movie that already exists, we would want to see
        # its count incremented.
        # if doesn't exist, we would like to add it for the very first time
        self.movie_count = dict()  # { title: count }
        self.movies = dict()  # { title: Movie() }
        # since movies and movie_count should not be directly accessed from the
        # outer scope, we can make them private

    def add_movie(self, title, duration, genre, release_year, actors=[]):
        title = title.lower()
        movie = Movie(title, duration, genre, release_year, actors)

        if title in self.movies:
            self.movie_count[title] += 1
        else:
            self.movie_count[title] = 1
            self.movies[title] = movie

        return self.movies

    def edit_movie(self, title, duration, genre, release_year, actors):
        title = title.lower()

        if title not in self.movies:
            return False

        movie = self.movies[title]
        movie.duration = duration
        movie.genre = genre
        movie.release_year = release_year
        movie.set_actors(actors)
        return True

    def delete_movie_entry(self, title):
        title = title.lower()  # should be done from the caller's side

        if title not in self.movies:
            return False

        del self.movies[title]
        del self.movie_count[title]

        return True

    def all_movie_titles(self):
        return [title for title in self.movies]

    def rent_out_movie(self, title):
        title = title.lower()

        if title not in self.movie_count or self.movie_count[title] < 1:
            return False

        self.movie_count[title] -= 1
        return True

    def movies_with_genre(self, genre):
        if issubclass(genre, Genre):
            return [mv.title for mv in self.movies if mv.genre == genre]
        return []  # fail silently

    def movies_with_title(self, title):
        """
        This method would be implemented if we weren't using titles
        for keys to the storage dictionary
        """
        pass

    def movies_released_in(self, year):
        movies_for_year = []

        for movie in self.movies.values():
            if movie.year == year:
                movies_for_year.append(movie)  # extract titles later

        return [movie.title for movie in movies_for_year]
