import unittest2 as unittest
import sys
sys.path.insert(0, '..')
from driver import Driver
from trip import Trip
from owner import Owner
from car import Car

class TestOneToManyRelationships(unittest.TestCase):

    global driver_1
    driver_1 = Driver("Dwight Schrute")
    global trip_1
    trip_1 = Trip("11 Broadway, NY, NY", "123 Smith Street, BK, NY", driver_1)
    global trip_2
    trip_2 = Trip("Pier 11 Ferry", "Battery Park", driver_1)
    global trip_3
    trip_3 = Trip("Wall Street", "Lincoln Center", driver_1)

    global owner_1
    owner_1 = Owner("Michael Scott", 38)
    global car_1
    car_1 = Car("Ford", "Aerostar Minivan", 1997, owner_1)
    global car_2
    car_2 = Car("Toyota", "Corolla", 2000, owner_1)
    global car_3
    car_3 = Car ("Chrysler", "300C", 2008, owner_1)

    def test_owner_property_methods(self):
        self.assertEqual(owner_1._name, "Michael Scott")
        self.assertEqual(owner_1.name, "Michael Scott")
        self.assertEqual(owner_1._age, 38)
        self.assertEqual(owner_1.age, 38)

    def test_driver_property_methods(self):
        self.assertEqual(driver_1._name, "Dwight Schrute")
        self.assertEqual(driver_1.name, "Dwight Schrute")

    def test_car_property_methods(self):
        self.assertEqual(car_1._make, "Ford")
        self.assertEqual(car_1.make, "Ford")
        self.assertEqual(car_1._model, "Aerostar Minivan")
        self.assertEqual(car_1.model, "Aerostar Minivan")
        self.assertEqual(car_1._year, 1997)
        self.assertEqual(car_1.year, 1997)
        self.assertEqual(car_1._owner, owner_1)
        self.assertEqual(car_1.owner, owner_1)

    def test_trip_property_methods(self):
        self.assertEqual(trip_3._start, "Wall Street")
        self.assertEqual(trip_3.start, "Wall Street")
        self.assertEqual(trip_3._destination, "Lincoln Center")
        self.assertEqual(trip_3.destination, "Lincoln Center")
        self.assertEqual(trip_3._driver, driver_1)
        self.assertEqual(trip_3.driver, driver_1)

    def test_car_class_method(self):
        self.assertItemsEqual(Car._all, [car_1, car_2, car_3])
        self.assertItemsEqual(Car.all(), [car_1, car_2, car_3])

    def test_trip_class_method(self):
        self.assertItemsEqual(Trip._all, [trip_1, trip_2, trip_3])
        self.assertItemsEqual(Trip.all(), [trip_1, trip_2, trip_3])

    def test_find_my_cars_instance_method(self):
        self.assertItemsEqual(owner_1.find_my_cars(), ["Ford Aerostar Minivan", "Toyota Corolla", "Chrysler 300C"])

    def test_my_trips_instance_method(self):
        self.assertItemsEqual(driver_1.my_trips(), [trip_1, trip_2, trip_3])

    def test_find_my_cars_instance_method(self):
        self.assertItemsEqual(driver_1.my_trip_summaries(), ["11 Broadway, NY, NY to 123 Smith Street, BK, NY", "Pier 11 Ferry to Battery Park", "Wall Street to Lincoln Center"])
