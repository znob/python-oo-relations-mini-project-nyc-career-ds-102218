class Invite:

    _all = []

    def __init__(self, dinner_party, guest):
        self._accepted = None
        self._guest = guest
        self._dinner_party = dinner_party
        Invite._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    def accepted():
        doc = "The accepted property."
        def fget(self):
            return self._accepted
        def fset(self, value):
            self._accepted = value
        def fdel(self):
            del self._accepted
        return locals()
    accepted = property(**accepted())

    def guest():
        doc = "The guest property."
        def fget(self):
            return self._guest
        def fset(self, value):
            self._guest = value
        def fdel(self):
            del self._guest
        return locals()
    guest = property(**guest())

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
