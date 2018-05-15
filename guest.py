from invite import Invite
from review import Review

class Guest:

    def __init__(self, name):
        self._name = name

    def name():
        doc = "The name property."
        def fget(self):
            return self._name
        def fset(self, value):
            self._name = value
        def fdel(self):
            del self._name
        return locals()
    name = property(**name())

    @classmethod
    def all(cls):
        return list(set([invite.guest for invite in Invite.all()]))

    def invites(self):
        return [invite for invite in Invite.all() if invite.guest == self]

    def reviews(self):
        return [review for review in Review.all() if review.reviewer == self]

    def number_of_invites(self):
        return len(self.invites())

    def rsvp(self, invite, status):
        invite.accepted = status
        return invite.accepted

    def review_recipe(self, recipe, rating, comment):
        new_review = Review(self, recipe, rating, comment)
        return recipe.reviews()

    def favorite_recipe(self):
        sorted_reviews = sorted(self.reviews(), key=lambda review: review.rating, reverse=True)
        fav_recipe = sorted_reviews[0].recipe
        return fav_recipe

    @classmethod
    def most_popular(cls):
        all_guests = cls.all()
        sorted_guests = sorted(all_guests, key=lambda guest: len(guest.invites()), reverse=True)
        return sorted_guests[0]

    @classmethod
    def toughest_critic(cls):
        all_guests = cls.all()
        sorted_by_critiques = sorted(all_guests, key=lambda guest: guest.average_rating())
        return sorted_by_critiques[0]

    @classmethod
    def most_active_critic(cls):
        all_guests = cls.all()
        sorted_by_critiques = sorted(all_guests, key=lambda guest: len(guest.reviews()), reverse=True)
        return sorted_by_critiques[0]

    def average_rating(self):
        reviews = self.reviews()
        num_reviews = len(self.reviews())
        total = sum([review.rating for review in self.reviews()])
        return (total/num_reviews)
