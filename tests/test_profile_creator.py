import unittest
import sys
from unittest.mock import patch
from io import StringIO
from datetime import datetime
from profile_creator import *

class TestCoolProfileCreator(unittest.TestCase):

    @patch("datetime.datetime")
    def test_get_time_of_day(self, mock_datetime):
        mock_datetime.now.return_value.hour = 8
        self.assertEqual(get_time_of_day(), "Good morning")

        mock_datetime.now.return_value.hour = 14
        self.assertEqual(get_time_of_day(), "Good afternoon")

        mock_datetime.now.return_value.hour = 20
        self.assertEqual(get_time_of_day(), "Good evening")

        mock_datetime.now.return_value.hour = 23
        self.assertEqual(get_time_of_day(), "Good night")

    @patch("builtins.input", return_value="Alice")
    def test_get_name(self, mock_input):
        self.assertEqual(get_name(), "Alice")

    @patch("builtins.input", side_effect=["25", "30", "150", "twenty"])
    def test_get_age(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.assertEqual(get_age(), 25)

            self.assertEqual(get_age(), 30)

            get_age()
            self.assertIn("Please enter a valid age (0-120).", fake_output.getvalue())

            get_age()
            self.assertIn("Please enter a number for your age.", fake_output.getvalue())

    @patch("builtins.input", return_value="blue")
    def test_get_favorite_color(self, mock_input):
        self.assertEqual(get_favorite_color(), "blue")

    def test_get_age_fun_fact(self):
        self.assertEqual(get_age_fun_fact(10), "You're still a kid at heart!")
        self.assertEqual(get_age_fun_fact(15), "Ah, the teenage years! Enjoy them!")
        self.assertEqual(get_age_fun_fact(25), "Welcome to adulthood!")
        self.assertEqual(get_age_fun_fact(35), "You're in your prime!")
        self.assertEqual(get_age_fun_fact(60), "Wisdom comes with age!")

    def test_get_color_personality(self):
        self.assertEqual(get_color_personality("blue"), "You're calm and trustworthy!")
        self.assertEqual(get_color_personality("gold"), "You're one of a kind!")

    @patch("sys.stdout", new=StringIO())
    def test_display_color_art(self):
        display_color_art("blue")
        self.assertIn("🌊", sys.stdout.getvalue())

        display_color_art("gold")
        self.assertIn("✨", sys.stdout.getvalue())

    @patch("sys.stdout", new=StringIO())
    def test_display_profile(self):
        display_profile("Alice", 25, "blue")
        output = sys.stdout.getvalue()
        self.assertIn("Good morning, Alice!", output)
        self.assertIn("You are 25 years old. Welcome to adulthood!", output)
        self.assertIn("Your favorite color is blue. You're calm and trustworthy!", output)
        self.assertIn("🌊", output)

    @patch("builtins.input", side_effect=["Bob", "30", "green"])
    def test_edit_profile(self, mock_input):
        name, age, color = edit_profile("Alice", 25, "blue")
        self.assertEqual(name, "Bob")
        self.assertEqual(age, 30)
        self.assertEqual(color, "green")

    @patch("builtins.input", side_effect=["Alice", "25", "blue", "3"])
    def test_main(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            main()
            output = fake_output.getvalue()
            self.assertIn("Welcome to the Cool Profile Creator!", output)
            self.assertIn("Good morning, Alice!", output)
            self.assertIn("You are 25 years old. Welcome to adulthood!", output)
            self.assertIn("Your favorite color is blue. You're calm and trustworthy!", output)
            self.assertIn("🌊", output)

if __name__ == "__main__":
    unittest.main()