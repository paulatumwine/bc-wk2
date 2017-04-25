# Office Space Allocation

April 25, 2017 2:36 PM

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
python dojo_app.py argument(s)
```