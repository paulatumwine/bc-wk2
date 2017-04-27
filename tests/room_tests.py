import sys
import unittest
from io import StringIO

from app.room import *
from app.person import *
from app.utility import *


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

    def test_reallocate_arguments_are_valid(self):
        """Tests that the reallocate method only accepts string arguments"""
        self.assertRaises(TypeError, Room.reallocate_person, 1)
        self.assertRaises(TypeError, Room.reallocate_person, '', [])
        self.assertRaises(TypeError, Room.reallocate_person, '12')
        self.assertRaises(TypeError, Room.reallocate_person, 1, 2)
        self.assertRaises(TypeError, Room.reallocate_person, '12', 'Office')

    def test_can_reallocate_person_successfully(self):
        """Test that a person can be reallocated successfully"""
        initial_room_name = Storage.people[0].office_assigned.name
        for room in Storage.rooms:
            if room.name != initial_room_name:
                room_to_assign = room
                break
        Room.reallocate_person(Storage.people[0].name, room_to_assign.name)
        if room_to_assign.room_type == Office.room_type:
            final_room_name = Storage.people[0].office_assigned.name
        elif room_to_assign.room_type == LivingSpace.room_type:
            final_room_name = Storage.people[0].living_space_assigned.name
        self.assertNotEqual(initial_room_name, final_room_name, msg='Person not reassigned to different room')

    def test_try_reallocation_of_person_that_does_not_exist(self):
        """Test that only persons that exist can be reallocated"""
        self.assertRaises(RuntimeError, Room.reallocate_person, 'Keele Jackson', 'RandomZero')  # inexistent person

    def test_try_reallocation_to_room_that_does_not_exist(self):
        """Test that only rooms that exist can be reallocated"""
        self.assertRaises(RuntimeError, Room.reallocate_person, 'Reel Jackson', 'RandomTen')  # inexistent room
