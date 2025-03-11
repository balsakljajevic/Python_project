# Python_project
# Project Description

This project is a Online Tech Shop that allows users to create account, log in, buy and sell products. The backend is powered by Python(Flask framework), and it uses a SQLite database for storing data. The frontend is built using HTML, CSS and Bootstrap to manage the user interface.

## Files

init.py: Initializes and import basic packages that are neccessay for the app. Defines and configuresthe app and the database.
run.py: Allows the application to be run.
models.py: Configures the models such as User and Item.
routes.py: Establishes connection between templates and functions in the app.
forms.py: Configures the forms such as: LogIn form, Register form, Contact form,...
README.md: Project documentation.
static folder: Contains all the static files that are used in the app(images).
templates folder: Contains all the templates that are visible in the browser when the app is run.

## Technologies Used

Frontend: HTML, CSS, Bootstrap/Javascript
Backend: Python/Flask
Database: SQLite
Code Editor: VS Code

## Installation Instructions

Follow these steps to set up the project on your local machine.

**Prerequisites**

* XAMPP: Includes Apache and MySQL, available from here.
* A code editor (I used VSCode).

**Steps for using the app**

1. Download/Clone the Repository to your local machine:

git clone https://github.com/balsakljajevic/Python_project.git

2. Go to the "run.py" file

3. Click on the "run" button

4. Access the Project in Your Browser:

Press CTRL+link that appeared in the terminal

5. From there on you can use any of the features mentioned above

## Project File Structure

Python_project/
│
├── market        # Contains all of the files needed for the app to function
├── templates     # Contains all the templates and modals
├── static        # Contains all the images
├── venv          # Virtual environment configuration 
├── run.py        # File for running the app
└── README.md     # Project documentation                           

## How to Use

Once the project is running, you can:

Register: You can register your own account with your own credentials.
Log in/Log out: Once registered, you can freely log in or log out whenever you want.
Browse the shop: You will have a display of all the available products. You can buy items you do not have, or sell the ones you have alreadz bought.
Other pages you can visit are: Home, Project descritpion, Contact, About Us.

