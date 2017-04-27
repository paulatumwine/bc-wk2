"""Usage: 
    dojo_app.py create_room <room_type> <room_name>...
    dojo_app.py add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
    dojo_app.py add_person <arguments>...
    dojo_app.py -h | --help | -v | --version

Options:
  -h --help     Show this screen.
  -v --version  Show version.
"""
from docopt import docopt, DocoptExit

from app.person import *
from app.room import *

if __name__ == '__main__':
    """
    Main entry point for this app's execution, command logic interpreted 
    here, and the respective functionality invoked from here
    """

    args = docopt(__doc__, version='Dojo app 1.0')

    if args['create_room']:
        for room_name in args['<room_name>']:
            if 'office' == args['<room_type>']:
                Office(room_name)
            elif 'livingspace' == args['<room_type>']:
                LivingSpace(room_name)
            else:
                raise DocoptExit()

    elif args['add_person']:
        arguments = [element.upper() for element in args['<arguments>']]
        if 'STAFF' in arguments:
            names = args['<arguments>'][0:arguments.index('STAFF')]
            name = ' '.join(names)
            Staff(name)
        elif 'FELLOW' in arguments:
            names = args['<arguments>'][0:arguments.index('FELLOW')]
            name = ' '.join(names)
            Fellow(name, args['<arguments>'][-1])
        else:
            raise DocoptExit()
