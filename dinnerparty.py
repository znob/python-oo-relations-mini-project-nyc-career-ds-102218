from invite import Invite
from course import Course

class DinnerParty:

    def __init__(self, name):
        self._name = name

    @classmethod
    def all(cls):
        return list(set([invite.dinner_party for invite in Invite.all()]))

    def invites(self):
        return [invite for invite in Invite.all() if invite.dinner_party == self]

    def guests(self):
        invites = self.invites()
        guests = [invite.guest for invite in invites]
        return guests

    def number_of_attendees(self):
        attendees = [invite.guest for invite in self.invites() if invite.accepted]
        return len(attendees)

    def courses(self):
        return [course for course in Course.all() if course.dinner_party == self]

    def recipes(self):
        courses = self.courses()
        return [course.recipe for course in courses]

    def recipe_count(self):
        return len(self.recipes())

    def highest_rated_recipe(self):
        all_reviews = self.reviews()
        sorted_reviews = sorted(all_reviews, key=lambda review: review.rating, reverse=True)
        return sorted_reviews[0].recipe

    def reviews(self):
        recipes = self.recipes()
        reviews = [recipe.reviews() for recipe in recipes]
        flattened = sum(reviews, [])
        return flattened
