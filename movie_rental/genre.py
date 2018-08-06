class Genre:
    """
    Defines the genre of the movie.
    For now this can be Adventure, Thriller, Horror, Romance, Comedy etc.
    """

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Romance(Genre):
    def __init__(self):
        super(self.__class__, self).__init__(
            self.__class__.__name__, "Disguised Chilli sauce/peppe"
        )


class Adventure(Genre):
    def __init__(self):
        super(Adventure, self).__init__(
            self.__class__.__name__,
            "Walks in parks is all"
        )


class Horror(Genre):
    def __init__(self):
        super(Horror, self).__init__(
            self.__class__.__name__,
            "Good enough to test whether your boyfriend is a coward"
        )


class Thriller(Genre):
    def __init__(self):
        super(Thriller, self).__init__(
            self.__class__.__name__,
            "The kind that keeps you at the edge of your seat"
        )


class Comedy(Genre):
    def __init__(self):
        super(Comedy, self).__init__(
            self.__class__.__name__,
            "Laughter is for the heart"
        )
