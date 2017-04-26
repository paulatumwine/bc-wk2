import sys
import unittest

from ..app.room import Room


class TestCreateRoom(unittest.TestCase):
    """
    Unit tests for the create_room method in the Room class
    """

    def setUp(self):
        self.room_instance = Room()

    def test_create_room_successfully(self):
        """
        Tests successful room creation
        """
        initial_room_count = len(self.room_instance.all_rooms)
        blue_office = self.room_instance.create_room('Blue', 'Office')
        self.assertTrue(blue_office)
        new_room_count = len(self.room_instance.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_room_arguments(self):
        """
        Tests if either or both of the arguments to the create_room method is not a string
        """
        self.assertRaises(ValueError, self.room_instance.create_room(1))
        self.assertRaises(ValueError, self.room_instance.create_room(1, 2))
        self.assertRaises(ValueError, self.room_instance.create_room('Blue', 2))
        self.assertRaises(ValueError, self.room_instance.create_room(1, 'Office'))
        self.assertRaises(ValueError, self.room_instance.create_room('1', 'Office'))
        self.assertRaises(ValueError, self.room_instance.create_room('Orange', '2'))

    def test_create_room_takes_only_specific_args(self):
        """
        Tests if second argument is a valid room type
        """
        self.assertRaises(ValueError, self.room_instance.create_room('Orange', 'Black'))

    def test_create_room_output_is_valid(self):
        """
        Tests that the create_room method outputs content in the expected format
        """
        captured_stdout = sys.stdout
        try:
            self.room_instance.create_room('Blue', 'Office')
            output = sys.stdout.getvalue().strip()
            self.assertContains(output, 'successfully created!')
        finally:
            sys.stdout = captured_stdout
