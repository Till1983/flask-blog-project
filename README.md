# Personal Blog - Web Dev Beginner Project

This is a basic web development project by a beginner. I am using **Python**, **HTML**, **CSS**, **Javascript** (for the client-side) and the **Flask** framework to create a basic blog.
It contains a landing page, an about page, a contact page, and the blog page itself. It is also possible to create an account, to log into and out of it.

The HTML files can be found in **app** in the **templates** folder. 
The CSS file can be found in **app** in the **static** folder.

You can find a deployed version of the project [here](https://flask-blog-project-y93o.onrender.com).

## Basic Setup

Go through the following steps to install the requisite software and run the app:

1. ### Clone the repository
```
git clone https://github.com/Till1983/flask-blog-project.git
```

2. ### Move to the project folder
```
cd flask-blog-project
```

3. ### Create a virtual environment
```
python3 -m venv venv
```

4. ### Activate the virtual environment
On Linux/MacOS
```
source venv/bin/activate
````
On Windows
```
venv\Scripts\activate.bat
```

5. ### Install packages from requirements.txt
```
python -m pip install -r requirements.txt
```

6. ### Now you can run the server
```
python run.py
```
7. ### When you are done, you can deactivate the virtual environment
```
deactivate
```

## Database setup

Before you do anything else, create an `.env` file. Open the file and insert the following:
```
FLASK_ENV=development
DATABASE_URL=sqlite:///your-database-name.db
FLASK_APP=run.py
SECRET_KEY="insert secret key"
```
The **DATABASE_URL** is crucial for the setting up of the database. You need to create your own secret key.
If you include special characters in your secret key, you need to put them in quotation marks.

### Setting up SQLite for Local Development

To run this project locally, we recommend using SQLite for its simplicity and ease of setup. Follow the steps below to get started:

### 1. Download SQLite

- **macOS:** SQLite comes preinstalled on macOS. You can verify its installation by opening Terminal and typing `sqlite3`. If not installed, you can download the command-line shell tools from [SQLite Downloads](https://www.sqlite.org/download.html).

- **Windows:** Download the SQLite command-line shell and tools from [SQLite Downloads](https://www.sqlite.org/download.html). Choose the appropriate precompiled binaries for your Windows version.

- **Linux:** SQLite is often available in the package manager of most Linux distributions. You can install it using your package manager. For example, on Ubuntu, you can install it with `sudo apt-get install sqlite3`.

### 2. Initiating the Database

Once SQLite is installed, navigate to the root directory of the project in your terminal, activate the local environment, and run the following command to initialise a new SQLite database:

```bash
flask db init
```

### 3. Migrating Changes

If there are any changes to the database schema or structure, you can execute these by using using the following command:
```
flask db migrate -m 'some message'
```
You can tailor the message to the specific change that you want to implement. In this case, you want to create the database schemata that have been predefined in **app/users/models.py** and **app/blogposts/models.py**. Execute:
```
flask db migrate -m 'create models'
```

### 4. Upgrading the Database

To apply the changes finally, you execute the following command:
```
flask db upgrade
```
If you want to reverse a previous change that you have made, execute:
```
flask db downgrade
```

### 5. Connecting to the Database

You can connect to your SQLite database using various tools such as Beekeeper Studio, DB Browser for SQLite, or any other SQLite database management tool.

- **Beekeeper Studio:** Download and install Beekeeper Studio from [Beekeeper Studio](https://www.beekeeperstudio.io/). Open Beekeeper Studio and click on the "Add a Connection" button. Choose SQLite as the database type and browse to select your SQLite database file (`mydatabase.db`). Click "Connect" to establish a connection.

- **DB Browser for SQLite:** Download and install DB Browser for SQLite from [DB Browser for SQLite](https://sqlitebrowser.org/). Open the application and go to "File" > "Open Database". Browse to select your SQLite database file (`mydatabase.db`). The database will open, and you can view and edit its contents.

### 6. Inspect the Database
Once you have connected to the database, take a look at the different tables and see how they have been populated with the content of the lists in **app/scripts/seed.py**

## Testing
At this point the project contains only unit tests, which you can find find in **app/users**. Run the following command in your terminal:
```
pytest
```