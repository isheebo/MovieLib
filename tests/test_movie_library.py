from tests import BaseTestCase
from movie_rental.library import MovieLibrary, Movie, GenreError
from movie_rental.genre import Thriller

class MovieLibraryTestCases(BaseTestCase):
    def setUp(self):
        self.movie_library = MovieLibrary()
        self.sample_movie_details = {
            'title':'Mission Impossible: Fall Out',
            'duration': 147,
            'genre': Thriller(),
            'release_year':'2018',
            'actors': ['Tom Cruiz', 'Simon Pegg', 'Ving Rymes', 'Rebecca Fergusson']
        }

    def test_can_add_movie_to_the_library(self):
        movie_title = self.sample_movie_details['title'].lower()
        self.movie_library.add_movie(**self.sample_movie_details)
        self.assertIn(movie_title, self.movie_library.all_movie_titles)
        self.assertEqual(self.movie_library.movie_count[movie_title], 1)

    def test_cant_add_movie_with_invalid_genre(self):
        movie_details = self.sample_movie_details
        movie_details['genre'] = "Bad Genre"
        self.assertRaises(GenreError, self.movie_library.add_movie, **movie_details)

        # this test can as well be written like this
        with self.assertRaises(GenreError):
            self.movie_library.add_movie(**movie_details)
        

    def test_movies_are_stored_as_movie_instances(self):
        self.movie_library.add_movie(**self.sample_movie_details)
        self.assertIsInstance(self.movie_library.get_movie_by_title(self.sample_movie_details['title'].lower()), Movie)
    
    def can_get_movie_by_title(self):
        """ Tests whether we get None if no movie exists with that title or the movie if it exists """
        movie_title = self.sample_movie_details['title'].lower()
        # access a movie before adding one to the lib
        self.assertIsNone(self.movie_library.get_movie_by_title(movie_title))
        
        # add movie and test whether we can get it by title
        self.movie_library.add_movie(**self.sample_movie_details)
        self.assertTrue(movie_title == self.movie_library.get_movie_by_title(movie_title)['title'])

    def test_can_get_movies_released_in_a_year(self):
        # try getting movies in 2018 and get back an empty list
        movies_2018 = self.movie_library.movies_released_in('2018')
        self.assertEqual(len(movies_2018), 0)

        # add some movies to the library
        self.add_movies_to_a_library(self.movie_library)
        # get all movies by the year 2018
        movies_2018 = self.movie_library.movies_released_in('2018')
        self.assertEqual(len(movies_2018), 2)

    def test_can_rent_out_movie(self):
        pass

    def test_cant_rent_out_an_out_of_stock_movie(self):
        # try renting out a movie that doesnt exist
        movie_rented = self.movie_library.rent_out_movie('How I met your mother')
        self.assertFalse(movie_rented)

        # create a single movie, rent it out and test whether the second attempt fails
        movie_title = self.sample_movie_details.get('title')
        self.movie_library.add_movie(**self.sample_movie_details)
        first_rented = self.movie_library.rent_out_movie(movie_title)
        self.assertTrue(first_rented)
        second_rented = self.movie_library.rent_out_movie(movie_title)
        self.assertFalse(second_rented)
    
    def test_can_get_movies_by_genre(self):
        # try with no movies and get back an empty list
        thrillers = self.movie_library.movies_with_genre(Thriller())
        self.assertEqual(thrillers, [])

        # add some movies and get thrillers
        # the movies we are adding have two thrillers i.e 'mission impossibles and bourne'
        expected_thrillers = ['mission impossible: fall out', 'bourne']
        self.add_movies_to_a_library(self.movie_library)
        thrillers = self.movie_library.movies_with_genre(Thriller())
        self.assertEqual(thrillers, expected_thrillers)

    def test_cant_get_movie_by_genre_with_invalid_genre(self):
        with self.assertRaises(GenreError):
            self.movie_library.movies_with_genre('Bad Genre')


    
    def test_can_delete_a_movie(self):
        pass

    def can_edit_a_movie(self):
        pass
    
    def cant_edit_movie_that_doesnt_exist(self):
        pass

    def tearDown(self):
        self.movie_library = None