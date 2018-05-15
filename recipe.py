from course import Course
from review import Review

class Recipe:

    def __init__(self, name):
        self._name = name

    @classmethod
    def all(cls):
        return list(set([course.recipe for course in Course.all()]))

    def reviews(self):
        return [review for review in Review.all() if review.recipe == self]

    @classmethod
    def top_three(cls):
        recipes = [recipe for recipe in Recipe.all() if (len(recipe.reviews()) > 0)]
        sorted_recipes = sorted(recipes, key=lambda rec: rec.average_rating(), reverse=True)
        return sorted_recipes[:3]

    @classmethod
    def bottom_three(cls):
        recipes = [recipe for recipe in Recipe.all() if (len(recipe.reviews()) > 0)]
        sorted_recipes = sorted(recipes, key=lambda rec: rec.average_rating())
        return sorted_recipes[:3]

    def average_rating(self):
        if (len(self.reviews()) > 0):
            num_reviews = len(self.reviews())
            total = sum([review.rating for review in self.reviews()])
            return (total/num_reviews)

    def top_five_reviews(self):
        reviews = self.reviews()
        sorted_reviews = Recipe.sort_reviews(reviews)
        return sorted_reviews[:5]

    @classmethod
    def sort_reviews(cls, list_reviews):
        return sorted(list_reviews, key=lambda review: review.rating)

    def _name():
        doc = "The _name property."
        def fget(self):
            return self.__name
        def fset(self, value):
            self.__name = value
        def fdel(self):
            del self.__name
        return locals()
    _name = property(**_name())
