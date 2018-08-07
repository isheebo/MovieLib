class Genre:
    """
    Defines the genre of the movie.
    For now this can be Adventure, Thriller, Horror, Romance, Comedy etc.
    """

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __eq__(self, comparator):
        return self.name == comparator.name and self.description == comparator.description


class Romance(Genre):
    def __init__(self):
        super().__init__(
            self.__class__.__name__, "Disguised Chilli sauce/peppe"
        )


class Adventure(Genre):
    def __init__(self):
        super().__init__(
            self.__class__.__name__,
            "Walks in parks is all"
        )


class Horror(Genre):
    def __init__(self):
        super().__init__(
            self.__class__.__name__,
            "Good enough to test whether your boyfriend is a coward"
        )


class Thriller(Genre):
    def __init__(self):
        super().__init__(
            self.__class__.__name__,
            "The kind that keeps you at the edge of your seat"
        )


class Comedy(Genre):
    def __init__(self):
        super().__init__(
            self.__class__.__name__,
            "Laughter is for the heart"
        )
