from movie_rental.movie import Movie
import unittest


class TestMovie(unittest.TestCase):
    def setUp(self):
        self.movie = Movie(
            'Pirates of the Carribean 1',
            '157min',
            'Comedy',
            2003
        )

    def test_movie_is_created_successfully(self):
        self.assertEqual(self.movie.title, 'Pirates of the Carribean 1')
