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
        Storage.rooms.append(self)
        Room.rooms_total += 1


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
