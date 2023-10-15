# Surreal DB Starter App

Welcome to the SurrealDB Flask Starter App repository! This project demonstrates how to install Surreal DB and run a Flask application that utilizes it. If you're ready to get started, follow the instructions below.

## Prerequisites

Before you begin, make sure you have the following prerequisites installed on your system:

- Python 3.6+
- pip
- Windows PowerShell (for Windows users)

## Installation

### 1. Install SurrealDB (Server Side)

You can install SurrealDB using pip. Open your terminal and run the following command:

```bash
pip install surrealdb
```
For more details regarding installation, you can refer to SurrealDB's official documentation [here](https://surrealdb.com/docs/integration/sdks/python).

### 2. Install SurrealDB on Windows using PowerShell (Server Side)

For Windows users, you can install SurrealDB using Windows PowerShell. Open PowerShell and run the following command:

```bash
iwr https://windows.surrealdb.com -useb | iex
```
This command will download and install SurrealDB on your Windows system and you can monitor any incoming updates to your DB using this.

![backendsurreal](https://github.com/syedzubeen/surrealdb_flask_starter_app/assets/14253061/c525585d-d605-4638-93b8-99f01cca2b2b)


### 3. Running the Flask App (Client Side)

### Set Flask Environment Variables
Before running the Flask app, you need to set the Flask environment variables. In your terminal or PowerShell window, run the following commands:

For Windows:

```bash
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
```
For Linux/macOS:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```
Run the Flask App
With the environment variables set, you can now run the Flask application. In your terminal or PowerShell, run the following command:

```bash
flask run
```
This command will start the Flask development server, and you can access the SurrealDB Starter App in your web browser by navigating to http://localhost:5000.

![surrealdbstarter](https://github.com/syedzubeen/surrealdb_flask_starter_app/assets/14253061/b842b329-c6c1-4809-8f25-e9ed802ab60d)


### Contributing
If you'd like to contribute to this project, please feel free to fork the repository and submit a pull request.

### Issues and Support
If you encounter any issues or have questions, please open an issue on this repository, and I'll do my best to assist you.

Thank you for using the SurrealDB Starter App! We hope you find it helpful to explore the capabilities of SurrealDB.
