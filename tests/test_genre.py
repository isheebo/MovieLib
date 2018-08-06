import unittest

from movie_rental.genre import Comedy, Horror


class TestGenre(unittest.TestCase):
    """
    use instances of movies with these genres to test these.
    e.g. create the movie PiratesOfTheCarribean with genre `Adventure`
    and test to ensure it genre is Adventure
    """

    def setUp(self):
        self.horror = Horror()
        self.comedy = Comedy()

    def test_horror_has_genre_horror(self):
        self.assertEqual(self.horror.name, 'Horror')
        self.assertEqual(
            self.horror.description,
            "Good enough to test whether your boyfriend is a coward")

    def test_comedy_has_genre_comedy(self):
        self.assertEqual(self.comedy.name, 'Comedy')
