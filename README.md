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

### 2. Install SurrealDB on Windows (PowerShell)

For Windows users, you can install SurrealDB using Windows PowerShell. Open PowerShell and run the following command:

```bash
iwr https://windows.surrealdb.com -useb | iex
```
This command will download and install SurrealDB on your Windows system.

### 3. Running the Flask App

Now that SurrealDB is installed, you can run the Flask application that showcases its features.

## 1. Set Flask Environment Variables
Before running the Flask app, you need to set the Flask environment variables. In your terminal or PowerShell, run the following commands:

For Windows (PowerShell):

```bash
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
```
For Linux/macOS:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```
2. Run the Flask App
With the environment variables set, you can now run the Flask application. In your terminal or PowerShell, run the following command:

```bash
flask run
```
This command will start the Flask development server, and you can access the SurrealDB Starter App in your web browser by navigating to http://localhost:5000.

### Contributing
If you'd like to contribute to this project, please feel free to fork the repository and submit a pull request. We welcome contributions and feedback from the community!

### Issues and Support
If you encounter any issues or have questions, please open an issue on this repository, and we'll do our best to assist you.

Thank you for using the SurrealDB Starter App! We hope you find it helpful to explore the capabilities of SurrealDB.
