# Anime API

## Overview

The Anime API provides a platform for users to access information about various anime series, including details such as titles, genres, and ratings. It allows users to search for specific anime, retrieve lists of top-rated series, and contribute their own reviews and ratings.

## Requirements

* Python 3.7 or higher
* Flask
* Flask-Migrate
* SQLAlchemy

## Installation

1.**Clone the repository:**

https://github.com/PythonShinobi/anime-api.git

2.**Navigate to the project directory:**

cd anime-api

3.**Create and activate a virtual environment:**

python -m venv venv

source venv/bin/activate   # For Unix/Linux

venv\Scripts\activate      # For Windows

4.**Install dependencies:**

pip install -r requirements.txt

5.**Set up environment variables (if necessary).**

6.Initialize and migrate the database:

flask db upgrade

7.**Run the application:**

flask run

8.**Access the application in your web browser at `http://localhost:5000`.**

## Configuration

To configure the API, modify the `.env` file to set environment variables such as database connection details and API keys for external services.

## Database Initialization

To initialize the database using Flask-Migrate, follow these steps:

1. Make sure you have Flask-Migrate installed (`pip install Flask-Migrate`).
2. Set up your Flask application and SQLAlchemy models.
3. Run the following commands:
   flask db upgrade  # Apply the migration to the database.
