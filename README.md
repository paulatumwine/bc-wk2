# Office Space Allocation

[![Build Status](https://travis-ci.org/paulatumwine/bc-wk2.svg?branch=master)](https://travis-ci.org/paulatumwine/bc-wk2)
[![Build Status](https://travis-ci.org/paulatumwine/bc-wk2.svg?branch=develop)](https://travis-ci.org/paulatumwine/bc-wk2)
## Intro
This project aims to provide a not-so-sketchy app to digitize and randomize a room allocation system for one of Andela Kenya’s facilities - **The Dojo**.

## Dependencies
This app depends on a number of multiple Python packages, including:
- [Docopt](https://github.com/docopt/docopt) - Since this is a CLI app, this is central to the app's overall execution.
- [SQLAlchemy](https://www.sqlalchemy.org/) - The ORM tool the app uses to persist data to an SQL data source.

## Execution
- Navigate to a directory of choice on terminal.
- Clone this repository on that directory:
```
git clone https://github.com/paulatumwine/bc-wk2.git
```
- Navigate to the repo's folder on your computer:
```
cd bc-wk2 
```
- Install the app's backend dependencies:
```
pip install -r requirements.txt
```
- And then, finally, to run the app:

```
python dojo_app.py -h
```
- Running the command above will produce output that's similar to the sample below.
```
Usage:
    dojo_app create_room <room_type> <room_name>...
    dojo_app add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
    dojo_app add_person <arguments>...
    print_room <room_name>
    print_allocations [--outfile=FILE]
    print_unallocated [--outfile=FILE]
    dojo_app -i | --interactive | -h | --help | -v | --version

Options:
  -i, --interactive  Interactive mode.
  -h --help     Show this screen.
  -v --version  Show version.
```
- To use the app, run:
```
python dojo_app.py -i
```
- Running this command brings up the app prompt, at which you can use the app interactively.
```
Welcome to The Dojo App! (Type help for a list of commands)
>>> help

Documented commands (type help <topic>):
========================================
add_person   help               print_room         quit
create_room  print_allocations  print_unallocated

>>>
```

## Tests

This project sticks with Python's inbuilt unittest package to create and execute tests. To run the project tests (from within the project root directory), run:

```python
python -m unittest discover -p *_tests.py
```
