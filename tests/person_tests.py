import sys
import unittest

from ..app.person import Person


class TestAddPerson(unittest.TestCase):
    """
    Unit tests for the add_person method of the Person class
    """

    def setUp(self):
        self.person_instance = Person()

    def test_add_person_successfully(self):
        """
        Tests that person is added successfully
        """
        initial_person_count = len(self.person_instance.all_people)
        person_zero = self.person_instance.add_person('Phil Jackson', 'Staff')
        self.assertTrue(person_zero)
        new_person_count = len(self.room_instance.all_people)
        self.assertEqual(new_person_count - initial_person_count, 1)

    def test_add_person_arguments(self):
        """
        Test that add_person only accepts string arguments
        """
        self.assertRaises(ValueError, self.person_instance.add_person(1))
        self.assertRaises(ValueError, self.person_instance.add_person(1, 2))
        self.assertRaises(ValueError, self.person_instance.add_person('Blue', 2))
        self.assertRaises(ValueError, self.person_instance.add_person(1, 'Office'))
        self.assertRaises(ValueError, self.person_instance.add_person('1', 'Office'))
        self.assertRaises(ValueError, self.person_instance.add_person('Orange', '2'))
        self.assertRaises(ValueError, self.person_instance.add_person('Orange', '2', 1))
        self.assertRaises(ValueError, self.person_instance.add_person('Orange', '2', []))

    def test_add_person_takes_only_specific_args(self):
        """
        Tests that the second and third arguments accept only pre-specified arguments
        """
        self.assertRaises(ValueError, self.person_instance.add_person('Orange', 'Black'))
        self.assertRaises(ValueError, self.person_instance.add_person('Orange', 'Fellow', 'Black'))

    def test_add_person_output_is_valid(self):
        """
        Tests that the add_person method outputs content in the expected format
        """
        captured_stdout = sys.stdout
        try:
            self.add_person.create_room('James Patterson', 'Fellow', 'Y')
            output = sys.stdout.getvalue().strip()
            self.assertContains(output, 'successfully added.')
            self.assertContains(output, 'allocated')
        finally:
            sys.stdout = captured_stdout
