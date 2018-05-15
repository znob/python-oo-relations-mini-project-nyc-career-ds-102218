
class Review:

    _all = []

    def __init__(self, reviewer, recipe, rating, comment):
        self._rating = rating
        self._recipe = recipe
        self._reviewer = reviewer
        self._comment = comment
        Review._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    def rating():
        doc = "The rating property."
        def fget(self):
            return self._rating
        def fset(self, value):
            self._rating = value
        def fdel(self):
            del self._rating
        return locals()
    rating = property(**rating())

    def recipe():
        doc = "The recipe property."
        def fget(self):
            return self._recipe
        def fset(self, value):
            self._recipe = value
        def fdel(self):
            del self._recipe
        return locals()
    recipe = property(**recipe())

    def reviewer():
        doc = "The reviewer property."
        def fget(self):
            return self._reviewer
        def fset(self, value):
            self._reviewer = value
        def fdel(self):
            del self._reviewer
        return locals()
    reviewer = property(**reviewer())

    def comment():
        doc = "The comment property."
        def fget(self):
            return self._comment
        def fset(self, value):
            self._comment = value
        def fdel(self):
            del self._comment
        return locals()
    comment = property(**comment())
