# Pet Compatibility App

This is a web application built with FastAPI that allows users to manage and find compatibility between pets based on their personality traits.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication**: Allow users to register and log in.
- **Pet Management**: Users can add, update, and delete their pets.
- **Compatibility Check**: Determine compatibility between pets based on personality traits.
- **API Integration**: Expose an API for interacting with pet data programmatically.
- **Database Persistence**: Store pet data in an SQLite database using SQLAlchemy.
- **Jinja2 Templates**: Use templates for rendering data in a simple HTML interface.

## Tech Stack

- **FastAPI**: Web framework for building APIs with Python 3.7+.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) for Python.
- **Jinja2**: Template engine for Python.
- **Pydantic**: Data validation and settings management using Python type hints.
- **SQLite**: Lightweight, file-based relational database.

## Getting Started

### Prerequisites

- Python 3.7+
- Pipenv (recommended for virtual environment management)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/pet-compatibility-app.git
cd pet-compatibility-app
```
2. Create a virtual environment and install dependencies:

```bash
pipenv install
Activate the virtual environment:
pipenv shell
pip install fastapi Jinja2 sqlalchemy
```
### Usage
Run the FastAPI application from the pet-compat-app folder:

```bash
uvicorn backend.main:app --reload
Open your browser and navigate to http://127.0.0.1:8000 to access the web application.
```

### API Documentation
  The API documentation is available at http://127.0.0.1:8000/docs when the application is running.

  ![image](https://github.com/DennisShin/pet-compat-app/assets/83376929/265dc775-229e-4660-aacb-c7f046e2e0f8)

  The API uses Jinja2 templates to show some basic information from the database. You can access this by going here: http://127.0.0.1:8000/pets/


