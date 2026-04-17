"""
Unit Tests for the MealTracker class.

These tests verify that the MealTracker methods work correctly.
Run them with:
    python -m unittest test_calories.py -v

All tests will FAIL until you implement the methods in calories_calculator.py.
Your goal: make all tests pass (green)!

What is a unit test?
    A unit test checks that a small piece of code (a "unit", e.g. a method)
    behaves as expected. We call the method with known inputs and check
    that the output matches what we expect using "assertions".

What is unittest?
    unittest is Python's built-in testing framework. It comes with Python,
    so you don't need to install anything extra. You write test methods
    inside a class that inherits from unittest.TestCase.

How to read a test:
    def test_something(self):
        # 1. ARRANGE – set up the objects and data
        tracker = MealTracker()

        # 2. ACT – call the method you want to test
        result = tracker.some_method()

        # 3. ASSERT – check that the result is what you expect
        self.assertEqual(result, expected_value)
"""

import unittest

# Import the MealTracker class from our main file.
# This works because both files are in the same folder.
from calories_calculator import MealTracker


class TestAddMeal(unittest.TestCase):
    """Tests for the add_meal() method."""

    def test_add_single_meal(self):
        """After adding one meal, the meals list should contain one item."""
        tracker = MealTracker()

        tracker.add_meal("Breakfast", 450)

        # len() returns the number of items in a list.
        self.assertEqual(len(tracker.meals), 1)

    def test_add_meal_stores_correct_name(self):
        """The stored meal should have the correct name."""
        tracker = MealTracker()

        tracker.add_meal("Breakfast", 450)

        # tracker.meals[0] is the first item in the list.
        # It should be a dict with key "name".
        self.assertEqual(tracker.meals[0]["name"], "Breakfast")

    def test_add_meal_stores_correct_calories(self):
        """The stored meal should have the correct calorie count."""
        tracker = MealTracker()

        tracker.add_meal("Breakfast", 450)

        self.assertEqual(tracker.meals[0]["calories"], 450)

    def test_add_multiple_meals(self):
        """Adding multiple meals should increase the list length."""
        tracker = MealTracker()

        tracker.add_meal("Breakfast", 450)
        tracker.add_meal("Lunch", 700)
        tracker.add_meal("Dinner", 600)

        self.assertEqual(len(tracker.meals), 3)

    def test_add_meal_preserves_order(self):
        """Meals should be stored in the order they were added."""
        tracker = MealTracker()

        tracker.add_meal("Breakfast", 450)
        tracker.add_meal("Lunch", 700)

        self.assertEqual(tracker.meals[0]["name"], "Breakfast")
        self.assertEqual(tracker.meals[1]["name"], "Lunch")


class TestGetTotalCalories(unittest.TestCase):
    """Tests for the get_total_calories() method."""

    def test_total_no_meals(self):
        """Total calories should be 0 when no meals have been added."""
        tracker = MealTracker()

        result = tracker.get_total_calories()

        self.assertEqual(result, 0)

    def test_total_single_meal(self):
        """Total should equal the calories of the single meal."""
        tracker = MealTracker()
        tracker.add_meal("Breakfast", 450)

        result = tracker.get_total_calories()

        self.assertEqual(result, 450)

    def test_total_multiple_meals(self):
        """Total should be the sum of all meal calories."""
        tracker = MealTracker()
        tracker.add_meal("Breakfast", 450)
        tracker.add_meal("Lunch", 700)
        tracker.add_meal("Dinner", 600)

        result = tracker.get_total_calories()

        self.assertEqual(result, 1750)

    def test_total_with_zero_calorie_meal(self):
        """A meal with 0 calories should not affect the total."""
        tracker = MealTracker()
        tracker.add_meal("Water", 0)
        tracker.add_meal("Lunch", 700)

        result = tracker.get_total_calories()

        self.assertEqual(result, 700)


class TestGetMealsSummary(unittest.TestCase):
    """Tests for the get_meals_summary() method."""

    def test_summary_no_meals(self):
        """Summary should be an empty list when no meals exist."""
        tracker = MealTracker()

        result = tracker.get_meals_summary()

        self.assertEqual(result, [])

    def test_summary_single_meal_format(self):
        """Each summary line should follow the format 'Name - Calories kcal'."""
        tracker = MealTracker()
        tracker.add_meal("Breakfast", 450)

        result = tracker.get_meals_summary()

        self.assertEqual(result[0], "Breakfast - 450 kcal")

    def test_summary_multiple_meals(self):
        """Summary should contain one line per meal."""
        tracker = MealTracker()
        tracker.add_meal("Breakfast", 450)
        tracker.add_meal("Lunch", 700)

        result = tracker.get_meals_summary()

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "Breakfast - 450 kcal")
        self.assertEqual(result[1], "Lunch - 700 kcal")

    def test_summary_returns_list(self):
        """The return type should be a list."""
        tracker = MealTracker()
        tracker.add_meal("Snack", 150)

        result = tracker.get_meals_summary()

        self.assertIsInstance(result, list)


class TestResetDay(unittest.TestCase):
    """Tests for the reset_day() method."""

    def test_reset_clears_meals(self):
        """After reset, the meals list should be empty."""
        tracker = MealTracker()
        tracker.add_meal("Breakfast", 450)
        tracker.add_meal("Lunch", 700)

        tracker.reset_day()

        self.assertEqual(len(tracker.meals), 0)

    def test_reset_then_total_is_zero(self):
        """After reset, total calories should be 0."""
        tracker = MealTracker()
        tracker.add_meal("Breakfast", 450)

        tracker.reset_day()
        result = tracker.get_total_calories()

        self.assertEqual(result, 0)

    def test_reset_then_add_new_meal(self):
        """After reset, we should be able to add new meals normally."""
        tracker = MealTracker()
        tracker.add_meal("Breakfast", 450)

        tracker.reset_day()
        tracker.add_meal("New Breakfast", 300)

        self.assertEqual(len(tracker.meals), 1)
        self.assertEqual(tracker.meals[0]["name"], "New Breakfast")


# =============================================================================
# This runs all tests when you execute: python -m unittest test_calories.py -v
# The -v flag means "verbose" – it shows each test name and its result.
# =============================================================================
if __name__ == "__main__":
    unittest.main()
