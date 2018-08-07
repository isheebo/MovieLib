import unittest

from fixtures.movies import sample_movie_list

class BaseTestCase(unittest.TestCase):
    def add_movies_to_a_library(self, movie_lib):
        for each_movie_details in sample_movie_list:
            movie_lib.add_movie(**each_movie_details)

            

