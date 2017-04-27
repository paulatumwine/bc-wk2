import random


def generate_id():
    """
    Reusable function to generate random (object) ids
    """
    return random.randint(999, 99999)


class Storage(object):
    """
    Utility class to hold the entire program's data throughout its execution lifetime
    """

    rooms = []
    people = []
