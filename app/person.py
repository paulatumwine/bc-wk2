from abc import ABCMeta

from .room import Office, LivingSpace
from .utility import generate_id


class Person(object):
    """
    A base class for the different kinds of people accommodated at the Dojo
    """

    __metaclass__ = ABCMeta

    people_total = 0

    def __init__(self, name):
        try:
            if isinstance(int(name), int):
                raise TypeError('name should not be an integer')
        except ValueError:
            pass

        if not isinstance(name, str):
            raise TypeError('name should be a string')

        self.id = generate_id()
        self.name = name

        # TODO: Randomise the room selection later...for now, just create a new one
        office_instance = Office('Random')
        if office_instance.assignees_count < Office.capacity:
            self.office_assigned = office_instance
            office_instance.assignees_count += 1
            print(
                '{} has been allocated the {} {}'.format(name.split()[0], Office.room_type, self.office_assigned.name))

        Person.people_total += 1


class Fellow(Person):
    """
    A sub-class of Person; a Fellow accepted into the Dojo
    """

    person_type = 'Fellow'

    def __init__(self, name, wants_accommodation='N'):
        if wants_accommodation not in ['Y', 'N']:
            raise TypeError('second argument should be one of \'Y\' or \'N\'')

        super().__init__(name)
        print('{} {} has been successfully added.'.format(Fellow.person_type, name))

        if 'Y' == wants_accommodation:
            living_space_instance = LivingSpace('Random')
            if living_space_instance.assignees_count < Office.capacity:
                self.living_space_assigned = living_space_instance
                living_space_instance.assignees_count += 1
            print('{} has been allocated the {} {}'.format(name.split()[0], LivingSpace.room_type,
                                                           self.living_space_assigned.name))


class Staff(Person):
    """
    A sub-class of Person; Staff at the Dojo
    """

    person_type = 'Staff'

    def __init__(self, name):
        super().__init__(name)
        print('{} {} has been successfully added.'.format(Staff.person_type, name))
