"""Usage: 
    dojo_app create_room <room_type> <room_name>...
    dojo_app add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
    dojo_app add_person <arguments>...
    dojo_app -i | --interactive | -h | --help | -v | --version

Options:
  -i, --interactive  Interactive mode.
  -h --help     Show this screen.
  -v --version  Show version.
"""
import cmd
from docopt import docopt, DocoptExit

from app.person import *
from app.room import *


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:
            print('Invalid Command!')
            print(e)
            return
        except SystemExit:
            return
        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class DojoApp(cmd.Cmd):
    intro = 'Welcome to The Dojo App! (Type help for a list of commands)'
    prompt = '>>> '
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        for room_name in arg['<room_name>']:
            if 'office' == arg['<room_type>']:
                Office(room_name)
            elif 'livingspace' == arg['<room_type>']:
                LivingSpace(room_name)

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: 
        add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
        add_person <arguments>...
        """
        arguments = [element.upper() for element in arg['<arguments>']]
        if 'STAFF' in arguments:
            names = arg['<arguments>'][0:arguments.index('STAFF')]
            name = ' '.join(names)
            Staff(name)
        elif 'FELLOW' in arguments:
            names = arg['<arguments>'][0:arguments.index('FELLOW')]
            name = ' '.join(names)
            if arg['<arguments>'][-1] in ['Y', 'N']:
                Fellow(name, arg['<arguments>'][-1])
            else:
                Fellow(name)

    @staticmethod
    def do_quit(arg):
        """Returns from interactive mode"""
        print('Buh - Bye!')
        exit()


if __name__ == '__main__':
    """
    Main entry point for this app's execution, command logic interpreted 
    here, and the respective functionality invoked from here
    
    This file uses as a template, the interactive_sample.py file in the official 
    docopt Python examples at https://github.com/docopt/docopt/tree/master/examples
    """

    args = docopt(__doc__, version='Dojo app 1.0')

    if args['--interactive']:
        DojoApp().cmdloop()
