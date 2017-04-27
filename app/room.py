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

        office_occupants = [person.name for person in Storage.people if person.office_assigned.name == name]
        living_space_occupants = [person.name for person in Storage.people if
                                  (hasattr(person,
                                           'living_space_assigned') and person.living_space_assigned.name == name)]
        occupants = office_occupants + living_space_occupants

        if len(occupants) == 0:
            print('{} has no occupants yet'.format(name))

        for occupant in occupants:
            print(occupant)

    @staticmethod
    def print_allocations(filename=''):
        if len(Storage.rooms) == 0:
            raise RuntimeError('no rooms in the system yet')

        output = ''
        for room in Storage.rooms:
            output += '{}\n'.format(room.name)
            output += '-------------------------------------\n'
            office_occupants = [person.name for person in Storage.people if person.office_assigned.name == room.name]
            living_space_occupants = [person.name for person in Storage.people if
                                      (hasattr(person,
                                               'living_space_assigned') and person.living_space_assigned.name == room.name)]
            occupants = office_occupants + living_space_occupants
            for occupant in occupants:
                output += occupant
                if occupant != occupants[-1]:
                    output += ", "
            output += '\n\n'

        if filename != '':
            file_handle = open(filename, 'w')
            file_handle.write(output)
            file_handle.close()
        else:
            print(output, end='')

    @staticmethod
    def print_unallocated(filename=''):
        unallocated_persons = [person.name for person in Storage.people if
                               person.office_assigned is None or
                               (hasattr(person, 'living_space_assigned') and person.living_space_assigned is None)]

        if len(unallocated_persons) == 0:
            raise RuntimeError('no unallocated persons present')

        output = ''
        for person in unallocated_persons:
            output += '{}\n'.format(person.name)

        if filename != '':
            file_handle = open(filename, 'w')
            file_handle.write(output)
            file_handle.close()
        else:
            print(output, end='')

    @staticmethod
    def reallocate_person(person_name, room_name):
        try:
            if isinstance(int(person_name), int) or isinstance(int(room_name), int):
                raise TypeError('no argument should be an integer')
        except ValueError:
            pass
        if not isinstance(person_name, str) or not isinstance(room_name, str):
            raise TypeError('arguments should be strings')

        new_room = None
        for room in Storage.rooms:
            if room.name == room_name:
                new_room = room
                break
        if new_room is None:
            raise RuntimeError('room {} does not exist'.format(room_name))

        person_in_qtn = None
        for person in Storage.people:
            if person.name == person_name:
                person_in_qtn = person
                break
        if person_in_qtn is None:
            raise RuntimeError('person {} does not exist'.format(person_name))

        if new_room.room_type == Office.room_type:
            person_in_qtn.office_assigned = new_room
        elif new_room.room_type == LivingSpace.room_type:
            person_in_qtn.living_space_assigned = new_room


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
