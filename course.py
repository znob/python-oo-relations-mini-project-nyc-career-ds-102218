class Course:

    _all = []

    def __init__(self, dinner_party, recipe):
        self._dinner_party = dinner_party
        self._recipe = recipe
        Course._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    def dinner_party():
        doc = "The dinner_party property."
        def fget(self):
            return self._dinner_party
        def fset(self, value):
            self._dinner_party = value
        def fdel(self):
            del self._dinner_party
        return locals()
    dinner_party = property(**dinner_party())

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
