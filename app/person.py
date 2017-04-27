from abc import ABCMeta

from .room import Office, LivingSpace
from .utility import generate_id, Storage


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

        # Update program storage and counters; while remembering to check for duplicates first
        people_names = [person.name for person in Storage.people]
        already_seen = set(people_names)
        if name in already_seen:
            raise TypeError('{} already added'.format(name))
        Storage.people.append(self)

        Person.people_total += 1

    def allocate_office(self):
        """Method used to allocate an office to a person"""
        office_instance = self.select_random_room()
        self.office_assigned = office_instance
        office_instance.assignees_count += 1
        print(
            '{} has been allocated the {} {}'.format(self.name.split()[0], Office.room_type, self.office_assigned.name))

    def select_random_room(self, room_type=''):
        """
        Instance method that uses a simple algorithm to randomise the room assigned. It will return a the first 
        room encountered that is not full yet, or create one if no such room exists
        """
        room_count = len(Storage.rooms)
        if room_count > 0:
            for room in Storage.rooms:
                if room_type != '':
                    if room.room_type == room_type and room.assignees_count < room.capacity:
                        return room
                else:
                    if room.assignees_count < room.capacity:
                        return room

        # Either no rooms yet, or all that exist are full; in any case, create a new one
        if LivingSpace.room_type == room_type:
            return LivingSpace('Random #{}'.format(LivingSpace.rooms_total + 1))
        else:
            return Office('Random #{}'.format(Office.rooms_total + 1))


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

        self.allocate_office()
        self.allocate_living_space(wants_accommodation)

    def allocate_living_space(self, wants_accommodation):
        if 'Y' == wants_accommodation:
            living_space_instance = self.select_random_room(LivingSpace.room_type)
            if living_space_instance.assignees_count < Office.capacity:
                self.living_space_assigned = living_space_instance
                living_space_instance.assignees_count += 1
            print('{} has been allocated the {} {}'.format(self.name.split()[0], LivingSpace.room_type,
                                                           self.living_space_assigned.name))


class Staff(Person):
    """
    A sub-class of Person; Staff at the Dojo
    """

    person_type = 'Staff'

    def __init__(self, name):
        super().__init__(name)
        print('{} {} has been successfully added.'.format(Staff.person_type, name))

        self.allocate_office()
