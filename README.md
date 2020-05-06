# Competition Finder
A simple web application to find upcoming coding contests in Codechef.com and Codeforeces.com

**Important**: A Jinja error may occur when logging-in just after a fresh sign-up, reloading the webpage will fix it and take you to the Dashboard!. This is due to some unresponsiveness of SQLite.

## Setup and Execution

### Requirements

- Python 3.6+
- Python dependencies can be installed from requirements.txt

```shell
$ pip install -r requirements.txt
```
*(Use **pip3** if both Python 2.x and Python 3.x are installed)*

### Creating SQLite Database

Initialize the database by executing this command in the root folder. *(Use **python3** if both Python 2.x and Python 3.x are installed)* 

```shell
$ python
```

This should open a python console. In the console execute

```python
>>> from main import db
>>> db.create_all()
```

(Ignore any warnings)

Exit the python console. A SQLite database *users.db* should have been created in the root folder.

### Running the Flask Server

In the root folder,

```shell
python main.py
```

*(Use **python3** if both Python 2.x and Python 3.x are installed)* 

After the server is hosted locally, open the web page by following the link on the console.

## About the application

This is a simple and light weight application which uses Flask as backend server and urllib and beatifulsoup for scraping data from competitive coding websites.

### Specifications

- **Flask** Backend
- **SQLite** for Database (Using *Flask_SQLAlchemy*)
- **urllib** and **BeautifulSoup4** for web-scraping data.
- **HTML** and **CSS** Frontend with **Bootstrap 4**
- **Flask-sessions** used to know if user is logged in.

This application is design to be minimalistic with only the required UI elements and no clutter. The user needs to be logged-in to view their Dashboard where all the competitions are neatly presented in a list-view.