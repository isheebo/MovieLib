from movie_rental.genre import Genre


class Movie:
    """
    Represents a picture recording that is commonly available
    in DVD rental shops
    duration - running time of a movie in minutes
    """

    def __init__(self, title, duration, genre, release_year, actors=[]):
        self.title = title
        self.duration = duration
        self.genre = genre if issubclass(genre, Genre) else None
        self.release_year = release_year
        self.__actors = actors

    def actors(self):
        return self.__actors