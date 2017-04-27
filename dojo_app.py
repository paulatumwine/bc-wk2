"""Usage: 
    dojo_app create_room <room_type> <room_name>...
    dojo_app add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
    dojo_app add_person <arguments>...
    print_room <room_name>
    print_allocations [--outfile=FILE]
    print_unallocated [--outfile=FILE]
    reallocate_person <person_identifier> <new_room_name>
    load_people --infile=FILE
    dojo_app -i | --interactive | -h | --help | -v | --version

Options:
  -i, --interactive  interactive mode
  -h --help     Show this screen
  -v --version  Show version
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
            return func(self, opt)
        except Exception as e:
            print('Error: {}'.format(e))
            return
        except DocoptExit as e:
            print('Invalid Command: {}'.format(e))
            return
        except SystemExit:
            return

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
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""
        Room.print_room_occupants(arg['<room_name>'])

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [--outfile=FILE]"""
        if arg['--outfile']:
            Room.print_allocations(arg['--outfile'])
        else:
            Room.print_allocations()

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [--outfile=FILE]"""
        if arg['--outfile']:
            Room.print_unallocated(arg['--outfile'])
        else:
            Room.print_unallocated()

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: 
        add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
        add_person <arguments>...
        """
        DojoApp.add_a_person(arg['<arguments>'])

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """
        Usage: reallocate_person <person_identifier> <new_room_name>
        Be sure to have both of these arguments surrounded with quotes
        """
        Room.reallocate_person(arg['<person_identifier>'], arg['<new_room_name>'])

    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people --infile=FILE"""
        lines = [line.rstrip('\n') for line in open(arg['--infile'])]

        for line in lines:
            DojoApp.add_a_person(line.split(' '))

    @staticmethod
    def add_a_person(arg_list):
        """Reusable function to add a person"""
        arguments = [element.upper() for element in arg_list]
        if 'STAFF' in arguments:
            names = arg_list[0:arguments.index('STAFF')]
            name = ' '.join(names)
            Staff(name)
        elif 'FELLOW' in arguments:
            names = arg_list[0:arguments.index('FELLOW')]
            name = ' '.join(names)
            if arg_list[-1] in ['Y', 'N']:
                Fellow(name, arg_list[-1])
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
