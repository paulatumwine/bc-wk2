import sys
import unittest
from io import StringIO

from app.room import *
from app.person import *


class RoomTests(unittest.TestCase):
    """
    Unit tests for the Room class and its descendants
    """

    def test_add_office_successfully(self):
        """
        Test successful office addition
        """
        initial_room_count = Room.rooms_total
        office_instance = Office('Office')
        self.assertIsInstance(office_instance, Office, msg='Object should be an instance of the `Office` class')
        final_room_count = Room.rooms_total
        self.assertEqual(final_room_count - initial_room_count, 1, msg='Total count should have increased by one')

    def test_add_living_space_successfully(self):
        """
        Test successful living space addition
        """
        initial_room_count = Room.rooms_total
        living_space_instance = LivingSpace('LivingSpace')
        self.assertIsInstance(living_space_instance, LivingSpace,
                              msg='Object should be an instance of the `LivingSpace` class')
        final_room_count = Room.rooms_total
        self.assertEqual(final_room_count - initial_room_count, 1, msg='Total count should have increased by one')

    def test_office_valid_instantiation(self):
        """
        Tests that the Office constructor only accepts a single string argument
        """
        self.assertRaises(TypeError, Office, 1)
        self.assertRaises(TypeError, Office, [])
        self.assertRaises(TypeError, Office, '12')
        self.assertRaises(TypeError, Office, 1, 2)
        self.assertRaises(TypeError, Office, '12', 'Office')

    def test_living_space_valid_instantiation(self):
        """
        Tests that the LivingSpace constructor only accepts a single string argument
        """
        self.assertRaises(TypeError, LivingSpace, 1)
        self.assertRaises(TypeError, LivingSpace, [])
        self.assertRaises(TypeError, LivingSpace, '12')
        self.assertRaises(TypeError, LivingSpace, 1, 2)
        self.assertRaises(TypeError, LivingSpace, '12', 'Office')

    def test_add_office_output_is_valid(self):
        """
        Tests that office addition outputs to stdout content in the expected format
        """
        captured_stdout = sys.stdout
        try:
            sys.stdout = StringIO()
            captured_stdout = sys.stdout
            Office('OfficeOne')
            output = sys.stdout.getvalue().strip()
            self.assertEquals(output, 'An office called OfficeOne has been successfully created!')
        finally:
            sys.stdout = captured_stdout

    def test_add_living_space_output_is_valid(self):
        """
        Tests that living space addition outputs to stdout content in the expected format
        """
        captured_stdout = sys.stdout
        try:
            sys.stdout = StringIO()
            LivingSpace('LivingSpaceOne')
            output = sys.stdout.getvalue().strip()
            self.assertEquals(output, 'A livingspace called LivingSpaceOne has been successfully created!')
        finally:
            sys.stdout = captured_stdout

    def test_addition_of_duplicate_room(self):
        """
        Test to ensure no duplicate rooms are added to the app
        """
        room_zero = Office('RandomZero')
        self.assertIsInstance(room_zero, Office, msg='Object should be an instance of the `Office` class')
        self.assertRaises(TypeError, Office, 'RandomZero')
        room_one = LivingSpace('RandomSpace')
        self.assertIsInstance(room_one, LivingSpace, msg='Object should be an instance of the `LivingSpace` class')
        self.assertRaises(TypeError, LivingSpace, 'RandomSpace')

    def test_printing_occupants_of_non_existent_room(self):
        """Raise an error if a room that does not exist is provided"""
        self.assertRaises(TypeError, Room.print_room_occupants, 'RandomOne')

    def test_printing_allocations_successfully(self):
        """Test that all allocations are able to be printed successfully"""
        staff_zero = Staff('Deal Jackson')
        captured_stdout = sys.stdout
        try:
            sys.stdout = StringIO()
            Room.print_allocations()
            output = sys.stdout.getvalue().strip()
            self.assertIn('Deal Jackson', output)
        finally:
            sys.stdout = captured_stdout
