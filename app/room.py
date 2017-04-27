from abc import ABCMeta

from .utility import generate_id, Storage


class Room(object):
    """
    Abstract class for all the different types of rooms in the Dojo
    """

    __metaclass__ = ABCMeta

    rooms_total = 0

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
        self.assignees_count = 0

        # Update program storage and counters; while remembering to check for duplicates first
        room_names = [room.name for room in Storage.rooms]
        already_seen = set(room_names)
        if name in already_seen:
            raise TypeError('{} already added'.format(name))
        Storage.rooms.append(self)

        Room.rooms_total += 1

    @staticmethod
    def print_room_occupants(name):
        room_names = [room.name for room in Storage.rooms]
        present_rooms = set(room_names)
        if name not in present_rooms:
            raise TypeError('{} does not exist'.format(name))

        occupants = [person.name for person in Storage.people if
                     person.office_assigned.name == name or person.living_space_assigned == name]
        if len(occupants) == 0:
            print('{} has no occupants yet'.format(name))

        for occupant in occupants:
            print(occupant)


class Office(Room):
    """
    Sub-class of Room; an office at the Dojo
    """

    capacity = 6
    room_type = 'office'

    def __init__(self, name):
        super().__init__(name)
        print('An {} called {} has been successfully created!'.format(Office.room_type, name))


class LivingSpace(Room):
    """
    A sub-class of Room; a living space at the Dojo
    """

    capacity = 4
    room_type = 'livingspace'

    def __init__(self, name):
        super().__init__(name)
        print('A {} called {} has been successfully created!'.format(LivingSpace.room_type, name))
