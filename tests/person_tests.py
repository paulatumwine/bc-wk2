import sys
import unittest
from io import StringIO

"""
As a note on imports; probably only to my future self... using something like:

from ..app.person import *

Will get rid of the IDE errors in PyCharm, but when running from the top-level dir at 
runtime, it will not resolve the path ..app. Instead, it will be expecting something like:

from app.person import *

at runtime, even though this gives errors in the IDE.
"""
from app.person import *


# noinspection PyUnresolvedReferences
class PersonTests(unittest.TestCase):
    """
    Unit tests for the Person class and all its descendants
    """

    def test_add_staff_successfully(self):
        """
        Tests that staff is added successfully
        """
        initial_person_count = Person.people_total
        suspect_zero = Staff('Phil Jackson')
        self.assertIsInstance(suspect_zero, Staff, msg='Object should be an instance of the `Staff` class')
        final_person_count = Person.people_total
        self.assertEqual(final_person_count - initial_person_count, 1, msg='Total count should have increased by one')

    def test_add_fellow_successfully(self):
        """
        Tests that a fellow is added successfully
        """
        initial_person_count = Person.people_total
        suspect_zero = Fellow('Jill Jackson')
        self.assertIsInstance(suspect_zero, Fellow, msg='Object should be an instance of the `Fellow` class')
        half_way_person_count = Person.people_total
        self.assertEqual(half_way_person_count - initial_person_count, 1,
                         msg='Total count should have increased by one')
        suspect_one = Fellow('Jill Jackson', 'Y')
        self.assertIsInstance(suspect_one, Fellow, msg='Object should be an instance of the `Fellow` class')
        final_person_count = Person.people_total
        self.assertEqual(final_person_count - half_way_person_count, 1, msg='Total count should have increased by one')

    def test_staff_constructor_arguments(self):
        """
        Test that the Staff constructor only accepts a single string argument
        """
        self.assertRaises(TypeError, Staff, 1)
        self.assertRaises(TypeError, Staff, [])
        self.assertRaises(TypeError, Staff, '12')
        self.assertRaises(TypeError, Staff, 1, 2)
        self.assertRaises(TypeError, Staff, '12', 'Office')

    def test_fellow_constructor_arguments(self):
        """
        Test that the Fellow constructor accepts at least one and at most two string arguments
        """
        self.assertRaises(TypeError, Fellow, 1)
        self.assertRaises(TypeError, Fellow, [])
        self.assertRaises(TypeError, Fellow, '12')
        self.assertRaises(TypeError, Fellow, 1, 2, 3)

    def test_fellow_constructor_second_arguments(self):
        """
        Test that the Fellow constructor's second argument is one of either 'Y' or 'N'
        """
        self.assertRaises(TypeError, Fellow, 'Name', 'Other')

    def test_add_staff_output_is_valid(self):
        """
        Tests that the staff addition outputs to stdout content in the expected format
        """
        captured_stdout = sys.stdout
        try:
            sys.stdout = StringIO()
            Staff('Reel Jackson')
            output = sys.stdout.getvalue().strip()
            self.assertIn('Staff Reel Jackson has been successfully added.', output)
            self.assertIn('Reel has been allocated the office', output)
        finally:
            sys.stdout = captured_stdout

    def test_add_fellow_output_is_valid(self):
        """
        Tests that the staff addition outputs to stdout content in the expected format
        """
        captured_stdout = sys.stdout
        try:
            sys.stdout = StringIO()
            Fellow('Peele Jackson', 'Y')
            output = sys.stdout.getvalue().strip()
            self.assertIn('Fellow Peele Jackson has been successfully added.', output)
            self.assertIn('Peele has been allocated the office', output)
            self.assertIn('Peele has been allocated the livingspace', output)
        finally:
            sys.stdout = captured_stdout
