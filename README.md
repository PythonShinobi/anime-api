# Anime API

## Overview

The Anime API provides a platform for users to access information about various anime series, including details such as titles, genres, and ratings. It allows users to search for specific anime, retrieve lists of top-rated series, and contribute their own reviews and ratings.

## Requirements

* Python 3.7 or higher
* Flask
* Flask-Migrate
* SQLAlchemy

## Installation

1. Clone the repository
2. Install dependencies
3. [Optional] Set up a virtual environment
4. Configure environment variables

## Configuration

To configure the API, modify the `.env` file to set environment variables such as database connection details and API keys for external services.

## Database Initialization

To initialize the database using Flask-Migrate, follow these steps:

1. Make sure you have Flask-Migrate installed (`pip install Flask-Migrate`).
2. Set up your Flask application and SQLAlchemy models.
3. Run the following commands:

    flask db init  # Initialize the migrations directory (only needed once).
       flask db migrate -m "Initial migration"# Create an initial migration.
       flask db upgrade  # Apply the migration to the database.
